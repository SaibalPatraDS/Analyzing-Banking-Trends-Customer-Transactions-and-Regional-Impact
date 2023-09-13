/*
What is the unique count and total amount for each transaction type?
*/

SELECT transaction_type,
       COUNT(DISTINCT consumer_id) AS unique_transaction,
       SUM(transaction_amount) AS total_transaction
FROM user_transaction
GROUP BY transaction_type;
