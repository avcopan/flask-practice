-- Following Rithm school tutorial
-- DDL: Data Definition Language (creating/modifying/deleting tables, columns, and databases)
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT
);

CREATE TABLE college_students (
  id SERIAL PRIMARY KEY,
  last_name VARCHAR(50),
  first_name VARCHAR(50),
  major VARCHAR(50) NOT NULL
);

CREATE TABLE phonebook (
  id SERIAL PRIMARY KEY,
  last_name VARCHAR(50),
  first_name VARCHAR(50),
  pohe_number VARCHAR(7) UNIQUE
);

CREATE TABLE products (
  product_no SERIAL PRIMARY KEY,
  name TEXT,
  price NUMERIC CHECK (price > 0)
);

ALTER TABLE users ADD COLUMN favorite_number INTEGER;
ALTER TABLE users DROP COLUMN favorite_number;
ALTER TABLE users ADD COLUMN jobb TEXT;
ALTER TABLE users RENAME COLUMN jobb TO job;
ALTER TABLE users ALTER COLUMN job SET DATA TYPE VARCHAR(100);
ALTER TABLE users ALTER COLUMN job SET NOT NULL;
ALTER TABLE users DROP COLUMN job;

-- DML: Data Manipulation Language (creating/modifying/deleting *rows*)
-- create
INSERT INTO users(first_name, last_name) VALUES ('Eli', 'Schoppik'), ('Joe', 'Lundman');

-- update
UPDATE users SET first_name = 'Elie'; -- updates all users, giving them the same first name
UPDATE users SET first_name = 'Joe' WHERE id = 2;

-- delete
DELETE FROM users; -- deletes all rows
DELETE FROM users WHERE id = 2; -- deletes only one row

-- OPERATORS AND AGGREGATES
-- if needed, cast data types using CAST or ::data_type at the end of the expression
-- with GROUP BY, we don't do "WHERE", we do "HAVING"

-- NORMALIZATION (helpful!)
-- 1NF (First Normal Form): a column cannot hold multiple values, only atomic
-- 2NF (Second Normal Form): two conditions:
--    1. The table is in 1NF
--    2. "Every non-prime attribute is dependent on the *whole* of every
--    candidate key."
--    Translation: If a table has a compound "candiate key" (under consideration
--    to be the table's key), none of the other columns should be tied to only
--    part of the key. (If they are, we need to separate off a table with
--    attributes tied only to that part of the key)
--  Example: A table with books in diferent formats. Here the compound key might
--  be {Title, Author, Format}. Some attributes, such as genre and publisher, will
--  be common across all formats and so are only actually tied to the {Title,
--  Author} key subset, whereas others, such as the price, depend on the full
--  compound key. In this case, we should separate the two tables, having one
--  table with {Title, Author} as the key and containing information specific to
--  it, and another table specific to the format where the price is listed.
-- 3NF (Third Normal Form): two conditions:
--    1. The table is in 2NF
--    2. "Every non-key attribute must provide a fact about the key, the whole
--    key, and nothing but the key"
--  Example: A table of tournament winners:
--    | Tournament | Year | Winner | Winner's date of birth |
--  The date of birth refers not to the primary key {Tournament, Year} but to a
--  non-key attribute, the Winner. This should be separated into two tables:
--    | Tournament | Year | Winner |    +    | Winner | Winner's date of birth |
--  We can see that this removes redundancies when we consider the possibility
--  of the same winner in different tournaments and years. In our initial
--  database, we would have had her date of birth appear multiple times, whereas
--  in the 3NF database, her date of birth is listed only once in the Winners
--  table.

