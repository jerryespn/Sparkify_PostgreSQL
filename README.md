# Udacity - Data Engineer Nanodegree - Sparkify - Postgresql Database Modeling Project

## About this project

Sparkify dataset is a database that contains music and artist records created for educational purposes.
The data extracted from this database it's on a json format and its available at this repository in [data](./data) folder.

For this project two datasets were used: songs and log data. 

- Song json files, were used to get the information about songs (of course) and artist.
- Log json files, were used to get the information about covers song, artist and the complementary information for each song. 

## Prerequisites to use this repository

1. Python 3.x
1. Postgresql (The Database creation it's also included at this repository)
1. Jupyter Notebook (Recommended, to install with Anaconda)
1. Windows/Mac/Linux - Compatible
2. Firefox, Chrome, Edge Navigators - Compatible

## Deployment instructions

From terminal, command line or kind of:


1. Execute as follows:
	1. `$ python ./create_tables.py` - This script is intended to create database and tables
	2. `python ./etl.py` - This scripts is intended to load data from dataset into database Sparkify Tables  

Just to test purposes there is another file called **test.ipynb**

----------
**TESTING:**

Sparkify DB Connection:

![Sparkify DB Connect][img1]

Users Table:

![Users TEST][img2]

Artist Table:

![Artist TEST][img3]

Songs Table:

![Songs TEST][img4]

SongPlays Table:

![SongPlays TEST][img5]


[img1]: images/Sparkify_DB_Connection.jpg "Sparkify DB Connect"
[img2]: images/Users_Table.jpg "Users Test"
[img3]: images/artist_table.jpg "Artist Test"
[img4]: images/Songs_Table.jpg "Song table Test"
[img5]: images/SongPlays_table.jpg "SongPlays Test"