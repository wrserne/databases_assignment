### Conceptual Exercise

Answer the following questions below:

**- What is PostgreSQL?**
	-PostgreSQL is an open source data management system with multiversion concurrency control, a flexible data model that supports structured, semi-structured, and unstructured data types, advanced indexing and query optimization capabilities, and a powerful set of built-in functions for data manipulation and analysis.

**- What is the difference between SQL and PostgreSQL?**
	-SQL and PostgreSQL are related but different concepts. SQL (Structured Query Language) is a standard language used for managing and manipulating relational databases, while PostgreSQL is a specific database management system (DBMS) that supports the SQL language along with many other features.

**- In `psql`, how do you connect to a database?**
	-To connect to a PostgreSQL database using the psql command-line interface, you can follow these steps:

Open a terminal or command prompt.

Type the following command, replacing "username" with your PostgreSQL username and "database_name" with the name of the database you want to connect to:


**psql -U username -d database_name**

For example, if your username is "postgres" and you want to connect to a database called "mydatabase", you would enter:


**psql -U postgres -d mydatabase**

If the database is located on a remote server, you may also need to specify the host and port using the -h and -p options. For example:
css

**psql -U username -d database_name -h hostname -p port_number**

If you need to specify a password to connect to the database, you can use the -W option. This will prompt you to enter your password after you run the psql command. For example:
 
**psql -U username -d database_name -W**

Once you've connected to the database, you should see a prompt that looks like this:

**mydatabase=#**

This indicates that you are now connected to the "mydatabase" database and can start executing SQL commands.

**What is the difference between `HAVING` and `WHERE`?**
	
-HAVING and WHERE are two different clauses in SQL that are used to filter rows from a result set. However, they are used in different contexts and have different functionality.

The main difference between HAVING and WHERE is that WHERE is used to filter rows before they are grouped, while HAVING is used to filter groups after they have been formed. In other words, WHERE is used with non-aggregate functions and HAVING is used with aggregate functions.

**- What is the difference between an `INNER` and `OUTER` join?**
INNER join only returns the rows that have matching values in both tables, while OUTER join returns all the rows from one table and matching rows from the other table. INNER join is used to retrieve data from two or more tables where the join condition must be satisfied by both tables, while OUTER join is used to retrieve data from two or more tables where the join condition is only required to be satisfied by one table.

**- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?**
The difference between a LEFT OUTER and RIGHT OUTER join lies in which table's all rows are returned. In a LEFT OUTER join, all rows from the left table and matching rows from the right table are returned. In a RIGHT OUTER join, all rows from the right table and matching rows from the left table are returned.

**- What is an ORM? What do they do?**
An ORM is a programming technique that allows developers to interact with a database using an object-oriented paradigm, by providing an abstraction layer between the application code and the database. ORMs help to increase productivity, reduce development costs, prevent errors, and provide easier interaction with the database. Examples of popular ORMs include Django ORM, SQLAlchemy, Hibernate, and Entity Framework.

**- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?**
  The main difference between making HTTP requests using AJAX and from the server-side using a library like requests is that AJAX requests are made asynchronously from the client-side using JavaScript, while requests requests are made synchronously from the server-side using a Python library.

AJAX requests are generally used to update a portion of a web page without reloading the entire page, while requests requests are typically used to retrieve data or perform actions on the server-side. AJAX requests can be faster and more responsive, but they require more client-side processing and can be limited by cross-origin restrictions, while requests requests require less client-side processing but are subject to server-side limitations such as rate limiting or network latency.

**- What is CSRF? What is the purpose of the CSRF token?**
CSRF stands for Cross-Site Request Forgery. It is a type of attack where a malicious actor tricks a user into unknowingly performing an action on a website that they did not intend to perform.

The purpose of a CSRF token is to prevent such attacks. It is a unique token that is generated by the server and embedded in the web page. When the user submits a form or makes a request, the token is included in the request, and the server verifies that the token matches the one that was issued for that user and request. If the tokens do not match, the server will reject the request, preventing the attack.

In summary, a CSRF token is a security measure that helps to protect against Cross-Site Request Forgery attacks by verifying that the user's request originates from the expected source.

**- What is the purpose of `form.hidden_tag()`?**
form.hidden_tag() is a method in the Flask web framework's WTForms module that generates a hidden input field in an HTML form. The purpose of this method is to add an additional layer of security to the form submission process by including a token that helps to prevent CSRF attacks.

The hidden_tag() method generates an input field with a randomly generated token that is unique to the form and user. This token is used to validate that the form submission was made by the user who originally requested the form and not by a malicious third party. The token is also used to ensure that the form submission is not a duplicate or replay attack.

In summary, the form.hidden_tag() method generates a hidden input field with a unique token that helps to prevent CSRF attacks and ensure the integrity of form submissions.
