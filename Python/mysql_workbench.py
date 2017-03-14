MySQL Commands:

-- Examples of queries.
USE books; -- to set the database you want to use.  Replace with any database name

SELECT * FROM books; -- or any table in the books database
INSERT INTO books (title, author, created_at, updated_at) VALUES ('Algorithm Challenges', 'Martin Puryear', NOW(), NOW());
DELETE FROM books WHERE id = 35;
UPDATE books SET author = 'Dan Brown' WHERE id = 34;

show databases;  -- show 'actual name of database';--

use database;  -- use 'actual name of database';--

  Inserting Records:

INSERT INTO table_name (column_name1, column_name 2)
VALUES('column1_value', 'column2_value');

  Updating Records:

UPDATE table_name
SET column_name1 = 'some_value', column_name2 = 'another_value'
WHERE condition(s)
** if WHERE condition is not added to the UPDATE statement, the changes will be applied to every record in the table.

  Deleting Records:
DELETE FROM table_name
WHERE conditions(s)
** if WHERE condition is not added to the DELETE statement, it will delete all the records on the table.

  CONCAT
  ex
SELECT CONCAT('Mr.', ' ', first_name, ' ', last_name) AS full_name, AS e FROM  clients;

  CONCAT_WS()
  EX
SELECT CONCAT_WS(' ', first_name, last_name, 'cool') AS full_name FROM clients;

  LENGTH
  ex
SELECT LENGTH(last_name) AS last_len FROM clients;

  LOWER()
  ex
SELECT LOWER(first_name) AS first_lowercase FROM clients;

  HOUR()
  ex
SELECT HOUR(joined_datetime) AS date_hour FROM clients;
  DAYNAME()
  ex
SELECT DAYNAME(joined_datetime) AS date_hour, joined_datetime FROM clients;

  MONTH()
  ex
SELECT MONTH(joined_datetime) AS month_number, joined_datetime FROM clients;

  NOW()
  ex
SELECT NOW() AS right_now;

  DATE_FORMAT()
  ex
SELECT DATE_FORMAT(joined_datetime, %W,%M,%e,%Y) FROM clients;

Format	Description
%a	Abbreviated weekday name (Sun-Sat)
%b	Abbreviated month name (Jan-Dec)
%c	Month, numeric (0-12)
%D	Day of month with English suffix (0th, 1st, 2nd, 3rd, �)
%d	Day of month, numeric (00-31)
%e	Day of month, numeric (0-31)
%f	Microseconds (000000-999999)
%H	Hour (00-23)
%h	Hour (01-12)
%I	Hour (01-12)
%i	Minutes, numeric (00-59)
%j	Day of year (001-366)
%k	Hour (0-23)
%l	Hour (1-12)
%M	Month name (January-December)
%m	Month, numeric (00-12)
%p	AM or PM
%r	Time, 12-hour (hh:mm:ss followed by AM or PM)
%S	Seconds (00-59)
%s	Seconds (00-59)
%T	Time, 24-hour (hh:mm:ss)
%U	Week (00-53) where Sunday is the first day of week
%u	Week (00-53) where Monday is the first day of week
%V	Week (01-53) where Sunday is the first day of week, used with %X
%v	Week (01-53) where Monday is the first day of week, used with %x
%W	Weekday name (Sunday-Saturday)
%w	Day of the week (0=Sunday, 6=Saturday)
%X	Year for the week where Sunday is the first day of week, four digits, used with %V
%x	Year for the week where Monday is the first day of week, four digits, used with %v
%Y	Year, numeric, four digits
%y	Year, numeric, two digits

Example
The following script uses the DATE_FORMAT() function to display different formats. We will use the NOW() function to get the current date/time:

DATE_FORMAT(NOW(),'%b %d %Y %h:%i %p')
DATE_FORMAT(NOW(),'%m-%d-%Y')
DATE_FORMAT(NOW(),'%d %b %y')
DATE_FORMAT(NOW(),'%d %b %Y %T:%f')
The result would look something like this:

Nov 04 2014 11:45 PM
11-04-2014
04 Nov 14
04 Nov 2014 11:45:34:243
