# Day 12

## What did I build?

Today I built my first SQLite database for the CommerceOps AI project. I created a database file, designed an inventory table with appropriate columns, inserted product data, and queried the database using basic SQL statements. I also organized my SQL learning into a dedicated experiments/sql folder with its own database directory.

## What did I learn?

Today I learned the fundamental concepts of relational databases, including databases, tables, rows, columns, and primary keys. I learned how SQLite stores data in a .db file, how to create tables using SQL, how to insert records using INSERT INTO, and how to retrieve data using SELECT. I also learned that SELECT * returns all columns, while specifying column names returns only the requested data.

## Biggest challenge today

The biggest challenge was understanding how SQLite databases are stored and why I couldn't simply open the .db file like a normal text file. I also encountered an issue with relative file paths when creating the database, which helped me understand how Python resolves paths based on the current working directory.

## How did I solve it?

I corrected the database path by running the script from the project root and keeping my database inside the experiments/sql/databases folder. After learning that SQLite databases are binary files, I queried the database using SQL instead of trying to open the file directly. This allowed me to view the stored records through Python.

## What surprised me?

I was surprised by how similar SQL feels to plain English. Statements like CREATE TABLE, INSERT INTO, and SELECT ... FROM were much easier to understand than I expected. It was also satisfying to see data that I inserted myself being returned from the database through a SQL query.

## One thing I still don't understand

I'm curious to learn how databases handle much larger amounts of data efficiently and how SQL can filter, sort, and aggregate records without scanning everything manually. I'm also looking forward to connecting my SQLite database to CommerceOps AI so it can answer questions using real data instead of Python dictionaries.