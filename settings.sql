-- settings.sql
CREATE DATABASE gameoverflow;
CREATE USER gameoverflowuser WITH PASSWORD 'gameoverflow';
GRANT ALL PRIVILEGES ON DATABASE gameoverflow TO gameoverflowuser;