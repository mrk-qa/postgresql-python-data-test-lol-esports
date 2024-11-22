SELECT
    COUNT(*) AS games_with_first_blood
FROM
    "2024_lol_esports"
WHERE
    firstblood = 1