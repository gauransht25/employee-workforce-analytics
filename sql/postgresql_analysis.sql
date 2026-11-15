-- Synthetic employee data; PostgreSQL
CREATE TABLE IF NOT EXISTS employees_raw (
 employee_id INTEGER PRIMARY KEY, department TEXT, job_title TEXT, gender TEXT,
 age INTEGER, state TEXT, work_location TEXT, hire_date DATE, termination_date DATE
);
-- In psql: \copy employees_raw FROM 'data/employees_synthetic.csv' CSV HEADER;
CREATE OR REPLACE VIEW employees_clean AS
SELECT *, (termination_date IS NOT NULL AND termination_date <= DATE '2026-11-15') AS terminated,
 EXTRACT(YEAR FROM AGE(COALESCE(termination_date, DATE '2026-11-15'),hire_date)) AS tenure_years
FROM employees_raw
WHERE age BETWEEN 18 AND 100 AND (termination_date IS NULL OR termination_date <= DATE '2026-11-15');
-- 11 workforce questions
SELECT gender, COUNT(*) FROM employees_clean GROUP BY gender;
SELECT CASE WHEN age < 25 THEN '18-24' WHEN age < 35 THEN '25-34' WHEN age < 45 THEN '35-44' WHEN age < 55 THEN '45-54' ELSE '55+' END age_band,COUNT(*) FROM employees_clean GROUP BY 1 ORDER BY 1;
SELECT department,COUNT(*) FROM employees_clean GROUP BY department ORDER BY 2 DESC;
SELECT job_title,COUNT(*) FROM employees_clean GROUP BY job_title ORDER BY 2 DESC;
SELECT work_location,COUNT(*) FROM employees_clean GROUP BY work_location;
SELECT state,COUNT(*) FROM employees_clean GROUP BY state ORDER BY 2 DESC;
SELECT department,COUNT(*) FILTER(WHERE terminated) AS terminated,COUNT(*) AS total,ROUND(100.0*COUNT(*) FILTER(WHERE terminated)/NULLIF(COUNT(*),0),2) AS termination_pct FROM employees_clean GROUP BY department ORDER BY termination_pct DESC;
SELECT ROUND(AVG(tenure_years) FILTER(WHERE terminated),2) AS avg_terminated_tenure_years FROM employees_clean;
SELECT EXTRACT(YEAR FROM hire_date) AS year,COUNT(*) AS hires FROM employees_clean GROUP BY 1 ORDER BY 1;
SELECT department,gender,COUNT(*) FROM employees_clean GROUP BY department,gender ORDER BY department,gender;
SELECT department,ROUND(AVG(tenure_years),2) FROM employees_clean GROUP BY department ORDER BY 2 DESC;
