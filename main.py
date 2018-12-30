Empty_list = [''] #initializing list
required_list = Empty_list*75 

# this is the checking of choice of the user

choice = int(input("What do you want to do? press 1 for Record entering and 2 for retrieving the record "))
if choice==1:
    no_of_record = int(input("How many records you want to add "))
    for _ in range(1,no_of_record+1):
        Employee_Number = int(input("Enter employee number (5 digits) "))
        Employee_Name = str(input("Enter the name of Employee "))
        Landline_number = int(input('Enter landline number '))
        Mobile_Number = int(input('Enter mobile number '))

 # function to calculate the hash address 
def hashing():
        hashe = Employee_Number % 73
        if required_list[hashe] == '':
            required_list[hashe] = Employee_Name,Landline_number,Mobile_Number
            print('the record is at ',hashe)
        else:
            required_list[hashe+1] = Employee_Name,Landline_number,Mobile_Number
            print('the record is at ',hashe+1)





hashing()
print(Empty_list,"position") # this will show the output of the list