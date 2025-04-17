class Applicant:
    def __init__(self, applicant_id, first_name, last_name, email, phone, resume):
        self.applicant_id = applicant_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.resume = resume

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return (f"ID: {self.applicant_id}, Name: {self.full_name}, Email: {self.email}, "
                f"Phone: {self.phone}, Resume: {self.resume}")
