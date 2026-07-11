-- Creating a database
CREATE DATABASE securecheck;

USE securecheck;

-- verifying the database
SELECT database();

CREATE TABLE traffic_stops (
    stop_id INT AUTO_INCREMENT PRIMARY KEY,
    stop_date DATE,
    stop_time TIME,
    country_name VARCHAR(50),
    driver_gender VARCHAR(10),
    driver_age_raw INT,
    driver_age INT,
    driver_race VARCHAR(50),
    violation_raw VARCHAR(100),
    violation VARCHAR(100),
    search_conducted BOOLEAN,
    search_type VARCHAR(100),
    stop_outcome VARCHAR(100),
    is_arrested BOOLEAN,
    stop_duration VARCHAR(20),
    drugs_related_stop BOOLEAN,
    vehicle_number VARCHAR(20)
);

-- verify the table
DESCRIBE traffic_stops;

SHOW TABLES;

SELECT COUNT(*) FROM traffic_stops;

SELECT * FROM traffic_stops LIMIT 10;

-- Top 10 vehicle numbers involved in drug-related stops
SELECT
    vehicle_number,
    COUNT(*) AS drug_stop_count
FROM traffic_stops
WHERE drugs_related_stop = TRUE
GROUP BY vehicle_number
ORDER BY drug_stop_count DESC
LIMIT 10;

-- Which vehicles were most frequently searched?
SELECT
    vehicle_number,
    COUNT(*) AS search_count
FROM traffic_stops
WHERE search_conducted = TRUE
GROUP BY vehicle_number
ORDER BY search_count DESC;

-- Which driver age group had the highest arrest rate?
SELECT
    CASE
        WHEN driver_age < 18 THEN 'Below 18'
        WHEN driver_age BETWEEN 18 AND 25 THEN '18-25'
        WHEN driver_age BETWEEN 26 AND 40 THEN '26-40'
        WHEN driver_age BETWEEN 41 AND 60 THEN '41-60'
        ELSE 'Above 60'
    END AS age_group,
    COUNT(*) AS arrest_count
FROM traffic_stops
WHERE is_arrested = TRUE
GROUP BY age_group
ORDER BY arrest_count DESC;

-- What is the gender distribution of drivers stopped in each country?
SELECT
    country_name,
    driver_gender,
    COUNT(*) AS total_stops
FROM traffic_stops
GROUP BY country_name, driver_gender
ORDER BY country_name;

-- Which race and gender combination has the highest search rate?
SELECT
    driver_race,
    driver_gender,
    COUNT(*) AS search_count
FROM traffic_stops
WHERE search_conducted = TRUE
GROUP BY driver_race, driver_gender
ORDER BY search_count DESC;

-- What time of day sees the most traffic stops?
SELECT
    HOUR(stop_time) AS stop_hour,
    COUNT(*) AS total_stops
FROM traffic_stops
GROUP BY stop_hour
ORDER BY total_stops DESC;

-- What is the average stop duration for different violations?
SELECT
    violation,
    stop_duration,
    COUNT(*) AS total_stops
FROM traffic_stops
GROUP BY violation, stop_duration
ORDER BY violation;

-- Are stops during the night more likely to lead to arrests?
SELECT
    CASE
        WHEN HOUR(stop_time) BETWEEN 18 AND 23
             OR HOUR(stop_time) BETWEEN 0 AND 5
        THEN 'Night'
        ELSE 'Day'
    END AS time_period,
    COUNT(*) AS arrest_count
FROM traffic_stops
WHERE is_arrested = TRUE
GROUP BY time_period;

-- Which violations are most associated with searches or arrests?
SELECT
    violation,
    SUM(search_conducted = TRUE) AS searches,
    SUM(is_arrested = TRUE) AS arrests
FROM traffic_stops
GROUP BY violation
ORDER BY arrests DESC;

-- Which violations are most common among younger drivers (<25)?
SELECT
    violation,
    COUNT(*) AS total_cases
FROM traffic_stops
WHERE driver_age < 25
GROUP BY violation
ORDER BY total_cases DESC;

-- Is there a violation that rarely results in search or arrest?
SELECT
    violation,
    SUM(search_conducted = TRUE) AS searches,
    SUM(is_arrested = TRUE) AS arrests
FROM traffic_stops
GROUP BY violation
ORDER BY searches ASC, arrests ASC;

-- Which countries report the highest rate of drug-related stops?
SELECT
    country_name,
    COUNT(*) AS drug_stop_count
FROM traffic_stops
WHERE drugs_related_stop = TRUE
GROUP BY country_name
ORDER BY drug_stop_count DESC;

-- What is the arrest rate by country and violation?
SELECT
    country_name,
    violation,
    COUNT(*) AS arrest_count
FROM traffic_stops
WHERE is_arrested = TRUE
GROUP BY country_name, violation
ORDER BY country_name;

-- Which country has the most stops with search conducted?
SELECT
    country_name,
    COUNT(*) AS search_count
FROM traffic_stops
WHERE search_conducted = TRUE
GROUP BY country_name
ORDER BY search_count DESC;

-- COMPLEX QUERIES
-- Yearly Breakdown of Stops and Arrests by Country
SELECT
    YEAR(stop_date) AS stop_year,
    country_name,
    COUNT(*) AS total_stops,
    SUM(is_arrested = TRUE) AS total_arrests,
    RANK() OVER (
        PARTITION BY YEAR(stop_date)
        ORDER BY COUNT(*) DESC
    ) AS country_rank
FROM traffic_stops
GROUP BY stop_year, country_name;

-- Driver Violation Trends Based on Age and Race
SELECT
    driver_race,
    CASE
        WHEN driver_age < 25 THEN 'Below 25'
        WHEN driver_age BETWEEN 25 AND 40 THEN '25-40'
        ELSE 'Above 40'
    END AS age_group,
    violation,
    COUNT(*) AS total_cases
FROM traffic_stops
GROUP BY driver_race, age_group, violation
ORDER BY total_cases DESC;

-- Number of Stops by Year, Month, and Hour
SELECT
    YEAR(stop_date) AS year,
    MONTH(stop_date) AS month,
    HOUR(stop_time) AS hour,
    COUNT(*) AS total_stops
FROM traffic_stops
GROUP BY year, month, hour
ORDER BY year, month, hour;

-- Violations with High Search and Arrest Rates
SELECT
    violation,
    SUM(search_conducted = TRUE) AS searches,
    SUM(is_arrested = TRUE) AS arrests,
    DENSE_RANK() OVER (
        ORDER BY SUM(is_arrested = TRUE) DESC
    ) AS violation_rank
FROM traffic_stops
GROUP BY violation;

-- Driver Demographics by Country
SELECT
    country_name,
    driver_gender,
    driver_race,
    AVG(driver_age) AS average_age,
    COUNT(*) AS total_drivers
FROM traffic_stops
GROUP BY country_name, driver_gender, driver_race;

-- Top 5 Violations with Highest Arrest Rates
SELECT
    violation,
    COUNT(*) AS arrest_count
FROM traffic_stops
WHERE is_arrested = TRUE
GROUP BY violation
ORDER BY arrest_count DESC
LIMIT 5;

