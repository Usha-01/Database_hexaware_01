from dao.company_dao import CompanyDAO
from dao.applicant_dao import ApplicantDAO
from dao.job_listing_dao import JobListingDAO
from dao.job_application_dao import JobApplicationDAO
from entity.job_listing import JobListing
from entity.job_application import JobApplication
from entity.applicant import Applicant

def main():
    while True:
        print("\n=== CareerHub Job Portal ===")
        print("1. Company Management")
        print("2. Applicant Management")
        print("3. Job Listing Management")
        print("4. Job Application Management")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            company_menu()
        elif choice == '2':
            applicant_menu()
        elif choice == '3':
            job_listing_menu()
        elif choice == '4':
            job_application_menu()
        elif choice == '5':
            print("Thank you for using CareerHub. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def company_menu():
    dao = CompanyDAO()
    while True:
        print("\n--- Company Menu ---")
        print("1. Add Company")
        print("2. View All Companies")
        print("3. Update Company")
        print("4. Delete Company")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Company Name: ")
            location = input("Enter Location: ")

            if dao.create_company(name, location):
                print("Company added successfully.")
            else:
                print("Failed to add company.")

        elif choice == '2':
            companies = dao.get_all_companies()
            for c in companies:
                print(c)

        elif choice == '3':
            try:
                cid = int(input("Enter Company ID: "))
                company = dao.get_company_by_id(cid)
                if not company:
                    print("Company not found.")
                    continue
                name = input(f"Enter Company Name [{company.name}]: ") or company.name
                location = input(f"Enter Location [{company.location}]: ") or company.location

                if dao.update_company(cid, name, location):
                    print("Company updated.")
                else:
                    print("Update failed.")
            except ValueError:
                print("❌ Invalid input. Company ID must be a number.")

        elif choice == '4':
            try:
                cid = int(input("Enter Company ID to delete: "))
                if dao.delete_company(cid):
                    print("Company deleted.")
                else:
                    print("Failed to delete company.")
            except ValueError:
                print("❌ Invalid input. Company ID must be a number.")

        elif choice == '5':
            break

def applicant_menu():
    dao = ApplicantDAO()
    while True:
        print("\n--- Applicant Menu ---")
        print("1. Add Applicant")
        print("2. View All Applicants")
        print("3. View Applicant by ID")
        print("4. Update Applicant")
        print("5. Delete Applicant")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                applicant_id = int(input("Enter Applicant ID: "))
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                email = input("Enter Email: ")
                phone = input("Enter Phone: ")
                resume = input("Enter Resume File Path: ")
                applicant = Applicant(applicant_id, first_name, last_name, email, phone, resume)
                dao.create_applicant(applicant)
            except ValueError:
                print("❌ Invalid input. Applicant ID must be a number.")

        elif choice == '2':
            for a in dao.get_all_applicants():
                print(a)

        elif choice == '3':
            try:
                aid = int(input("Enter Applicant ID: "))
                applicant = dao.get_applicant_by_id(aid)
                print(applicant if applicant else "Applicant not found.")
            except ValueError:
                print("❌ Invalid input. Applicant ID must be a number.")

        elif choice == '4':
            try:
                aid = int(input("Enter Applicant ID: "))
                a = dao.get_applicant_by_id(aid)
                if not a:
                    print("Applicant not found.")
                    continue
                first_name = input(f"Enter First Name [{a.first_name}]: ") or a.first_name
                last_name = input(f"Enter Last Name [{a.last_name}]: ") or a.last_name
                email = input(f"Enter Email [{a.email}]: ") or a.email
                phone = input(f"Enter Phone [{a.phone}]: ") or a.phone
                resume = input(f"Enter Resume Path [{a.resume}]: ") or a.resume

                dao.update_applicant(aid, first_name, last_name, email, phone, resume)
            except ValueError:
                print("❌ Invalid input. Applicant ID must be a number.")

        elif choice == '5':
            try:
                aid = int(input("Enter Applicant ID: "))
                dao.delete_applicant(aid)
            except ValueError:
                print("❌ Invalid input. Applicant ID must be a number.")

        elif choice == '6':
            break

def job_listing_menu():
    dao = JobListingDAO()
    while True:
        print("\n--- Job Listings Menu ---")
        print("1. Add Job Listing")
        print("2. View All Job Listings")
        print("3. View Job by ID")
        print("4. Update Job Listing")
        print("5. Delete Job Listing")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                cid = int(input("Enter Company ID: "))
                title = input("Enter Job Title: ")
                desc = input("Enter Description: ")
                location = input("Enter Location: ")
                salary = float(input("Enter Salary: "))
                job_type = input("Enter Job Type (Full-time/Part-time): ")
                posted_date = input("Enter Posted Date (YYYY-MM-DD): ")

                job = JobListing(None, cid, title, desc, location, salary, job_type, posted_date)
                dao.add_job_listing(job)
                print("Job listing added.")
            except Exception as e:
                print(f"❌ {e}")

        elif choice == '2':
            try:
                for job in dao.get_all_job_listings():
                    print(job)
            except Exception as e:
                print(f"❌ {e}")

        elif choice == '3':
            try:
                jid = int(input("Enter Job ID: "))
                job = dao.get_job_listing_by_id(jid)
                print(job if job else "Job not found.")
            except Exception as e:
                print(f"❌ {e}")

        elif choice == '4':
            try:
                jid = int(input("Enter Job ID: "))
                job = dao.get_job_listing_by_id(jid)
                if not job:
                    print("⚠️ Job not found.")
                    continue

                title = input(f"Title [{job.JobTitle}]: ") or job.JobTitle
                desc = input(f"Description [{job.JobDescription}]: ") or job.JobDescription
                location = input(f"Location [{job.JobLocation}]: ") or job.JobLocation
                salary_in = input(f"Salary [{job.Salary}]: ")
                salary = float(salary_in) if salary_in else job.Salary
                job_type = input(f"Type [{job.JobType}]: ") or job.JobType
                posted_date = input(f"Posted Date [{job.PostedDate}]: ") or job.PostedDate

                updated_job = JobListing(jid, job.CompanyID, title, desc, location, salary, job_type, posted_date)
                dao.update_job_listing(updated_job)
                print("Job listing updated.")
            except Exception as e:
                print(f"❌ {e}")

        elif choice == '5':
            try:
                jid = int(input("Enter Job ID: "))
                dao.delete_job_listing(jid)
                print("Job listing deleted.")
            except Exception as e:
                print(f"❌ {e}")

        elif choice == '6':
            break

def job_application_menu():
    dao = JobApplicationDAO()
    while True:
        print("\n--- Job Applications Menu ---")
        print("1. Apply for Job")
        print("2. View All Applications")
        print("3. View Application by ID")
        print("4. Update Cover Letter")
        print("5. Delete Application")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                jid = int(input("Enter Job ID: "))
                aid = int(input("Enter Applicant ID: "))
                application_date = input("Enter Application Date (YYYY-MM-DD): ")
                cover_letter = input("Enter Cover Letter (optional): ") or None
                application = JobApplication(None, jid, aid, application_date, cover_letter)
                dao.create_application(application)
                print("Application submitted.")
            except Exception as e:
                print(f"❌ Error creating job application: {e}")

        elif choice == '2':
            try:
                for app in dao.get_all_applications():
                    print(app)
            except Exception as e:
                print(f"❌ {e}")

        elif choice == '3':
            try:
                app_id = int(input("Enter Application ID: "))
                application = dao.get_application_by_id(app_id)
                print(application if application else "Application not found.")
            except ValueError:
                print("❌ Invalid input. Application ID must be a number.")

        elif choice == '4':
            try:
                app_id = int(input("Enter Application ID: "))
                new_letter = input("Enter New Cover Letter: ")
                dao.update_application_status(app_id, new_letter)
                print("Cover letter updated.")
            except ValueError:
                print("❌ Invalid input. Application ID must be a number.")

        elif choice == '5':
            try:
                app_id = int(input("Enter Application ID: "))
                dao.delete_application(app_id)
                print("Application deleted.")
            except ValueError:
                print("❌ Invalid input. Application ID must be a number.")

        elif choice == '6':
            break

if __name__ == "__main__":
    main()
