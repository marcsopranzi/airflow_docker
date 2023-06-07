#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --dbname template1 --username postgres <<-EOSQL
\c ecology;

CREATE TABLE IF NOT EXISTS public.water_consumption (
measure_year int,
ny_population int,
ny_day_consumption decimal(10,2),
person_day_consumption varchar(50),
created_at TIMESTAMP DEFAULT now()
);
EOSQL
