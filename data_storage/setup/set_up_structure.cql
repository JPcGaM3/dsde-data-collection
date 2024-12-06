CREATE KEYSPACE IF NOT EXISTS space WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE IF NOT EXISTS space.result_table (
    id INT,
    year INT,
    title TEXT,
    publicationname TEXT,
    citedbycount INT,
    asia INT,
    oceania INT,
    europe INT,
    north_america INT,
    south_america INT,
    africa INT,
    keywords_list TEXT,
    cluster INT,
    keyword_category TEXT,
    PRIMARY KEY (id, year, title)
);
