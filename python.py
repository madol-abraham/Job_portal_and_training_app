class JobPortal:
    def __init__(self):
        self.jobs = []

    def post_job(self, title, company, description):
        self.jobs.append({
            'title': title,
            'company': company,
            'description': description
        })

    def view_jobs(self):
        if not self.jobs:
            print("No jobs available.")
        else:
            print("Available jobs:")
            for index, job in enumerate(self.jobs):
                print(f"{index + 1}. {job['title']} at {job['company']} - {job['description']}")

def main():
    job_portal = JobPortal()

    while True:
        print("\nMenu:")
        print("1. Post a job")
        print("2. View available jobs")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            title = input("Enter job title: ")
            company = input("Enter company name: ")
            description = input("Enter job description: ")
            job_portal.post_job(title, company, description)
            print("Job posted successfully!")
        elif choice == '2':
            job_portal.view_jobs()
        elif choice == '3':
            print("Exiting the job portal.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

