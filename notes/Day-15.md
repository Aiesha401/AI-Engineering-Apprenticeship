# Day 15

## What did I build?

Today I connected Python to my SQLite database using parameterized SQL queries. I created reusable Python functions to retrieve product quantities and prices, learned how to fetch individual records efficiently, and explored the database schema using SQLite's built-in metadata tables.

## What did I learn?

I learned how to execute parameterized SQL queries using placeholders (?) and why they are safer than string formatting. I learned the difference between fetchone() and fetchall(), how to inspect database tables with sqlite_master, how to inspect columns with PRAGMA table_info, and how to wrap SQL queries inside reusable Python functions.

## Biggest challenge today

The biggest challenge was understanding how to write reusable database functions instead of executing standalone SQL queries. I also learned how SQLite represents returned data as tuples and how to extract the values I actually need.

## How did I solve it?

I solved this by creating helper functions like get_quantity() and get_price(), using fetchone() to retrieve a single row, and returning only the required value instead of the entire tuple. I also explored the database schema so I don't have to rely on memory to know what tables and columns exist.

## What surprised me?

I was surprised by how little code is needed to build useful database helper functions. I also found it interesting that SQLite stores the original CREATE TABLE statement and exposes metadata through sqlite_master and PRAGMA, making it easy to inspect the database structure.

## One thing I still don't understand

I'd like to learn how larger applications organize database code when there are many tables and many different queries. I'm also looking forward to seeing how these helper functions are integrated into my CommerceOps AI so the AI can query the database directly.