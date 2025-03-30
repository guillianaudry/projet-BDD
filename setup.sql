CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE transport_costs (
    id SERIAL PRIMARY KEY,
    from_city_id INT REFERENCES cities(id),
    to_city_id INT REFERENCES cities(id),
    duration INTERVAL NOT NULL
);

INSERT INTO cities (name) VALUES ('Paris'), ('Madrid'), ('Rome'), ('Berlin'), ('Londre'), ('Lisbon');
INSERT INTO transport_costs (from_city_id, to_city_id, duration) VALUES 
    (1, 2, '2 hours'),
    (1, 3, '3 hours'),
    (1, 4, '4 hours'),
    (1, 5, '5 hours'),
    (1, 6, '6 hours'),
    (2, 1, '2 hours'),
    (2, 3, '1 hour'),
    (2, 4, '2 hours'),
    (2, 5, '3 hours'),
    (2, 6, '4 hours'),
    (3, 1, '3 hours'),
    (3, 2, '1 hour'),
    (3, 4, '1 hour'),
    (3, 5, '2 hours'),
    (3, 6, '3 hours'),
    (4, 1, '4 hours'),
    (4, 2, '2 hours'),
    (4, 3, '1 hour'),
    (4, 5, '1 hour'),
    (4, 6, '2 hours'),
    (5, 1, '5 hours'),
    (5, 2, '3 hours'),
    (5, 3, '2 hours'),
    (5, 4, '1 hour'),
    (5, 6, '1 hour'),
    (6, 1, '6 hours'),
    (6, 2, '4 hours'),
    (6, 3, '3 hours'),
    (6, 4, '2 hours'),
    (6, 5, '1 hour');

