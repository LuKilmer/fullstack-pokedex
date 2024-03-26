sudo -iu postgres psql
\c flask_db
SELECT title, author FROM books;
