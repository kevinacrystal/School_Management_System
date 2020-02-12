'''this module contains all Data Access Object classes used by the program'''
import Models as m

class StudentDAO:
    '''represents the Data Access Object that allows access to the data source students.csv'''
    def __init__(self):
        ''' reads data from students.csv and instantiates StudentDAO object with a list of Student objects '''
        with open('students.csv', 'r') as f:
            student_lines = f.read().splitlines()
            self.students = []
            for student in student_lines:
                info_list = student.split(',')
                self.students.append(m.Student(info_list[0], info_list[1], info_list[2]))
        
    def get_students(self):
        ''' returns a list of student objects '''
        return self.students   
        
    def validate_user(self, email, pw):
        ''' takes an email and a password from user input '''
        ''' returns True if a student with the given info is found, False otherwise '''
        for i in range(len(self.students)):
            if self.students[i].email == email and self.students[i].password == pw:
                return True
        return False
     
    def get_student_by_email(self, email):
        ''' takes a student email as a string and searches the list of student objects for the object with that email '''
        ''' returns the corresponding student object '''
        for i in range(len(self.students)):
            if self.students[i].email == email:
                return self.students[i]
            
    
class CourseDAO:
    '''represents the Data Access Object that allows access to the data source courses.csv'''
    def __init__(self):
        ''' reads data from courses.csv and instantiates CourseDAO object with a list of Course objects '''
        with open('courses.csv', 'r') as f:
            course_lines = f.read().splitlines()
            self.courses = []
            for course in course_lines:
                info_list = course.split(',')
                self.courses.append(m.Course(info_list[0], info_list[1], info_list[2]))
        
    def get_courses(self):
        ''' returns a list of Course objects '''
        return self.courses

    
class AttendingDAO:
    '''represents the Data Access Object that allows access to the data source attending.csv'''
    def __init__(self):
        ''' reads data from attending.csv and instantiates AttendingDAO object with a list of Attending objects '''
        with open('attending.csv', 'r') as f:
            lines = f.read().splitlines()
            self.attending = []
            for line in lines:
                c_id, email = line.split(',')[0], line.split(',')[1]
                self.attending.append(m.Attending(c_id, email))
        
    def get_attending(self):
        ''' returns a list of Attending objects '''
        return self.attending
    
    def get_student_courses(self, course_list, email):
        ''' takes a student's email and a course List as parameters '''
        ''' searches the List of Attending objects for all the courses corresponding to the email '''
        ''' returns a list of courses the student is attending '''
        self.student_course_ids = [i.course_id for i in self.attending if i.student_email == email]
        self.student_courses = []
        for i in self.student_course_ids:
            for j in course_list:
                if i == j.course_id:
                    self.student_courses.append(j)
        return self.student_courses
        
    def register_student_to_course(self, email, course_id, course_list):
        ''' takes a student's email, a course ID, and a course list as parameters '''
        ''' checks if a student with that email is currently attending a course with that course ID '''
        ''' returns an alert if the student is already registered for the course or if the course ID is invalid '''
        ''' otherwise, add a new Attending object to the list of Attending objects, overwrites attending.csv and returns True'''
        course_id_list = [course.get_id() for course in course_list]
        course_email = [course_id, email]
        if course_email in [[course.course_id, course.student_email] for course in self.attending]:
            print('\nYou Are Already Registered In The Course.')
            return False
        elif course_id not in course_id_list:
            print('\nNot A Valid Course ID Number...')
            return False
        else:
            self.attending.append(m.Attending(course_id, email))
            self.save_attending()
            print('\nRegistration Successful!')
            return True
        
    def save_attending(self):
        ''' overwrites the original Attending.csv file with the new data '''
        attending_text = ''
        for i in self.attending:
            attending_text+=(f'{i.course_id},{i.student_email}\n')
        with open('attending.csv', 'w') as f:
            f.write(attending_text)
    
    