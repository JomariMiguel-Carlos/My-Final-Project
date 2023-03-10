print ("\n*********************      FINAL PROJECT       *********************")
print ("\n\n*********************      PROGRAMMED BY       *********************")
print ("*********************  CARLOS, JOMARI MIGUEL   *********************")


import sys

def menu():
    print("\n\n********************************************************************")
    print("*\t\t\t            Address Book Main                          *")
    print("********************************************************************")
    print("*\t             Welcome to My Address Book                        *")
    print("* You can now perform the following operations on this phonebook   *")
    print("********************************************************************")
    print("*\t1. Add a new Contact                                           *")
    print("*\t2. Edit a Contact                                              *")
    print("*\t3. Delete Contact                                              *")
    print("*\t4. Display all contacts                                        *")
    print("*\t5. Search for a contact                                        *")
    print("*\t6. Exit Address Book                                           *")
    print("********************************************************************\n")

def add_contact(pb):


    ans = 'y'
    while ans == 'y':
        ques = 'n'
        print("\n********************************************************************")
        print("\t\t\t            ADD CONTACT")
        print("********************************************************************")

        while ques == 'n':
            contact = []

            contact.append(str(input("\nEnter First name: ")).capitalize())
            contact.append(str(input("Enter Last name: ")).capitalize())
            contact.append(str(input("Enter address: ")).capitalize())
            contact.append(int(input("Enter number: ")))
            print("\t",contact)
            for i in range(len(pb)):
                if contact == pb[i]:
                    print("\t\tThe contact is already on the Address Book!!!")
            ques = input("\nDo you really want to add this contact? (y/n) ")


        pb.append(contact)
        ans = input("Do you want to add another contact? (y/n) ")
    keme = input("Hit Enter to go back to Main Menu...")
    print("********************************************************************")


    return pb

def edit_contact(pb):
    print("\n********************************************************************")
    print("\t\t\t            EDIT EXISTING CONTACT")
    print("********************************************************************")
    query =str(input("Please enter the First name of the contact you wish to change: ")).capitalize()
    contact = []
    temp = 0

    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb[i])
            choice = int(input(
                "Enter data you want to change\n\n\t1. First Name\n\t2. Last Name\n\t3. Address\n\t4. Contact Number\nPlease enter: "))
            new = []
            new = pb[i]
            print(new)
            check = -1

            if choice == 1:
                bago = str(input("Enter the new First Name: ")).capitalize()
                new[0] = bago
                pb[i] = new
                print("Edited Successfully!!!")
                keme = input("Hit Enter to go back to Main Menu...")

            elif choice == 2:
                bago = str(input("Enter the new Last Name: ")).capitalize()
                new[1] = bago
                pb[i] = new
                print("Edited Successfully!!!")
                keme = input("Hit Enter to go back to Main Menu...")

            elif choice == 3:
                bago = str(input("Enter the new Address: ")).capitalize()
                new[2] = bago
                print(new)
                print("Edited Successfully!!!")
                keme = input("Hit Enter to go back to Main Menu...")


            elif choice == 4:
                bago = int(input("Enter the new Number: "))
                new[3] = bago
                pb[i] = new
                print("Edited Successfully!!!")
                keme = input("Hit Enter to go back to Main Menu...")

    if temp == 0:
        print("Sorry, you have entered an invalid query.\
        Please recheck and try again later.")
        keme = input("Hit Enter to go back to Main Menu...")

    return pb

def remove_existing(pb):
    print("\n********************************************************************")
    print("\t\t\t            REMOVE EXISTING CONTACT")
    print("********************************************************************")
    query = str(input("Please enter the First name of the contact you wish to remove: ")).capitalize()

    temp = 0

    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1

            print(pb.pop(i))

            print("This query has now been removed :)")

            keme = input("Hit Enter to go back to Main Menu...")

            return pb
    if temp == 0:
        print("Sorry, you have entered an invalid query. Please recheck and try again later.")
        keme = input("Hit Enter to go back to Main Menu...")

        return pb

def display_all(pb):
    print("\n********************************************************************")
    print("\t\t\t            ALL CONTACTS")
    print("********************************************************************")
    print("First Name,     Last Name,      Address,        Number")
    if not pb:
        print("List is empty: []")
    else:
        for i in range(len(pb)):
            pb.sort()
            print( *pb[i], sep= ",\t\t\t\t")

    keme = input("Press Enter to continue... ")

def search_existing(pb):
    print("********************************************************************")
    print("\t\t\t            SEARCH EXISTING CONTACT")
    print("********************************************************************")
    choice = int(input("Enter search criteria\n\t1. First Name\n\t2. Last Number\n\t3. Address\n\t4. Contact Number\nPlease enter: "))

    temp = []
    check = -1

    if choice == 1:
        query = str(
            input("\nPlease enter the first name of the contact you wish to search: ")).capitalize()
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])

    elif choice == 2:
        query = str(
            input("\nPlease enter the last name of the contact you wish to search: ")).capitalize()
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])

    elif choice == 3:
        query = str(input("\nPlease enter the Address of the contact you wish to search: ")).capitalize()
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])

    elif choice == 4:
        query = int(input("\nPlease enter the number of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])


    else:
        print("Invalid search criteria")
        return -1

    if check == -1:
        return -1
    else:
        display_all(temp)

        return check
        keme = input("Press Enter to continue... ")

def thanks():
    print("********************************************************************")
    print("Thank you for using our Smartphone directory system.")
    print("Please visit again!")
    print("********************************************************************")
    sys.exit("Goodbye, have a nice day ahead!")


add_book = []
cnum = 0
choice = 0
while choice in (0, 1, 2, 3, 4, 5):
    menu()
    choice = int(input("Please enter your choice: "))
    if choice == 1:
        add_book = add_contact(add_book)
        cnum += 1

    elif choice == 2:
        add_book = edit_contact(add_book)

    elif choice == 3:
        add_book = remove_existing(add_book)
        cnum -= 1

    elif choice == 4:
        display_all(add_book)
    elif choice == 5:
        d = search_existing(add_book)
        if d == -1:
            print("The contact does not exist. Please try again")
    else:
        thanks()
