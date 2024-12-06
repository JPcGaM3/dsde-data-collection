CREATE KEYSPACE IF NOT EXISTS space WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
USE testspace;

CREATE TABLE IF NOT EXISTS space.result_table (
    id INT PRIMARY KEY,
    name TEXT,
    age INT
);