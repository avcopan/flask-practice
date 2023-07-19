CREATE DATABASE testdb;

\c testdb;

CREATE TABLE test1 (
  id SERIAL PRIMARY KEY,
  name TEXT
);

INSERT INTO test1(name) VALUES ('this'), ('that'), ('the other');