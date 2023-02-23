# Import libraries
import sqlite3

# Connect to the database
conn = sqlite3.connect('ebookstore.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# Create the books table if it doesn't already exist
c.execute('''CREATE TABLE IF NOT EXISTS books
             (id INTEGER PRIMARY KEY,
              title TEXT,
              author TEXT,
              qty INTEGER)''')

# Function to add a new book to the database
def add_book():
    id = input("Enter the bok id: ")
    title = input("Enter the title: ")
    author = input("Enter the author: ")
    qty = int(input("Enter the quantity: "))
    c.execute("INSERT INTO books (id, title, author, qty) VALUES (?, ?, ?, ?)", (id, title, author, qty))
    conn.commit()
    print("Book added successfully.")

# Function to update book information
def update_book():
    id = int(input("Enter the book ID: "))
    id_new = input("Enter the new id (Leave blank to keep the same): ")
    title = input("Enter the new title (leave blank to keep the same): ")
    author = input("Enter the new author (leave blank to keep the same): ")
    qty = input("Enter the new quantity (leave blank to keep the same): ")
    fields = []
    values = []
    if id_new:
        fields.append("id = ?")
        values.append(id_new)
    if title:
        fields.append("title = ?")
        values.append(title)
    if author:
        fields.append("author = ?")
        values.append(author)
    if qty:
        fields.append("qty = ?")
        values.append(int(qty))
    if not fields:
        print("No changes were made.")
        return
    query = "UPDATE books SET " + ", ".join(fields) + " WHERE id = ?"
    values.append(id)
    c.execute(query, tuple(values))
    conn.commit()
    print("Book updated successfully.")

# Function to delete a book from the database
def delete_book():
    id = int(input("Enter the book ID: "))
    c.execute("DELETE FROM books WHERE id = ?", (id,))
    conn.commit()
    print("Book deleted successfully.")

# Function to search for a book
def search_book():
    keyword = input("Enter a keyword to search for: ")
    c.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", ('%'+keyword+'%', '%'+keyword+'%'))
    results = c.fetchall()
    if not results:
        print("No books found.")
    else:
        for row in results:
            print(row)

# Main loop for the program
while True:
    # Display menu options to the user
    print("\nBOOKSTORE MANAGEMENT SYSTEM")
    print("1. Add a new book")
    print("2. Update book information")
    print("3. Delete a book")
    print("4. Search for a book")
    print("0. Exit")
    choice = input("Enter your choice: ")
    # Call the appropriate function based on user input
    if choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        delete_book()
    elif choice == '4':
        search_book()
    elif choice == '0':
        print("System exited, have a nice day!")
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()
