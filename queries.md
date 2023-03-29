Make sure you download the starter code and run the following:

```sh
  psql < movies.sql
  psql movies_db
```

In markdown, you can place a code block inside of three backticks (```) followed by the syntax highlighting you want, for example

\```sql

SELECT \* FROM users;

\```

Using the `movies_db` database, write the correct SQL queries for each of these tasks:

The title of every movie.


```SELECT title FROM movies;```

All information on the G-rated movies.
```SELECT * FROM movies WHERE rating = 'G';```

 The title and release year of every movie, ordered with the
    oldest movie first.
```SELECT title, release_year FROM movies ORDER BY release_year;```

    
 All information on the 5 longest movies.
```SELECT * FROM movies ORDER BY duration DESC LIMIT 5;```


  A query that returns the columns of `rating` and `total`, tabulating the
    total number of G, PG, PG-13, and R-rated movies.
    
    SELECT rating, COUNT(*) AS total FROM movies GROUP BY rating;

 A table with columns of `release_year` and `average_runtime`,
    tabulating the average runtime by year for every movie in the database. The data should be in reverse chronological order (i.e. the most recent year should be first).
    ```SELECT release_year, AVG(runtime) AS average_runtime
FROM movies
GROUP BY release_year
ORDER BY release_year DESC;```


 The movie title and studio name for every movie in the
    database.
```SELECT movies.title, studios.name AS studio_name
FROM movies
JOIN studios ON movies.studio_id = studios.id;```
 The star first name, star last name, and movie title for every
    matching movie and star pair in the database.
```SELECT stars.first_name, stars.last_name, movies.title
FROM stars
JOIN stars_in_movies ON stars.id = stars_in_movies.star_id
JOIN movies ON stars_in_movies.movie_id = movies.id;```

 The first and last names of every star who has been in a G-rated movie. The first and last name should appear only once for each star, even if they are in several G-rated movies. *IMPORTANT NOTE*: it's possible that there can be two *different* actors with the same name, so make sure your solution accounts for that.
 ```SELECT DISTINCT ON (stars.first_name, stars.last_name) stars.first_name, stars.last_name
FROM stars
JOIN stars_in_movies ON stars.id = stars_in_movies.star_id
JOIN movies ON stars_in_movies.movie_id = movies.id
WHERE movies.rating = 'G'
ORDER BY stars.first_name, stars.last_name;```

The first and last names of every star along with the number
    of movies they have been in, in descending order by the number of movies. (Similar to #9, make sure
    that two different actors with the same name are considered separately).
    ```SELECT stars.first_name, stars.last_name, COUNT(*) AS movie_count
FROM stars
JOIN stars_in_movies ON stars.id = stars_in_movies.star_id
GROUP BY stars.first_name, stars.last_name
ORDER BY movie_count DESC;```

### The rest of these are bonuses

11. The title of every movie along with the number of stars in
    that movie, in descending order by the number of stars.

12. The first name, last name, and average runtime of the five
    stars whose movies have the longest average.

13. The first name, last name, and average runtime of the five
    stars whose movies have the longest average, among stars who have more than one movie in the database.

14. The titles of all movies that don't feature any stars in our
    database.

15. The first and last names of all stars that don't appear in any movies in our database.

16. The first names, last names, and titles corresponding to every
    role in the database, along with every movie title that doesn't have a star, and the first and last names of every star not in a movie.
