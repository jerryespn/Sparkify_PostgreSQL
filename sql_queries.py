# Sparkify - Data Engineer Nanodegree program SQL Data Model Project
# By JGEL
# February 2020

# DROP TABLES

user_table_drop = "DROP TABLE users"
songplay_table_drop = "DROP TABLE songplays"
song_table_drop = "DROP TABLE songs"
artist_table_drop = "DROP TABLE artists"
time_table_drop = "DROP TABLE time"

# CREATE TABLES

songplay_table_create = ("""
	CREATE TABLE IF NOT EXISTS songplays (songplay_id serial PRIMARY KEY, start_time timestamp NOT NULL, 
										user_id int NOT NULL, level varchar, song_id varchar NULL, 
										artist_id varchar NULL, session_id int, location varchar,
										user_agent varchar);
""")

user_table_create = ("""
	CREATE TABLE IF NOT EXISTS users (user_id varchar PRIMARY KEY, first_name varchar,
									  last_name varchar, gender varchar, level varchar);
""")

song_table_create = ("""
	CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY, title varchar, artist_id varchar NOT NULL, 
										year int, duration float);
""")

artist_table_create = ("""
	CREATE TABLE IF NOT EXISTS artists (artist_id varchar NOT NULL, name varchar, location varchar,
										latitude real NULL, longitude real NULL);
""")

time_table_create = ("""
	CREATE TABLE IF NOT EXISTS time (start_time timestamp, hour int, day varchar, week int, month int, year int, weekday varchar);
""")

# INSERT RECORDS

songplay_table_insert = ("""
	INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                 VALUES (to_timestamp(%s), %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
	INSERT INTO users (user_id, first_name, last_name, gender, level)
	             VALUES (%s, %s, %s, %s, %s)
				 ON CONFLICT (user_id) DO UPDATE
				 	SET first_name = excluded.first_name,
					 	last_name = excluded.last_name,
						gender = excluded.gender, 
					 	level = EXCLUDED.level;
""")

song_table_insert = ("""
	INSERT INTO songs (song_id, title, artist_id, year, duration)
	            VALUES (%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
	INSERT INTO artists (artist_id, name, location, latitude, longitude)
                 VALUES (%s, %s, %s, %s, %s);
""")


time_table_insert = ("""
	INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                 VALUES (%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
	SELECT s.song_id, a.artist_id 
	FROM songs s
	LEFT OUTER JOIN artists a
		ON s.artist_id = a.artist_id
	WHERE s.title = %s 
		AND a.name = %s 
		AND s.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]