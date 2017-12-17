#!/usr/bin/env python3.5

import psycopg2

def db_connect():
    """ Creates and returns a connection to the database defined by DBNAME,
        as well as a cursor for the database.

        Returns:
            db, c - a tuple. The first element is a connection to the database.
                    The second element is a cursor for the database.
    """
    try:
        conn = psycopg2.connect("dbname='news' user='vagrant'")
    except (Exception, DatabaseError) as error:
        print(error)

    cur = conn.cursor()
    return (conn, cur)

def execute_query(query, cur):
    """execute_query takes an SQL query as a parameter.
        Executes the query and returns the results as a list of tuples.
       args:
           query - an SQL query statement to be executed.

       returns:
           A list of tuples containing the results of the query.
    """
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def print_top_articles(cur):
    """Prints out the top 3 articles of all time."""
    query = """SELECT articles.title, topArticles.times
                FROM
                (SELECT
                SUBSTRING(path FROM '\/article\/(.+)') AS articleName,
                COUNT(*) AS times
                FROM log
                WHERE log.status = '200 OK'
                GROUP BY path
                ORDER BY COUNT(*) DESC )AS topArticles
                RIGHT JOIN articles
                ON articles.slug = topArticles.articleName
                LIMIT 3;"""
    results = execute_query(query, cur)
    print("\n Most popular three articles of all time,")
    for title, times in results:
        print("  \"{}\" -- {} views".format(title, times))

def print_top_authors(cur):
    """Prints a list of authors ranked by article views."""
    query = """SELECT articleAuthorMap.authorName, COUNT(*) as count
                FROM
                (SELECT
                articles.slug AS articleSlug, authors.name AS authorName
                FROM authors JOIN articles
                ON authors.id = articles.author)
                AS articleAuthorMap JOIN simplifiedLog
                ON articleAuthorMap.articleSlug = simplifiedLog.slug
                GROUP BY articleAuthorMap.authorName
                ORDER BY COUNT(*) DESC;"""
    results = execute_query(query, cur)
    print("\n Most popular article authors of all time,")
    for authorName, count in results:
        print("  {} -- {} views".format(authorName, count))

def print_errors_over_one(cur):
    """Prints out the days where more than 1% of logged access requests were errors."""
    query = """SELECT finalLog.Atime,
                ROUND(finalLog.errorCounts/finalLog.allCounts * 100, 1)||'%'
                AS errorRate
                FROM
                ((SELECT SUM(count) AS allCounts, time AS ATime
                FROM countLog GROUP BY time)
                AS allCountsLog
                JOIN
                (SELECT count AS errorCounts, time AS ETime
                FROM countLog
                WHERE status = '404 NOT FOUND')
                AS errorCountsLog
                ON allCountsLog.Atime = errorCountsLog.Etime)
                AS finalLog
                WHERE (finalLog.errorCounts/finalLog.allCounts) > 0.01;"""
    results = execute_query(query, cur)
    print("\n The days that have more than 1% of requests lead to errors,")
    for Atime, errorRate in results:
        print("  {} -- {} errors".format(Atime, errorRate))


if __name__ == '__main__':

    (conn, cur) = db_connect()
    print("\nAnalysis Results:")

    # analysis on what the most popular three articles of all time are
    print_top_articles(cur)

    # analysis on who the most popular article authors of all time are
    print_top_authors(cur)

    # analysis on which days more than 1% of requests lead to errors
    print_errors_over_one(cur)
