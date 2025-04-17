import pyodbc
from entity.job_listing import JobListing
from exception.exception import DatabaseException
from exception.exception import NegativeSalaryException  # Import your custom exception
from util.db_connection import DBConnection

class JobListingDAO:
    def __init__(self):
        self.conn = DBConnection.get_connection()

    def add_job_listing(self, job_listing):
        try:
            if job_listing.Salary < 0:
                raise NegativeSalaryException()

            cursor = self.conn.cursor()
            query = """
                INSERT INTO Jobs (company_id, job_title, job_description, job_location, salary, job_type, posted_date)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(query, (
                job_listing.CompanyID,
                job_listing.JobTitle,
                job_listing.JobDescription,
                job_listing.JobLocation,
                job_listing.Salary,
                job_listing.JobType,
                job_listing.PostedDate
            ))
            self.conn.commit()
            print("✅ Job listing added successfully.")
        except NegativeSalaryException as e:
            print(f"❌ {e}")
        except pyodbc.Error as e:
            raise DatabaseException(f"❌ Error adding job listing: {e}")

    def get_all_job_listings(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Jobs")
            rows = cursor.fetchall()
            listings = [JobListing(
                job_id=row.job_id,
                company_id=row.company_id,
                job_title=row.job_title,
                job_description=row.job_description,
                job_location=row.job_location,
                salary=row.salary,
                job_type=row.job_type,
                posted_date=row.posted_date
            ) for row in rows]
            return listings
        except pyodbc.Error as e:
            raise DatabaseException(f"❌ Error fetching job listings: {e}")

    def get_job_listing_by_id(self, job_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM Jobs WHERE job_id = ?", (job_id,))
            row = cursor.fetchone()
            if row:
                return JobListing(
                    job_id=row.job_id,
                    company_id=row.company_id,
                    job_title=row.job_title,
                    job_description=row.job_description,
                    job_location=row.job_location,
                    salary=row.salary,
                    job_type=row.job_type,
                    posted_date=row.posted_date
                )
            else:
                print("⚠️ Job listing not found.")
                return None
        except pyodbc.Error as e:
            raise DatabaseException(f"❌ Error retrieving job listing: {e}")

    def update_job_listing(self, job_listing):
        try:
            if job_listing.Salary < 0:
                raise NegativeSalaryException()

            cursor = self.conn.cursor()
            query = """
                UPDATE Jobs
                SET company_id = ?, job_title = ?, job_description = ?, job_location = ?, 
                    salary = ?, job_type = ?, posted_date = ?
                WHERE job_id = ?
            """
            cursor.execute(query, (
                job_listing.CompanyID,
                job_listing.JobTitle,
                job_listing.JobDescription,
                job_listing.JobLocation,
                job_listing.Salary,
                job_listing.JobType,
                job_listing.PostedDate,
                job_listing.JobID
            ))
            self.conn.commit()
            print("✅ Job listing updated successfully.")
        except NegativeSalaryException as e:
            print(f"❌ {e}")
        except pyodbc.Error as e:
            raise DatabaseException(f"❌ Error updating job listing: {e}")

    def delete_job_listing(self, job_id):
        try:
            cursor = self.conn.cursor()

            # Check if the job ID exists
            cursor.execute("SELECT * FROM Jobs WHERE job_id = ?", (job_id,))
            row = cursor.fetchone()

            if row is None:
                print("❌ Job listing not found with the provided ID.")
                return

            # Delete the job
            cursor.execute("DELETE FROM Jobs WHERE job_id = ?", (job_id,))
            self.conn.commit()
            print("✅ Job listing deleted successfully.")
        except pyodbc.Error as e:
            raise DatabaseException(f"❌ Error deleting job listing: {e}")
