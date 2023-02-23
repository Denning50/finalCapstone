# finalCapstone
Ebookstore Management System

Contents: 
1. Brief description and overview of functions
2. installation and how to run
3. Database structure
4. Detail about the functions
5. Credits

This is a command-line program that allows users to manage a bookstore's inventory using a SQLite database. The program offers the following features:

1. Add a new book
2. Update book information
3. Delete a book
4. Search for a book
5. Exit

Installation and Usage
Clone the repository or download the code as a ZIP file.
Ensure that you have Python 3.x and SQLite3 installed on your machine.
Open a terminal or command prompt and navigate to the directory where the code is located.
Run the following command to start the program:
python ebookstore.py
Follow the prompts to add, update, delete or search for a book in the database.

The program uses a SQLite database called ebookstore.db. The database has one table called books with the following columns:

id (INTEGER, PRIMARY KEY): unique identifier for each book
title (TEXT): title of the book
author (TEXT): author of the book
qty (INTEGER): quantity of the book in stock
Code Overview
The program starts by importing the required libraries and connecting to the ebookstore.db database. A cursor object is created to execute SQL commands.

The books table is created if it does not already exist using the CREATE TABLE IF NOT EXISTS SQL command.

The program then defines four functions:

![Adding a book](https://user-images.githubusercontent.com/51790499/220880764-29d474b7-4322-4aa3-9a74-394155181511.jpg)
add_book(): This function allows the user to add a new book to the database by prompting them to enter the book's ID, title, author and quantity. The function then executes an SQL INSERT INTO command to add the book to the database.

![Updating book information](https://user-images.githubusercontent.com/51790499/220880821-114ced40-8808-41e5-887c-d6d2efda19ac.jpg)
update_book(): This function allows the user to update the information for an existing book in the database by prompting them to enter the book's ID and the new values for any of the book's attributes. The function then executes an SQL UPDATE command to update the book's information in the database.

![Deleting a book](https://user-images.githubusercontent.com/51790499/220880872-055b073a-c067-49e0-bcbd-1993155ada00.jpg)
delete_book(): This function allows the user to delete an existing book from the database by prompting them to enter the book's ID. The function then executes an SQL DELETE FROM command to remove the book from the database.

![Search and exit](https://user-images.githubusercontent.com/51790499/220880968-a43c3582-6823-499c-a37c-ece8cddf6f4d.jpg)
search_book(): This function allows the user to search for a book in the database by keyword. The function prompts the user to enter a keyword and then executes an SQL SELECT command to search for the keyword in the book's title or author.

Finally, the program enters a main loop where it displays the menu options to the user and prompts them to enter a choice. Based on the user's choice, the program calls the appropriate function. If the user enters 0, the program exits the loop and closes the database connection.

Credits:
Developed by Josh Denning
