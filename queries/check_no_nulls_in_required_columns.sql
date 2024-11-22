SELECT
    COUNT(*) AS null_count
FROM
    "2024_lol_esports"
WHERE
    {{column_name}} IS NULL