class Member:
    #Create new library member

    def __init__(self, member_id, f_name, l_name, phone_num):
        self.member_id = member_id
        self.f_name = f_name
        self.l_name = l_name
        self.phone_num = phone_num

    def __repr__(self):
        return "Member('{}', '{}', '{}', '{}')".format(self.member_id, self.f_name, self.l_name, self.phone_num)
        