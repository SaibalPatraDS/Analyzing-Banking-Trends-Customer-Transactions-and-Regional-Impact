/*
How many transactions were made by consumers from each region?
*/

SELECT wr.region_name,
       COUNT(ut.consumer_id) AS total_transactions
FROM world_regions wr 
LEFT JOIN user_nodes un 
ON wr.region_id = un.region_id
JOIN user_transaction ut 
ON ut.consumer_id = un.consumer_id
GROUP BY wr.region_id, wr.region_name;
