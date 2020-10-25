SELECT (price*amount) AS total FROM items

-- Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

-- SQL: return results in a column named greeting
select concat('Hello, ',name,' how are you doing today?') as greeting from person

-- Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

-- You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

-- For example:

-- time = 3 ----> litres = 1

SELECT id, hours, floor(hours *.5) as liters 
FROM cycling

-- Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.
-- you will be given a table 'kata' with columns 'n', 'x', and 'y'. Return the 'id' and your result in a column named 'res'.
select id, (n % x = 0 and n % y = 0) as res 
from kata