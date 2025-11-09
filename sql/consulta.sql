SELECT
  b.zone,
  SUM(l.amount) AS total_amount
FROM loans_clean l
JOIN branches b ON l.branch_id = b.branch_id
GROUP BY b.zone
ORDER BY total_amount DESC;