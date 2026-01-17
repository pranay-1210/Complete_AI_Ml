# SQL Basics – Part 1

This contains my learning and practice work for **SQL fundamentals (Part 1)**.  
I studied core database concepts and implemented them practically using **MySQL**.

## Topics Covered

### Database Fundamentals
- What is a Database?
- Difference between SQL and NoSQL
- What is SQL?
- What is a Table?

### DBMS
- Introduction to DBMS
- DBMS Installation

### MySQL Setup
- MySQL Installation
- Creating the First Database
- Creating the First Table

### SQL Operations
- Database Queries
- CRUD Operations on Tables  
  - Create  
  - Read  
  - Update  
  - Delete  

### Constraints & Keys
- What are Constraints?
- Key Constraints (Primary Key, Foreign Key, etc.)

## Tools Used
- MySQL
- SQL Queries
- Command Line / SQL Editor

## Learning Outcome
By completing this part, I gained a clear understanding of:
- How databases work internally
- How to design tables properly
- How to perform CRUD operations
- How constraints and keys maintain data integrity


## Day-02

## SELECT Command

Used to retrieve data from one or more tables.

Learned how to select specific columns as well as all columns using *.

## WHERE Clause

Used to filter records based on specific conditions.

Helps in fetching only the required data.

## Operators in WHERE Clause

Learned comparison operators such as =, !=, >, <, >=, <=.

Logical operators like AND, OR, and NOT.

## Frequently Used Operators

IN, BETWEEN, LIKE, IS NULL.

Used for advanced filtering and pattern matching.

## LIMIT Clause

Used to restrict the number of records returned in the result set.

Helpful for pagination and testing queries.

## ORDER BY Clause

Used to sort records in ascending or descending order.

Sorting can be done on one or multiple columns.

## Aggregate Functions

Functions like COUNT(), SUM(), AVG(), MIN(), and MAX().

Used to perform calculations on groups of data.

## GROUP BY Clause

Used to group rows that have the same values.

Mostly used along with aggregate functions.

## HAVING Clause

Used to filter grouped data.

Works like WHERE but for aggregate results.

## General Order of SQL Query

Understood the execution order:
SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT

## DELETE Table

Used to remove specific records from a table using conditions.

## ALTER Table

Used to modify table structure.

Adding, deleting, or updating columns.

## TRUNCATE Table

Used to delete all records from a table at once.

Faster than DELETE and resets table data completely.

## Summary

These topics together build a strong foundation in SQL for working with databases, writing efficient queries, and managing table data effectively. This knowledge will be useful for backend development, data analysis, and real-world database operations.


