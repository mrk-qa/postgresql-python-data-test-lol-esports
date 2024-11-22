SELECT
    SUM(CASE WHEN side = 'Blue' AND result = 1 THEN 1 ELSE 0 END) AS blue_wins,
    SUM(CASE WHEN side = 'Red' AND result = 1 THEN 1 ELSE 0 END) AS red_wins
FROM
    "2024_lol_esports"