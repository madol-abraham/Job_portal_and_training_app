class JobPortal:
    def _init_(self):
        self.job_listings = []
        self.training_courses = []

    def add_job_listing(self, title, company, location, description):
        self.job_listings.append({"title": title, "company": company, "location": location, "description": description})

    def add_training_course(self, title, provider, duration, description):
        self.training_courses.append({"title": title, "provider": provider, "duration": duration, "description": description})

    def view_job_listings(self):
        print("==== Job Listings ====")
        for idx, job in enumerate(self.job_listings, 1):
            print(f"{idx}. {job['title']} at {job['company']} ({job['location']})")
            print(job['description'])
            print("=======================")

    def view_training_courses(self):
        print("==== Training Courses ====")
        for idx, course in enumerate(self.training_courses, 1):
            print(f"{idx}. {course['title']} by {course['provider']} (Duration: {course['duration']})")
            print(course['description'])
            print("==========================")

def display_menu():
    print("==== Job Portal and Training Menu ====")
    print("1. View Job Listings")
    print("2. View Training Courses")
    print("3. Add Job Listing")
    print("4. Add Training Course")
    print("5. Exit")
    print("======================================")

if __name__ == "_main_":
    job_portal = JobPortal()

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            job_portal.view_job_listings()
        elif choice == "2":
            job_portal.view_training_courses()
        elif choice == "3":
            title = input("Enter the job title: ")
            company = input("Enter the company name: ")
            location = input("Enter the job location: ")
            description = input("Enter the job description: ")
            job_portal.add_job_listing(title, company, location, description)
            print("Job listing added successfully!")
        elif choice == "4":
            title = input("Enter the course title: ")
            provider = input("Enter the course provider: ")
            duration = input("Enter the course duration: ")
            description = input("Enter the course description: ")
            job_portal.add_training_course(title, provider, duration, description)
            print("Training course added successfully!")
        elif choice == "5":
            print("Thank you for using our Job Portal and Training app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
