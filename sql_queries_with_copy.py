# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""

CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY,
    ts TIMESTAMP NOT NULL REFERENCES TIME(start_time),
    userId INT NOT NULL,
    level TEXT,
    songid VARCHAR REFERENCES songs(song_id),
    artistid VARCHAR REFERENCES artists(artist_id),
    sessionId INT NOT NULL,
    location TEXT,
    user_agent TEXT
);
""")

user_table_create = ("""

CREATE TABLE IF NOT EXISTS users (
    userId INT PRIMARY KEY,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    gender VARCHAR,
    level TEXT
);
""")

song_table_create = ("""

CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR PRIMARY KEY,
    title TEXT NOT NULL,
    artist_id VARCHAR NOT NULL,
    year INT,
    duration NUMERIC NOT NULL
);
""")

artist_table_create = ("""

CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR PRIMARY KEY,
    artist_name TEXT NOT NULL,
    artist_location TEXT,
    artist_latitude REAL,
    artist_longitude REAL
);
""")

time_table_create = ("""

CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP PRIMARY KEY,
    hour INT,
    day INT,
    week INT,
    month INT,
    year INT,
    weekday VARCHAR
);
""")

# INSERT RECORDS

songplay_table_copy = ("""

INSERT INTO songplays (
    ts, userId, level, songid, artistid, sessionId, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_copy = ("""

COPY users (userId, firstName, lastName, gender, level)
    FROM "C:\Users\owner\Documents\Online Classes\Udacity\Data Engineering Nanodegree\Projects\Course 1_Data Modeling_Data Modeling with Postgres\data\song_data\songs.csv"
    DELIMITER ','
    CSV HEADER;

""")

song_table_copy = ("""

COPY songs (song_id, title, artist_id, year, duration)
    FROM "C:\Users\owner\Documents\Online Classes\Udacity\Data Engineering Nanodegree\Projects\Course 1_Data Modeling_Data Modeling with Postgres\data\song_data\songs.csv"
    DELIMITER ','
    CSV HEADER;

""")

artist_table_copy = ("""

COPY artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
    DELIMITER ','
    CSV HEADER;

""")

time_table_copy = ("""

COPY time (start_time, hour, day, week, month, year, weekday)
    FROM 'songs.csv' WITH DELIMITER
    ON CONFLICT (start_time) DO NOTHING

""")

# FIND SONGS

song_select = ("""

SELECT s.song_id,
       a.artist_id
FROM songs s
JOIN artists a
        ON s.artist_id = a.artist_id
WHERE s.title = %s AND a.artist_name = %s AND s.duration = %s;

""")

# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
