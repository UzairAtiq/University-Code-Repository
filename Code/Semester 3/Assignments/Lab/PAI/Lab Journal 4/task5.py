# Lab Journal 4 - Task 5: Object-Oriented Programming
# Programming for Artificial Intelligence

class Student:
    """Student class demonstrating OOP concepts"""
    
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course
        self.grades = []
    
    def add_grade(self, grade):
        """Add a grade to the student's record"""
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 100")
    
    def get_average(self):
        """Calculate and return average grade"""
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0
    
    def get_letter_grade(self):
        """Convert average to letter grade"""
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    
    def display_info(self):
        """Display student information"""
        print(f"Student: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Course: {self.course}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.get_average():.2f}")
        print(f"Letter Grade: {self.get_letter_grade()}")

class AIStudent(Student):
    """AI Student class inheriting from Student"""
    
    def __init__(self, name, student_id, specialization):
        super().__init__(name, student_id, "Programming for AI")
        self.specialization = specialization
        self.projects = []
    
    def add_project(self, project_name):
        """Add a project to the student's portfolio"""
        self.projects.append(project_name)
    
    def display_info(self):
        """Override parent method to include AI-specific info"""
        super().display_info()
        print(f"AI Specialization: {self.specialization}")
        print(f"Projects: {self.projects}")

def main():
    print("Lab Journal 4 - Task 5: Object-Oriented Programming")
    
    # Create AI student instance
    ai_student = AIStudent("Alice Johnson", "AI001", "Machine Learning")
    
    # Add grades and projects
    ai_student.add_grade(95)
    ai_student.add_grade(87)
    ai_student.add_grade(92)
    
    ai_student.add_project("Neural Network Implementation")
    ai_student.add_project("Data Visualization Dashboard")
    
    # Display student information
    ai_student.display_info()
    
    print("\n" + "="*50)
    
    # Create regular student for comparison
    regular_student = Student("Bob Smith", "CS001", "Computer Science")
    regular_student.add_grade(78)
    regular_student.add_grade(82)
    regular_student.add_grade(85)
    
    regular_student.display_info()

if __name__ == "__main__":
    main()