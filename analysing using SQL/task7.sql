/* Find the user who made the largest deposit amount in the "Australia" region.*/


SELECT  t.consumer_id,
       MAX(transaction_amount) AS largest_deposit
FROM user_transaction t
JOIN user_nodes n 
ON t.consumer_id = n.consumer_id
JOIN world_regions w 
ON w.region_id = n.region_id
WHERE region_name = 'Australia' AND transaction_type = 'deposit'
GROUP BY t.consumer_id
ORDER BY largest_deposit DESC
LIMIT 1;
