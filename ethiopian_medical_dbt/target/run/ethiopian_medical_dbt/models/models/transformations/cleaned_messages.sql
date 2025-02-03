
  create view "telegram_data"."public"."cleaned_messages__dbt_tmp"
    
    
  as (
    SELECT
    message_id,
    channel,
    sender_id,
    text,
    date::date AS message_date,
    CASE
        WHEN text IS NULL THEN 'No text'
        ELSE text
    END AS cleaned_text
FROM
    telegram_data
WHERE
    text IS NOT NULL
  );