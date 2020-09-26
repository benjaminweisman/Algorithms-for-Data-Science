#This was a group assignment worked on by Conor Howlett, Benjamin Weisman, Amanda Norton, and Carloyn Herrera


class Student:
    
    ''' Creates the "Student" class. Each object has properties that are 
    associated with each student.'''
    
    def __init__(self, name, level, major, year, registration, 
                 dropped=False):
        ''' Each student has the following properties:
            
            - name: A string input of their full legal name
            - level: A string input of their current education level.
                (Graduate, Undergraduate, Auditor)
            - major: A string input of the student's major.
            - year: An integer input of the student's current year in 
                their respective level of education (1-4)
            - registration: An integer input (1-5) of which day of 
                orientation the student enrolled in the course.
            - dropped: This property defaults to False, but can be specified
                to indicate that the student has dropped the course.'''
        self.name = name
        self.level = level
        self.major = major
        self.year = year
        self.registration = registration
        self.dropped = dropped
        
    def get_points(self):
        
        ''' This function evalautes all of the properties that are considered
        in a perspective student, and assigns the student a score. 
        The score is an integer between 1 and 46 inclusive, with 1 showing
        the best chances for a student to be accepted into the class, and 46 
        being the worst chances for the student to be accepted.
        All graduate students recieve a 1, since the year and the day they
        apply are not taken into account (as long as it was done within the
        orientation week deadline.
        Auditors who applied on the 5th day of orientation week are given a
        score of 46.
        For Undergraduate students, they are scored an extra 20 points if
        their major is either Computer Science or Math. 
        Their year is also factored into the score, with 5 points being
        awarded for each year of education they have completed.'''
        total = 47
        if self.level == 'Graduate':
            return 1
        if self.level == 'Undergraduate':
            total -= 5
            if self.year == 4:
                total -= 15
            if self.year == 3:
                total -= 10
            if self.year == 2:
                total -= 5
            if self.major == 'Computer Science' or self.major == 'Math':
                total -= 20
        if self.registration == 5:
            total -= 1
        if self.registration == 4:
            total -= 2
        if self.registration == 3:
            total -= 3
        if self.registration == 2:
            total -= 4
        if self.registration == 1:
            total -= 5
        return total
    
    def create_key(self):
        
        ''' This function simply returns the string of the student's 
        full legal name, to be used later as a key in a student dictionary'''
        
        return f"{self.name}"

''' Below are the people who are applying to enroll in the course.
They belong to the Class we created above called "Students".
The students' relevant information is included in their properties.'''

steve = Student('Steve Madison', 'Graduate', 'Data Science', 1, 2, 
                dropped=True)
toby = Student('Toby Michaels', 'Graduate', 'Data Science', 1, 3)
adam = Student('Adam Smith', 'Undergraduate', 'Computer Science', 3, 1)
mike = Student('Mike Honcho', 'Undergraduate', 'Math', 1, 4)
mary = Student('Mary Elizabeth', 'Undergraduate', 'Music', 4, 1)
kim = Student('Kim Jones', 'Undergraduate', 'Theater', 2, 5)
scott = Student('Scott Hendrix', 'Undergraduate', 'Economics', 2, 3)
ali = Student('Ali Heart', 'Auditor', 'Business', 4, 2)
valerie = Student('Valerie Smith', 'Undergraduate', 'Finance', 3, 1)
todd = Student('Todd Kim', 'Undergraduate', 'Finance', 4, 2)
frank = Student('Frank Howard', 'Undergraduate', 'Finance', 3, 3)
troy = Student('Troy Koi', 'Undergraduate', 'Finance', 1, 1)
cedric = Student('Cedric Kerr', 'Undergraduate', 'Finance', 4, 4)
austin = Student('Austin Maynard', 'Undergraduate', 'Finance', 3, 5)
cody = Student('Cody Jhin', 'Undergraduate', 'Finance', 3, 4)
ahmed = Student('Ahmed Andrews', 'Undergraduate', 'Finance', 2, 4)
carrie = Student('Carrie Jones', 'Undergraduate', 'Math', 3, 4)
emma = Student('Emma Smith', 'Auditor', 'Finance', 1, 3)
olivia = Student('Olivia Brown', 'Undergraduate', 'Finance', 3, 5)
vicky = Student('Vicky Garcia', 'Undergraduate', 'Finance', 4, 4)
mary2 = Student('Mary Miller', 'Undergraduate', 'Computer Science', 3, 2,
                dropped=True)
edward = Student('Edward Nelson', 'Auditor', 'Finance', 2, 4)
alexia = Student('Alexia Torres', 'Graduate', 'Finance', 2, 4)
michelle = Student('Michelle Roberts', 'Auditor', 'Finance', 3, 1)
gloria = Student('Gloria Spooner', 'Undergraduate', 'Math', 1, 5)
harry = Student('Harry Young', 'Undergraduate', 'Finance', 3, 3)
amelia = Student('Amelia Brownlee', 'Graduate', 'Data Science', 1, 4)
sophie = Student('Sophie Lee', 'Auditor', 'Finance', 1, 2)
isabella = Student('Isabella Cruise', 'Graduate', 'Finance', 2, 1)
charlotte = Student('Charlotte Hunt', 'Auditor', 'Art', 1, 2,
                    dropped=True)

''' Below is a list of the perspective students, each item containing 
a variable name of each student object in our Student class.'''
student_lst = [steve, toby, adam, mike, mary, kim, scott, ali, valerie,
               todd, frank, troy, cedric, austin, cody, ahmed, carrie,
               emma, olivia, vicky, mary2, edward, alexia, michelle,
               gloria, harry, amelia, sophie, isabella]


def parent(i):
    ''' Returns the parent in a max-heap.'''
    return i//2

def left(i):
    ''' Returns the left child.'''
    return 2*i +1

def right(i):
    ''' Returns the right child.'''
    return 2*i +2

def max_heapify(a, heap_size, i):
    ''' Maintains that a heap is sorted and that children smaller than their 
    parent node'''
    l = left(i)
    r = right(i)
    if l <= heap_size -1 and a[l] > a[i]:
        largest = l
    else:
        largest = i
    if r <= heap_size -1 and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, heap_size, largest)
        
def build_max_heap(a):
    '''Creates a max heap, callng max-heapify iteratively for the length
    of the array'''
    for i in range(len(a) // 2 - 1, -1, -1):
        max_heapify(a, len(a), i)

def heapsort(a):
    '''Sorts an array by calling the build_max_heap and max_heapify functions.
    Converts array into max heap and then sorts the array into non-decreasing
    order.'''
    build_max_heap(a)
    for i in range(len(a)-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        max_heapify(a, i, 0)
        
'''Initiates an empty dictionary that will be populated with student
names and their scores as the keys and values'''
student_dict = {}

'''Adds students to the dictionary if they have not dropped the class.
Their names are the keys, and the points
atrributed to them are their respective values'''
for i in student_lst:
    if not i.dropped:
        student_dict[i.create_key()] = i.get_points()

'''Initiates an array and iterates through all of the students' scores to 
populate with integers'''
values_lst = []
for i in student_dict:
    values_lst.append(student_dict[i])

'''Sets the list to equal itself minus the redundant scores students'''
values_lst = list(set(values_lst))

'''Uses build max heap, max heapify, and heapsort build a max heap out of
the students' scores, then uses heapsort to sort the array'''
heapsort(values_lst)

'''A nested For loop that first iterates through all of the sorted scores 
for the students, then iterates through the student dictionary, looking for 
values that match the the heapsorted values in the list.
Prints out the place of the student, and the students full legal name for up 
to a maximum of 25 students.
If less than 26 students enroll, they will all be accepted, so long as they
did not drop the class.''' 
n = 1
for i in values_lst:
    for key in student_dict:
        if student_dict[key] == i:
            if n == 26:
                break
            print(str(n) +'. ' + str(key) )
            n +=1
