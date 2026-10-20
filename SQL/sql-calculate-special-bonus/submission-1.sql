SELECT 
    e.employee_id, 
    CASE
        WHEN e.employee_id % 2 != 0 and e.name not like 'M%' THEN e.salary
        ELSE 0
    END as bonus
from employees as e
ORDER by e.employee_id;