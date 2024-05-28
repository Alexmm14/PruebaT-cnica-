CREATE VIEW daily_transactions AS
SELECT c.company_name, date_trunc('day', ch.created_at) AS day, SUM(ch.amount) AS total_amount
FROM charges ch
JOIN companies c ON ch.company_id = c.company_id
GROUP BY c.company_name, day;
