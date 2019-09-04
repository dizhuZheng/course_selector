import classes
import course
import student
import teacher 

class School(object):
    def __init__(self, name, address):
        self.name = name 
        self.address = address
        self.courses = {}
        self.teacher = {}
        self.clesses = {}
    
    def create_course(self, price, name, period):
        new_course = course(price=price, name=name, period=period)
        self.courses[name] = new_course
    
    def course_info(self, name):
        print(self.courses[name].name+self.courses[name].period+self.courses[name].price)

    def create_teacher(self,)
