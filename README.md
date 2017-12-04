# UdacityProject3
Log Analysis

## Intro
This is a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database

## Requirements

  - [Python 3](https://www.python.org/downloads/) installed on your Mac/Windows
  - Add python.exe to PATH environmental variable if you are using Windows
  - install psql database server
  - Create tables (articles, authors and log)
  - views needed: simplifiedLog for question 2, countLog for question 3

## Schemas for views

- schema for simplifiedLog,    
  View "public.simplifiedlog"
  Column    | Type | Modifiers
  -------------+------+-----------
  articlename | text |
  status      | text |
- articlename is the full name of the article extracted from its path

- schema for countLog,
  View "public.countlog"
  Column |  Type  | Modifiers
  --------+--------+-----------
  count  | bigint |
  time   | text   |
  status | text   |
- count is the count of status of one specific type on one day

## Download and Run
  - Download the project folder `UdacityProject3` from        [GitHub](https://github.com/mengluo/UdacityProject3)
  - The folder contains three files, README.md, LogAnalysis.py and output.png.
  - LogAnalysis.py is the script you should use to generate the log analysis to the three questions.
  - What the script does is that it first connects to the news database server and then run queries for each question. Note that, views are created for question 2 and question 3. If these two view are already created, creating view process will be skipped.
  - After running the script, you will get the same results shown in output.png
  - For Mac users, open terminal program and type *"cd ~/[your directory path]/`UdacityProject3`"* to change directory to the folder downloaded. And then type *"python3 ./LogAnalysis.py"* to run the program.
  - For Windows users, open terminal program and type *"cd [your directory path]/`UdacityProject3`"* to change directory to the folder downloaded. And then type *"python3 LogAnalysis.py"* to run the program.
