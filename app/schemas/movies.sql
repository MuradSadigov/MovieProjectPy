CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50),
    director VARCHAR(50),
    release_year VARCHAR(50),
    actors VARCHAR(50),
    length INTEGER
);