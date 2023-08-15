class JobPortal:
    def __init__(self):
        self.job_listings = []
        self.training_courses = []

    def add_job_listing(self, title, company, location, description):
        self.job_listings.append({"title": title, "company": company, "location": location, "description": description})

    def add_training_course(self, title, provider, duration, description):
        self.training_courses.append(
            {"title": title, "provider": provider, "duration": duration, "description": description})

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


def main():
    job_portal = JobPortal()
    menu_functions = {
        "1": job_portal.view_job_listings,
        "2": job_portal.view_training_courses,
        "3": job_portal.add_job_listing,
        "4": job_portal.add_training_course
    }

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "5":
            print("Thank you for using our Job Portal and Training app. Goodbye!")
            break

        if choice in menu_functions:
            function = menu_functions[choice]
            if choice in ["3", "4"]:
                title = input("Enter the title: ")
                provider = input("Enter the provider: ")
                duration = input("Enter the duration: ")
                description = input("Enter the description: ")
                function(title, provider, duration, description)
                print("Added successfully!")
            else:
                function()
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

