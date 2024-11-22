SELECT
    teamname, AVG(kills) AS avg_kills
FROM
    "2024_lol_esports"
GROUP BY
    teamname
ORDER BY
    avg_kills DESC
LIMIT
    1