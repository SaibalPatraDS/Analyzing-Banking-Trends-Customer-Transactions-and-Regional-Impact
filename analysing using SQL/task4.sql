/* Calculate the total number of transactions made by each user in the "United States" region.*/
 
SELECT DISTINCT t.consumer_id,
      COUNT(t.consumer_id) AS total_transactions
FROM user_transaction t 
LEFT JOIN user_nodes n 
ON t.consumer_id = n.consumer_id
JOIN world_regions w 
ON n.region_id = w.region_id 
WHERE region_name = 'United States'
GROUP BY t.consumer_id;
