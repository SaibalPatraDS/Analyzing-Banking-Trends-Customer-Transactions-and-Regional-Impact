/* Write a query to find the total deposit amount for each region (region_name) in the user_transaction table. 
Consider only those transactions where the consumer_id is associated with a valid region in the user_nodes table.*/

SELECT region_name,
       SUM(transaction_amount) AS total_transaction
FROM user_transaction ut 
JOIN user_nodes un 
ON ut.consumer_id = un.consumer_id
JOIN world_regions wr 
ON wr.region_id = un.region_id
WHERE transaction_type = 'deposit'
GROUP BY region_name;
