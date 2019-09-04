#teacher
class Teacher(object):
    """for teachers"""
    def __init__(self, name, salary, id):
        self.name = name
        self.salary = salary
        self.id = id
        self.classes = {}

    def add_class(self, class_id, class_name):
        """ adding classes"""
        self.classes[class_id] = class_name
