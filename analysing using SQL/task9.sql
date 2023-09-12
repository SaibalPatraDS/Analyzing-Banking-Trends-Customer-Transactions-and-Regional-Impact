/* Retrieve the total number of transactions for each region. */

SELECT region_name, 
       COUNT(ut.transaction_type) AS total_transactions
FROM world_regions AS wr 
JOIN user_nodes AS un 
ON  wr.region_id = un.region_id
JOIN user_transaction ut 
USING (consumer_id)
GROUP BY region_name;
