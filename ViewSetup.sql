-- create view for the second question
CREATE OR REPLACE VIEW simplifiedLog AS
SELECT * FROM (SELECT SUBSTRING(PATH FROM '\/article\/(.+)') AS slug, status FROM log) AS tempLog
WHERE tempLog.slug IN (SELECT slug FROM articles);

-- create view for the third question
CREATE OR REPLACE VIEW countLog AS
SELECT COUNT(*), tempLog.time, tempLog.status
FROM
((SELECT to_char(time, 'Mon dd,yyyy') AS time, id FROM log) AS timeLog
JOIN (SELECT id, status FROM log) AS statusLog
ON timeLog.id = statusLog.id) AS tempLog
GROUP BY tempLog.time, tempLog.status;
