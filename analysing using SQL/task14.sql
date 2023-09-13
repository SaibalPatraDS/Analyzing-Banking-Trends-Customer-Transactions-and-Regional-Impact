/*
What are the average deposit counts and amounts for each transaction type ('deposit') across all customers, grouped by transaction type?
*/

/*
(Hint:You can achieve this by using a CTE to calculate deposit counts and amounts for each customer, 
and then in the main query, group by transaction type ('deposit') to find the rounded average deposit counts and amounts. 
Use the ROUND() function for rounding.)
*/

WITH users AS (
    SELECT consumer_id,
           transaction_type,
           COUNT(transaction_type) AS total_transactions,
           SUM(transaction_amount) AS total_amount
    FROM user_transaction
    WHERE transaction_type = 'deposit'
    GROUP BY consumer_id)

SELECT transaction_type,
       ROUND(AVG(total_transactions),0) AS avg_transactions,
       ROUND(AVG(total_amount),0) AS avg_amount
FROM users
GROUP BY transaction_type;
