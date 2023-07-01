class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


employees = []
id = 1

ch = True
while ch:
    name = str(input("Please enter employee name(0 to quit):"))
    if  name == "0":
        id = 1
        for item in employees:
            print("Id:" , id  , "Name:" , item)
            id = id +1
        ch = False
    else:
        employees.append(name)
        id =id +1
