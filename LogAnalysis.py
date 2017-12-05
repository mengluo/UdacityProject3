#!/usr/bin/python3.5.2

import psycopg2

# connect to database
try:
    conn = psycopg2.connect("dbname='news' user='vagrant'")
except:
    print("unable to connect to the database")

cur = conn.cursor()
print("\nAnalysis Results:")

# analysis on what the most popular three articles of all time are
cur.execute("SELECT articles.title, topArticles.times " +
            "FROM " +
            "(SELECT " +
            "SUBSTRING(path FROM '\/article\/(.+)') AS articleName, " +
            "COUNT(*) AS times " +
            "FROM log " +
            "WHERE log.status = '200 OK' " +
            "GROUP BY path " +
            "ORDER BY COUNT(*) DESC )AS topArticles " +
            "RIGHT JOIN articles " +
            "ON articles.slug = topArticles.articleName " +
            "LIMIT 3;")
rows = cur.fetchall()
print("\n Most popular three articles of all time,")
for row in rows:
    print("  \"{}\" -- {} views".format(row[0], row[1]))

# analysis on who the most popular article authors of all time are
cur.execute("SELECT articleAuthorMap.authorName, COUNT(*) " +
            "FROM " +
            "(SELECT " +
            "articles.slug AS articleSlug, authors.name AS authorName " +
            "FROM authors JOIN articles " +
            "ON authors.id = articles.author) " +
            "AS articleAuthorMap JOIN simplifiedLog " +
            "ON articleAuthorMap.articleSlug = simplifiedLog.slug " +
            "GROUP BY articleAuthorMap.authorName " +
            "ORDER BY COUNT(*) DESC;")
rows = cur.fetchall()
print("\n Most popular article authors of all time,")
for row in rows:
    print("  {} -- {} views".format(row[0], row[1]))

# analysis on which days more than 1% of requests lead to errors
cur.execute("SELECT finalLog.Atime, " +
            "ROUND(finalLog.errorCounts/finalLog.allCounts * 100, 1)||'%' " +
            "AS errorRate " +
            "FROM " +
            "((SELECT SUM(count) AS allCounts, time AS ATime " +
            "FROM countLog GROUP BY time) " +
            "AS allCountsLog " +
            "JOIN " +
            "(SELECT count AS errorCounts, time AS ETime " +
            "FROM countLog " +
            "WHERE status = '404 NOT FOUND') " +
            "AS errorCountsLog " +
            "ON allCountsLog.Atime = errorCountsLog.Etime) " +
            "AS finalLog " +
            "WHERE (finalLog.errorCounts/finalLog.allCounts) > 0.01;")
rows = cur.fetchall()
print("\n The days that have more than 1% of requests lead to errors,")
for row in rows:
    print("  {} -- {} errors".format(row[0], row[1]))
