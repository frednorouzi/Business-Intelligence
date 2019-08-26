# Project: Data Modeling with Postgres

* Introduction
A startup called Sparkify wants to analyze the data in order to know what songs users are listening to. For reaching this aim, I created a Postgres database with tables designed to optimize queries and ETL pipeline on song play analysis. Requirement data resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.


* Project Description
In this project, I apply on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, I define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.
Following picture showes entity relationship diagram between songplays as a Fact table and four dimention tables included users, songs, artists and time.

* Project Repository files
In addition to the data files (song_data and log_data), the project includes six files:
test.ipynb displays the first few rows of each table to let user check database.
create_tables.py drops and creates tables. It should run to reset tables before each time user run ETL scripts.
etl.ipynb reads and processes a single file from song_data and log_data and loads the data into tables. 
etl.py reads and processes files from song_data and log_data and loads them into tables. 
sql_queries.py contains all your sql queries, and is imported into the last three files above.

* Database Design:
I created a stat schema by extracting the song and log dataset. The dimension tables represents the database applications designed according to the needs of the individual user and it may also have descriptive attributes. In this case I defined four dimension tables inclusive: users, songs, artists and time. 
Fact table in this project bring dimension keys and measures to facilitate business process analysis at a specific grain. Fact table in this project is songplays.  

* ETL Process (pipeline)
process_song_file: This procedure processes to read the song file and insert data into song and artist dimension table.
process_log_file: This procedure processes to read log file and insert data into user, time as dimension tables and songplays as a facttable.
process_data: collect all the file paths and call the two defined function to perform etl process.
* How To Run the Project
Below are steps user can follow to run the project:
1- Run create_tables.py to create database and tables.
2- Run etl.py to read & process from song_data/log_data and loads them into tables.
3- Run test.ipynb to confirm that records were successfully inserted into each table.