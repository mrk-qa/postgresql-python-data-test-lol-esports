SELECT
    champion, COUNT(*) AS pick_count
FROM
    "2024_lol_esports"
GROUP BY
    champion
ORDER BY
    pick_count DESC
LIMIT
    10