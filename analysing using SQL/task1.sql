/* List all regions along with the number of users assigned to each region. */


-- List all regions along with the number of users assigned to each region.

SELECT w.region_name,
      COUNT(DISTINCT consumer_id) AS users
FROM user_nodes n 
RIGHT JOIN world_regions w 
On n.region_id = w.region_id
GROUP BY region_name
ORDER BY region_name;
