student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6
}

# First, display the complete record using for loop, printing and some string formatting only
print("CURRENT STUDENT RECORD")
for key, value in student.items():
    print(f"{key:<12}: {value}")

# Check if there's a key called 'email'. If not, ask the user to enter an email
if "email" not in student:
    email = input("\nEmail: ").strip()
    while not email:
        print("Error: the email cannot be empty.")
        email = input("Email: ").strip()
    student["email"] = email

# Ask the user to enter a new city, and update the existing city with this new one
# Make sure the new city is not an empty string
new_city = input("\nNew city: ").strip()
if new_city:
    student["city"] = new_city
else:
    print("Error: the city cannot be empty. The original city has been kept.")

# Check if there's 'phone' key in the dictionary. If not, print a message saying "Phone number not found."
# Use the get() method
print(student.get("phone", "Phone number not found."))

# Add a new key called 'contact' to the dictionary, which is itself a dictionary containing two keys: 'phone' and 'email'.
phone = student.get("phone", "")
while not phone:
    phone = input("Phone number: ").strip()
    if not phone:
        print("Error: the phone number cannot be empty.")
student["contact"] = {"phone": phone, "email": student["email"]}

# Add another key called 'courses' to the dictionary, which is itself a dictionary containing three keys: 'Python', 'Databases', and 'Software Engineering', with 88, 91, and 84 as their corresponding scores
student["courses"] = {
    "Python": 88,
    "Databases": 91,
    "Software Engineering": 84
}

# Calculate the average score for the student without built-in functions like sum(). Use a for loop instead.
def calculate_average(courses):
    total = 0
    count = 0
    for score in courses.values():
        total += score
        count += 1
    return total / count


average_score = calculate_average(student["courses"])

# Add a new key called 'academic_status' to the dictionary
# It should be a string that indicates the student's academic status based on the average score.
# If the score is >= 90, the status should be "Excellent".
# If the score is >= 75, the status should be "Good".
# If the score is >= 60, the status should be "Pass".
# If the score is < 60, the status should be "At Risk".
def get_academic_status(average):
    if average >= 90:
        return "Excellent"
    if average >= 75:
        return "Good"
    if average >= 60:
        return "Pass"
    return "At Risk"


student["academic_status"] = get_academic_status(average_score)

# Add the logic to search for a course.
# If the course is found, print the course name and score. If not, print "Course not found".
def find_course(name):
    for course in student["courses"]:
        if course.casefold() == name.strip().casefold():
            return course
    return None


course_name = find_course(input("\nCourse to search for: "))
if course_name is None:
    print("Course not found")
else:
    print(f"{course_name}: {student['courses'][course_name]:g}")

# Add the logic to update a course score.
# Ask the user to enter the course name and the new score.
# If the course is found, then update the score and print a message indicating the change.
# While adding the new course, make sure the new score is a number between 0 and 100
course_name = find_course(input("\nCourse to update: "))
if course_name is None:
    print("Course not found")
else:
    try:
        new_score = float(input("New score (0-100): "))
    except ValueError:
        print("Error: the score must be a number.")
    else:
        if not 0 <= new_score <= 100:
            print("Error: the score must be between 0 and 100.")
        else:
            old_score = student["courses"][course_name]
            student["courses"][course_name] = new_score
            print(f"{course_name} updated from {old_score:g} to {new_score:g}.")

# Recaclculate the average score and update the academic status after the course score has been updated.
average_score = calculate_average(student["courses"])
student["academic_status"] = get_academic_status(average_score)

# Display the final formatted student record with all the updated information, including the average score and academic status.
# It should look like the following:
"""
=====================================
        STUDENT RECORD
=====================================

Name: Alice Wong
Student ID: ST1024
Age: 21
Program: Software Engineering
City: Shanghai
GPA: 3.6

CONTACT
Phone: 13800001111
Email: alice.wong@university.edu

COURSE RESULTS
Python: 88
Databases: 91
Software Engineering: 84

Average Score: 87.7
Academic Status: Good

===================================== """
print("\n=====================================")
print("        STUDENT RECORD")
print("=====================================\n")
print(f"Name: {student['name']}")
print(f"Student ID: {student['student_id']}")
print(f"Age: {student['age']}")
print(f"Program: {student['program']}")
print(f"City: {student['city']}")
print(f"GPA: {student['gpa']}")

print("\nCONTACT")
print(f"Phone: {student['contact']['phone']}")
print(f"Email: {student['contact']['email']}")

print("\nCOURSE RESULTS")
for course, score in student["courses"].items():
    print(f"{course}: {score:g}")
print(f"\nAverage Score: {average_score:.1f}")
print(f"Academic Status: {student['academic_status']}")
print("\n=====================================")

