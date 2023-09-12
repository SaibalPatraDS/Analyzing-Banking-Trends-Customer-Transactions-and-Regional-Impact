/*
Write a query to find the top 5 consumers 
who have made the highest total transaction amount (sum of all their deposit transactions) in the user_transaction table.
*/


SELECT consumer_id,
       SUM(transaction_amount) AS total_transaction
FROM user_transaction ut
WHERE transaction_type = 'deposit'
GROUP BY consumer_id
ORDER BY total_transaction DESC
LIMIT 5;
