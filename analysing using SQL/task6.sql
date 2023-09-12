/* Find the regions with the highest number of nodes assigned to them. */

SELECT w.region_name,
       COUNT(node_id) AS total_nodes
FROM world_regions w 
JOIN user_nodes n  
ON w.region_id = n.region_id
GROUP BY region_name
ORDER BY total_nodes DESC;
