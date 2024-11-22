SELECT
    COUNT(*) AS negative_count
FROM
    "2024_lol_esports"
WHERE
    kills < 0
    OR
    deaths < 0
    OR
    assists < 0
    OR
    gamelength < 0