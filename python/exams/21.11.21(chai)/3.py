# SELECT c.name,
#        c.phone,
#        SUM(CASE WHEN h.direction = 'in' THEN h.duration END +
#        CASE WHEN h.direction = 'out' AND h.duration > 120 THEN 500 + 2*(h.duration-120)
#             WHEN h.direction = 'out' AND h.duration <= 120 THEN 500
#        END) as TotalCost
# FROM customer c
# JOIN (SELECT 'out' as directon, duration, dialed_on, outgoing_phone as phone
#       FROM history
#       WHERE YEAR(dialed_on) = 1995
#       AND MONTH(dialed_on) = 1
#       UNION ALL
#       SELECT 'in' as direction, duration, dialed_on, incoming_phone as phone
#       FROM history
#       WHERE YEAR(dialed_on) = 1995
#       AND MONTH(dialed_on) = 1
#      ) h ON c.phone = h.phone
# GROUP BY c.name,
#          c.phone
#
#
#
#
# SELECT c.name, c.phone_number, SUM(case when h.direction = 'in' THEN h.duration END + case when h.direction = 'out' AND h.duration > 120 THEN 500 + 2 * (h.duration-120) when h.direction = 'out' and h.duration <= 120 then 500 END) as call_units from customer_detail c join (select 'out' as direction, as outgoing_number as phone_number from call_record where YEAR(dialed_on) = 2018 AND MONTH(dialed_on) = 5 union all select 'in' as direction, incomming_number as phone_number from call_record where YEAR(dialed_on) = 2018 AND MONTH(dialed_on) = 5) r ON c.phone_number = r.phone_number GROUP BY c.name, c.phone_number