/* Calculate the total amount deposited for each user in the "Europe" region. */


SELECT t.consumer_id,
       SUM(transaction_amount) AS total_transaction
FROM world_regions w 
JOIN user_nodes n 
ON w.region_id = n.region_id 
JOIN user_transaction t  
ON n.consumer_id = t.consumer_id
WHERE region_name = 'Europe' AND transaction_type = 'deposit'
GROUP BY t.consumer_id;

