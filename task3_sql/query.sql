.mode csv


WITH job_lower AS (
    SELECT id, url, LOWER(location) AS location
    FROM Job
)
SELECT
    jl.url,
    jt.description
FROM
    job_lower jl
    JOIN Job_text jt ON jl.id = jt.id_job
WHERE
    jl.location LIKE '%kyiv%'
    OR jl.location LIKE '%kiev%'
    OR jl.location LIKE '%lviv%'
    OR jl.location LIKE '%lvov%';
