/* Calculate the total amount deposited by each user in each region. */

SELECT ut.consumer_id,
       wr.region_name,
       SUM(ut.transaction_amount) AS total_deposits
FROM user_transaction ut 
LEFT JOIN user_nodes un 
ON ut.consumer_id = un.consumer_id
LEFT JOIN world_regions wr 
ON un.region_id = wr.region_id 
WHERE ut.transaction_type = 'deposit'
GROUP BY ut.consumer_id, wr.region_name;
