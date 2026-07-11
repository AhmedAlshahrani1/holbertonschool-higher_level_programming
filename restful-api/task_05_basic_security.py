#!/usr/bin/python3
"""Module that implements API security and authentication techniques"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "my-super-secret-key-change-me"
auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verifies username and password for basic authentication"""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protected by basic authentication"""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Logs in a user and returns a JWT access token"""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        token = create_access_token(
            identity=username,
            additional_claims={"role": user["role"]}
        )
        return jsonify({"access_token": token})
    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protected by JWT authentication"""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route accessible only to admin users"""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handles missing token errors"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handles invalid token errors"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handles expired token errors"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handles revoked token errors"""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handles fresh token required errors"""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
