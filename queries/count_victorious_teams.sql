SELECT
    COUNT(DISTINCT teamname) AS victorious_teams
FROM
    "2024_lol_esports"
WHERE
    result = 1