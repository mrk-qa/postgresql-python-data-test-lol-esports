SELECT
    gameid, champion, COUNT(*) AS repeated_champions
FROM
    "2024_lol_esports"
WHERE
    champion IS NOT NULL
    AND
    champion <> ''
GROUP BY
    gameid, champion
HAVING
    COUNT(*) > 1