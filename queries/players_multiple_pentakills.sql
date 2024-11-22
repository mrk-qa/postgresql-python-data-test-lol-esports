SELECT
    playername, COUNT(pentakills) AS pentakill_count
FROM
    "2024_lol_esports"
WHERE
    pentakills IS NOT NULL
    AND
    pentakills <> ''
    AND
    playername IS NOT NULL
    AND
    playername <> ''
    AND
    CAST(pentakills AS INTEGER) > 0
GROUP BY
    playername
HAVING
    COUNT(pentakills) > 1