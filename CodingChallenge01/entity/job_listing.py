class JobListing:
    def __init__(self, job_id, company_id, job_title, job_description,
                 job_location, salary, job_type, posted_date):
        self.JobID = job_id
        self.CompanyID = company_id
        self.JobTitle = job_title
        self.JobDescription = job_description
        self.JobLocation = job_location
        self.Salary = salary
        self.JobType = job_type
        self.PostedDate = posted_date

    def __str__(self):
        return (f"JobID: {self.JobID}, Title: {self.JobTitle}, Description: {self.JobDescription}, "
                f"CompanyID: {self.CompanyID}, Salary: {self.Salary}, Location: {self.JobLocation}, "
                f"Type: {self.JobType}, PostedDate: {self.PostedDate}")
