class Company:
    def __init__(self, company_id, name, location):
        self.company_id = company_id
        self.name = name
        self.location = location

    def __str__(self):
        return f"ID: {self.company_id}, Name: {self.name}, Location: {self.location}"
