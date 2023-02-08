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

    elif sel == "2":

        print("\n" * 50)

        count = 1

        for x in people:
            print(str(count) + ": " + x[0])
            count += 1

        deleted = int(input("Pick One: ")) - 1

        if deleted == len(people):

            del(people[deleted])

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
