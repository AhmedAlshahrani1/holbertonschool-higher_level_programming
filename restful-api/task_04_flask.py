#!/usr/bin/python3
"""Module that develops a simple API using Flask"""
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """Returns a welcome message"""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Returns a list of all usernames"""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns API status"""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object of the given username"""
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user from the POSTed JSON data"""
    user_data = request.get_json(silent=True)
    if user_data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    username = user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409
    users[username] = {
        "username": username,
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
