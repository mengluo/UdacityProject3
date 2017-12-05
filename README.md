# UdacityProject3
Log Analysis

## Intro
This is a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database

## Requirements
  - [Python 3](https://www.python.org/downloads/) installed on your Mac/Windows
  - Add python.exe to PATH environmental variable if you are using Windows
  - install psql database server
  - Setup news database using `newsdata.sql` script, which includes three tables (articles, authors and log)
  - Create views needed using `ViewSetup.sql`, simplifiedLog for question 2, countLog for question 3

## Schemas for views
- schema for simplifiedLog,    
  View "public.simplifiedlog"
  | Column        | Type | Modifiers  |
  | ------------- |:----:| ----------:|
  | articlename   | text |            |
  | status        | text |            |
- articlename is the full name of the article extracted from its path

- schema for countLog,
  View "public.countlog"
  | Column | Type   | Modifiers  |
  | -------|:------:| ----------:|
  | count  | bigint |            |
  | time   | text   |            |
  | status | text   |            |
- count is the count of status of one specific type on one day

## Download and Run
  - Download the project folder `UdacityProject3` from        [GitHub](https://github.com/mengluo/UdacityProject3)
  - The folder contains four files, `README.md`, `LogAnalysis.py`, `output.png` and `ViewSetup.sql`.
  - Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip it and you will get a file called `newsdata.sql`.
  - Run command *"psql -d news -f newsdata.sql"* to connect to your installed database server and execute the create tables and populate them with data
  - Run command *"psql -d news -f ViewSetup.sql"* to import the views to the news database. You only need to do this once when setting up the database for the first time
  - `LogAnalysis.py` is the script you should use to generate the log analysis to the three questions.
  - What the script does is that it first connects to the news database server and then run queries for each question.
  - After running the script, you will get the same results shown in `output.png`
  - For Mac users, open terminal program and type *"cd ~/[your directory path]/`UdacityProject3`"* to change directory to the folder downloaded. And then type *"python3 ./LogAnalysis.py"* to run the program.
  - For Windows users, open terminal program and type *"cd [your directory path]/`UdacityProject3`"* to change directory to the folder downloaded. And then type *"python3 LogAnalysis.py"* to run the program.
