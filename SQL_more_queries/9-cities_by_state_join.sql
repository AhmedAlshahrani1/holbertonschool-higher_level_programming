-- Lists all cities with their state name, sorted by cities.id, using one SELECT with JOIN
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
