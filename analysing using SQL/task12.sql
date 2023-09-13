/*
How many consumers are allocated to each region?
*/


SELECT wr.region_id,
       region_name,
       COUNT(DISTINCT consumer_id) AS total_consumer
FROM world_regions wr 
JOIN user_nodes un 
ON wr.region_id = un.region_id
GROUP BY region_name;
