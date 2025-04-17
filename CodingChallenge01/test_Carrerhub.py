import pytest
from datetime import datetime

class Company:
    def __init__(self, company_id, company_name, location):
        self.company_id = company_id
        self.company_name = company_name
        self.location = location

class Job:
    def __init__(self, job_id, company_id, job_title, job_description, job_location, salary, job_type, posted_date):
        self.job_id = job_id
        self.company_id = company_id
        self.job_title = job_title
        self.job_description = job_description
        self.job_location = job_location
        self.salary = salary
        self.job_type = job_type
        self.posted_date = posted_date

# ---------- Mock DAO Classes ----------

class MockCompanyDAO:
    def __init__(self):
        self.companies = {
            1: Company(company_id=1, company_name="TechCorp", location="New York"),
            2: Company(company_id=2, company_name="Innovatech", location="San Francisco"),
            3: Company(company_id=3, company_name="Green Solutions", location="Chicago"),
        }

    def get_company_by_id(self, company_id):
        return self.companies.get(company_id)

class MockJobDAO:
    def __init__(self):
        self.jobs = {
            1: Job(job_id=1, company_id=1, job_title="Software Engineer", job_description="Develop web apps", job_location="Remote", salary=85000.00, job_type="Full-time", posted_date="2025-04-10"),
            2: Job(job_id=2, company_id=2, job_title="Data Analyst", job_description="Analyze datasets", job_location="San Francisco", salary=70000.00, job_type="Part-time", posted_date="2025-04-12"),
            3: Job(job_id=3, company_id=3, job_title="DevOps Engineer", job_description="Manage CI/CD", job_location="Chicago", salary=90000.00, job_type="Contract", posted_date="2025-04-15"),
        }

    def get_job_by_id(self, job_id):
        return self.jobs.get(job_id)

# ---------- Test Cases ----------

def test_company_exists_by_id():
    dao = MockCompanyDAO()
    company = dao.get_company_by_id(2)
    assert company is not None
    assert company.company_name == "Innovatech"
    assert company.location == "San Francisco"

def test_job_exists_by_id():
    dao = MockJobDAO()
    job = dao.get_job_by_id(3)
    assert job is not None
    assert job.job_title == "DevOps Engineer"
    assert job.salary == 90000.00
    assert job.job_type == "Contract"

def test_company_not_found_returns_none():
    dao = MockCompanyDAO()
    company = dao.get_company_by_id(100)  # Non-existent ID
    assert company is None

def test_job_not_found_returns_none():
    dao = MockJobDAO()
    job = dao.get_job_by_id(101)  # Non-existent ID
    assert job is None
