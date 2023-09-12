/*Calculate the total number of users who made more than 5 transactions.*/

SELECT consumer_id, 
       COUNT(consumer_id) AS num_transactions
FROM user_transaction t  
GROUP BY consumer_id
HAVING COUNT(transaction_type) > 5;
