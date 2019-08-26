# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
songplay_id SERIAL not null PRIMARY KEY,
start_time timestamp not null,
user_id varchar not null,
level varchar, 
song_id varchar,
artist_id varchar,
session_id varchar not null,
location text,
user_agent text
)
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
user_id varchar not null PRIMARY KEY,
first_name varchar not null, 
last_name varchar not null,
gender varchar,
level varchar
)
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
song_id varchar not null PRIMARY KEY,
title text,
artist_id varchar not null,
year int,
duration numeric
)
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
artist_id varchar not null PRIMARY KEY,
name varchar,
location text,
latitude decimal(10,8),
longitude decimal(11,8)
)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
start_time timestamp not null PRIMARY KEY,
hour int,
day int,
week int,
month int,
year int,
weekday int
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, 
song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, a.artist_id
FROM songs AS s 
JOIN artists AS a ON 
s.artist_id = a.artist_id
WHERE s.title = %s
AND a.name = %s
AND s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]