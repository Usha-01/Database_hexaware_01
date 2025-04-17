class JobApplication:
    def __init__(self, application_id, job_id, applicant_id, application_date, cover_letter):
        self.application_id = application_id
        self.job_id = job_id
        self.applicant_id = applicant_id
        self.application_date = application_date
        self.cover_letter = cover_letter

    def __str__(self):
        return f"Application ID: {self.application_id}, Job ID: {self.job_id}, Applicant ID: {self.applicant_id}, " \
               f"Date: {self.application_date}, Cover Letter: {self.cover_letter}"

    def __repr__(self):
        return self.__str__()
