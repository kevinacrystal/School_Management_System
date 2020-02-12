'''
This module contains classes that can be used to instantiate 
Student, Course, and Attending objects.

Each class contains:
    1. an _init_ method to instantiate the given object with the required attributes.
    2. getter methods that permit access to those instance attributes without having
    to call them directly.
'''

class Student:
    '''represents the transfer object used to carry student data'''
    def __init__(self, email, s_name, s_password):
        self.email = email
        self.name = s_name
        self.password = s_password
    
    def get_email(self):
        return self.email
    def get_name(self):
        return self.name
    def get_password(self):
        return self.password
    
class Course:
    '''represents the transfer object used to carry course data'''
    def __init__(self,c_id,c_name,instructor):
        self.course_id = c_id
        self.course_name = c_name
        self.instructor = instructor
        
    def get_id(self):
        return self.course_id
    def get_name(self):
        return self.course_name
    def get_instructor(self):
        return self.instructor
    
class Attending:
    '''represents the transfer object used to carry attending data'''
    def __init__(self, course_id, student_email):
        self.course_id = course_id
        self.student_email = student_email
    
    def get_course_id(self):
        return self.course_id
    def get_student_email(self):
        return self.student_email