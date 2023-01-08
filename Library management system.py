#LIBRARY MANAGEMENT SYSTEM
#Authorisation of admin
while True:
    print("Welcome to Library management system!")
    password = input("Please enter admin password:")

    #Making a drop down menu
    def main():
        print("1. Issue Books" ) 
        print("2. Return Books")

    #Authorisation of admin
    if password == "bia":
        main()
    else:
        print("You have entered the incorrect password (1/2)")
        next = int(input("Enter 0 to try again, or 1 to exit: "))
        if next==0:
            password = input("Please enter admin password:")
            if password == "bia":
                main()
            else:
                print("You have entered incorrect password (2/2).")
                print("You have exited.")
        elif next == 1:
            print("You have exited.")
        else:
            print("Enter correct integer.")

    #Taking input from the user to perform the task
    option = int(input("Enter the serial number of the task to be performed: "))
    book_data   = ["book_name","author_name",]

    #Issuing books
    if option == 1:
        book_data_issue   = ["name","issue_name", "date"]
        dict        = {"name":"student_name","issue_name":'book_name',"date":'date'}
        book_name   = input("Enter the name of the book to be issued: ")
        available = input("Is this book available? (yes/no)")
        if available == "yes":
            name        = input("Enter student's full name: ")
            date = input("Enter todays date in this format '1 january 2023': ")
            dict["name"]= name
            dict["issue_name"]=book_name
            dict["date"] = date
            print("Here is your data",dict)
            print("Remind the student to return the book in the next class.")
        else:
            print("Book is not available")

    #Returning books
    elif option == 2:
        book_data_return   = ["name","return_name", "date"]
        dict        = {"name":"student_name","return_name":'book_name',"date":'date'}
        name = input("Enter your full name: ")
        book_name   = input("Enter the name of the book to be returned: ")
        date = input("Enter todays date in this format '1 january 2023': ")
        dict["name"]= name
        dict["return_name"]=book_name
        dict["date"] = date
        print("Here is your data",dict)
    else:
        print("Enter correct integer.")
        main()
    








    
 

