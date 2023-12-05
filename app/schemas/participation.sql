CREATE TABLE participation (
    movie_id INTEGER REFERENCES movies(id),
    actor_id INTEGER REFERENCES actors(id),
    is_director BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (movie_id, actor_id),
    UNIQUE (movie_id, actor_id)
);
