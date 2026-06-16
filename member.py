class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def update_email(self, email):
        self.email = email

    def matches_id(self, member_id):
        if str(self.member_id) == str(member_id):
            return True
        return False

    def to_csv_row(self):
        row = []
        row.append(self.member_id)
        row.append(self.name)
        row.append(self.email)
        return row

    def __str__(self):
        return "Member ID: " + str(self.member_id) + " | Name: " + self.name + " | Email: " + self.email