  SELECT *,
       SUM(is_new_session) OVER (ORDER BY created_ts) AS session_id,
       FROM (
        SELECT *,
              CASE WHEN EXTRACT('EPOCH' FROM created_ts) - EXTRACT('EPOCH' FROM last_event) >= 60
                     OR last_event IS NULL 
                   THEN 1 ELSE 0 END AS is_new_session
         FROM (
              SELECT *,
                     LAG(created_ts,1) OVER (ORDER BY created_ts) AS last_event
                FROM  events
              )
       )
