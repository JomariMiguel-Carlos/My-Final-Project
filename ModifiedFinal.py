print ("\n*********************      FINAL PROJECT       *********************")
print ("\n\n*********************      PROGRAMMED BY       *********************")
print ("*********************  CARLOS, JOMARI MIGUEL   *********************")

import sys

contact = []

def menu():
    print("\n\n********************************************************************")
    print("*\t\t\t            Address Book Main                          *")
    print("********************************************************************")
    print("*\t             Welcome to My Phone Book                          *")
    print("* You can now perform the following operations on this phonebook   *")
    print("********************************************************************")
    print("*\t1. Add a new Contact                                           *")
    print("*\t2. Edit a Contact                                              *")
    print("*\t3. Delete Contact                                              *")
    print("*\t4. Display all contacts                                        *")
    print("*\t5. Search for a contact                                        *")
    print("*\t6. Exit Address Book                                           *")
    print("********************************************************************\n")

    sel = input("Pick One: ")

def add_contact(pb):

        print("ADD CONTACT")
            contact.append(str(input("\nEnter First name: ")).capitalize())
            contact.append(str(input("Enter Last name: ")).capitalize())
            contact.append(str(input("Enter address: ")).capitalize())
            contact.append(int(input("Enter number: ")))
            print("\t", contact)
            for i in range(len(pb)):
                if contact == pb[i]:

        pb.append(contact)

        return pb

def edit_contact(pb):
    print("\t\t\t            EDIT EXISTING CONTACT")
    query =str(input("Please enter the First name of the contact you wish to change: ")).capitalize()
    temp = 0

    for i in range(len(pb)):
        if query == pb[i][0]:
            temp += 1
            print(pb[i])
            choice = int(input(
                "Enter data you want to change\n\n\t1. First Name\n\t2. Last Number\n\t3. Address\n\t4. Contact Number\nPlease enter: "))
            new = []
            new = pb[i]
            print(new)
            check = -1

            if choice == 1:
                bago = str(input("Enter the new First Name: ")).capitalize()
                new[0] = bago
                pb[i] = new
                print("Edited Successfully!!!")

            elif choice == 2:
                bago = str(input("Enter the new Last Name: ")).capitalize()
                new[1] = bago
                pb[i] = new
                print("Edited Successfully!!!")

            elif choice == 3:
                bago = str(input("Enter the new Address: ")).capitalize()
                new[2] = bago
                print(new)
                print("Edited Successfully!!!")


            elif choice == 4:
                bago = int(input("Enter the new Number: "))
                new[3] = bago
                pb[i] = new
                print("Edited Successfully!!!")

                return pb

    def remove_existing(pb):
        print("\t\t\t            REMOVE EXISTING CONTACT")
        query = str(input("Please enter the First name of the contact you wish to remove: ")).capitalize()

        temp = 0

        for i in range(len(pb)):
            if query == pb[i][0]:
                temp += 1

                print(pb.pop(i))

                print("This query has now been removed :)")

                keme = input("Hit Enter to go back to Main Menu...")

                return pb

    elif sel == "3":

        print("\n" * 50)

        for x in people:

            print("Name: " + x[0])
            print("Age: " + x[1])
            print("Address: " + x[2])
            print("Phone Number: " + x[3])

            print("\n")

        input("Press enter/return to continue")

    elif sel == "4":
        isRunning = False
