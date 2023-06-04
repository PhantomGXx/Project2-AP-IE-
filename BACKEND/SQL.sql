CREATE DATABASE mydatabase;
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    price FLOAT NOT NULL,
    category VARCHAR(50) NOT NULL
);