class Student(object):
    def __init__(self, name, last, age):
        self.age = age
        self.name = name
        self.last = last

    def describe(self):
        print 'This student is ' + self.name + ' ' + self.last + ' and is %i years old.' % self.age


class ForeignStudent(Student):
    def __init__(self, name, last, age, nation):
        super(ForeignStudent, self).__init__(name, last, age)
        self.nation = nation

    def describe(self):
        print 'This student is %s %s and is %i years old and comes from %s.' \
              % (self.name, self.last, self.age, self.nation)


s1 = Student('Lorenzo', 'Costa', 22)
s4 = ForeignStudent('Mark', 'Dwayne', 23, 'USA')
s2 = Student('Arianna', 'Pravettoni', 21)
s3 = Student('Alice', 'Costa', 19)
s5 = ForeignStudent('Malambe', 'Uktur', 18, 'Zimbabwe')
for s in s1, s4, s2, s3, s5:
    s.describe()
