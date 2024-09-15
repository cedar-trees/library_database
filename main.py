import sqlite3
from book import Books
from member import Member
from borrow import Borrow

conn = sqlite3.connect('library.db')

c = conn.cursor()

##Creating the books table and inserting values into it

# c.execute(""" CREATE TABLE books (
#           book_id INT,
#           title TEXT,
#           author TEXT,
#           copies_available INT)""")

# c.execute("INSERT INTO books VALUES (00102, 'Six Crimson Cranes', 'Elizabeth Lim', 2)")

##using new books class to insert it easily into database

book_1 = Books(103, 'Astrid Parker Doesnt Fail', 'Ashley Herring Blake', 1)

#insert into table using the ? method w tuple

# c.execute("INSERT INTO books VALUES (?, ?, ?, ?)", (book_1.book_id, book_1.title, book_1.author, book_1.copies_available))

##insert into using the :words method w dictionary

book_2 = Books(104, 'The Secret Garden', 'Francis Hodgson Burnett', 2)
# c.execute("INSERT INTO books VALUES (:book_id, :title, :author, :copies_available)", 
#           {'book_id': book_2.book_id, 'title': book_2.title, 'author': book_2.author, 'copies_available': book_2.copies_available})


##fetch  a specific book using the tuple method

# c.execute("SELECT * FROM books WHERE book_id = ?", ('103',))
# print(c.fetchall())

##fetch a specific book using the dictionary method

# c.execute("SELECT * FROM books WHERE book_id = :book_id", {'book_id': 104})
# print(c.fetchall())

# c.execute("SELECT * FROM books")
# print(c.fetchall())

##Create the members table for people borrowing books

# c.execute(""" CREATE TABLE members (
#           member_id INT,
#           f_name TEXT,
#           l_name TEXT,
#           phone_num INT)""")

##Create our first two members

mem_1 = Member(201, 'Lex', 'Smith', 1234567890)
# c.execute("INSERT INTO members VALUES (:member_id, :f_name, :l_name, :phone_num)", {'member_id': mem_1.member_id, 'f_name': mem_1.f_name, 'l_name': mem_1.l_name, 'phone_num': mem_1.phone_num})

mem_2 = Member(202, 'Sam', 'Fourie', 9876543210)
# c.execute("INSERT INTO members VALUES (:member_id, :f_name, :l_name, :phone_num)", {'member_id': mem_2.member_id, 'f_name': mem_2.f_name, 'l_name': mem_2.l_name, 'phone_num': mem_2.phone_num})

# c.execute("SELECT * FROM members")
# print(c.fetchall())

##Create the borrowed books table

# c.execute(""" CREATE TABLE borrowed_books (
#           borrow_id INT,
#           book_id INT,
#           member_id INT,
#           borrow_date INT)""")

##Update the table parameters so that borrow_dates data type is DATE rather than INT

# c.execute("DROP table IF EXISTS borrowed_books")
# print('Table dropped')

##create new borrowed books table

# c.execute(""" CREATE TABLE borrowed_books (
#           borrow_id INT,
#           book_id INT,
#           member_id INT,
#           borrow_date DATE,
#           return_date DATE)""")

# b1 = Borrow(301, 104, 202, 20240904, 00000000)
# c.execute("INSERT INTO borrowed_books VALUES (:borrow_id, :book_id, :member_id, :borrow_date, :return_date)", {'borrow_id': b1.borrow_id, 'book_id': b1.book_id, 'member_id': b1.member_id, 'borrow_date': b1.borrow_date, 'return_date': b1.return_date})

##Retrieve borrowed books

# c.execute("SELECT * FROM borrowed_books")
# print(c.fetchall())

##Then use the member number to find the member who owes you the book

# c.execute("SELECT * FROM members WHERE member_id = 202")
# print(c.fetchall())

#########################################################

##Insert new books into the books table
##Since it's a long list of data, it's more efficient doing it the traditional way, the classes are better for a single entry

# c.execute(""" INSERT INTO books (book_id, title, author, copies_available)
#           VALUES('105', 'Before the Coffee Gets Cold', 'Toshikazu Kawaguchi', '1'),
#                 ('106', 'The Song of Achilles', 'Madeline Miller', '1'),
#                 ('107', 'Legends and Lattes', 'Travis Baldree', '1'),
#                 ('108', 'The Poppy War', 'R.F. Kuang', '1'),
#                 ('109', 'The Dragon Republic', 'R.F. Kuang', '1'),
#                 ('110', 'The Burning God', 'R.F. Kuang', '1'),
#                 ('111', 'Solitaire', 'Alice Oseman', '1'),
#                 ('112', 'Ariadne', 'Jennifer Saint', '1'),
#                 ('113', 'The Seven Husbands of Evelyn Hugo', 'Taylor Jenkins Reid', '1'),
#                 ('114', 'Lessons in Chemistry', 'Bonnie Garmus', '1'),
#                 ('115', 'Smothermoss', 'Alisa Alering', '1'),
#                 ('116', 'The Colour of Magic', 'Terry Pratchett', '1'),
#                 ('117', 'The Light Fantastic', 'Terry Pratchett', '1'),
#                 ('118', 'A Game of Thrones', 'George R.R. Martin', '1'),
#                 ('119', 'To Sleep in a Sea of Stars', 'Christopher Paolini', '1'),
#                 ('120', 'Ahsoka', 'E.k. Johnston', '1')""")

##Sam recently returned the book she borrowed, let's update the borrowed_books table to reflect that

# c.execute(""" UPDATE borrowed_books
#           SET return_date = 20240914 
#           WHERE borrow_id = 301""")

# c.execute("SELECT * FROM borrowed_books")
# print(c.fetchall())


# conn.commit()

conn.close()