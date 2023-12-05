CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    director VARCHAR(50) NOT NULL,
    release_year VARCHAR(50) NOT NULL,
    length_min INTEGER NOT NULL,
    UNIQUE (title, director)
);