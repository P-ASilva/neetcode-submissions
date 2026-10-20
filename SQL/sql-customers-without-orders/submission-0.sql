SELECT c.name from customers as c
LEFT JOIN orders as o on c.id = o.customer_id
WHERE o.id is NULL
GROUP BY c.id;
