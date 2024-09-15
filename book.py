class Books:
    #Create new book entry

    def __init__(self, book_id, title, author, copies_available):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies_available = copies_available

    def __repr__(self):
        return "Books('{}', '{}', '{}', '{}')".format(self.book_id, self.title, self.author, self.copies_available)
        