CREATE KEYSPACE IF NOT EXISTS space1 WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE IF NOT EXISTS space1.table1 (
    Year INT,
    Title TEXT,
    PublicationName TEXT,
    CitedByCount INT,
    Asia INT,
    Oceania INT,
    Europe INT,
    North_America INT,
    South_America INT,
    Africa INT,
    keywords_list TEXT,
    cluster TEXT,
    keyword_category TEXT,
    processed_time TIMESTAMP,
    PRIMARY KEY (Year, Title)
);
