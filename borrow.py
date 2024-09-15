class Borrow:
    #Create new borrow books entry

    def __init__(self, borrow_id, book_id, member_id, borrow_date, return_date):
        self.borrow_id = borrow_id
        self.book_id = book_id
        self.member_id = member_id
        self.borrow_date = borrow_date
        self.return_date = return_date

    def __repr__(self):
        return "Borrow('{}', '{}', '{}', '{}')".format(self.borrow_id, self.book_id, self.member_id, self.borrow_date, self.return_date)