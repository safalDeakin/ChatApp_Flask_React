class Student(object):
    name = None

    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super (Student,cls).__new__(cls)
        return cls.instance


s1 = Student()
print s1
