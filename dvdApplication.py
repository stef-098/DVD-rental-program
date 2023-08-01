from customerType import *
from dvdClass import dvdType


#class that contains the main application 
class main(): 
    #print option for user whether they are admin or customer
    def printOption():
        status = "Modes:"
        status += "\n1. Admin"
        status += "\n2. Customer"
        print(status)

    #print menu for admin
    def adminMenu():
        menu = ""
        menu += "\n1. Add new movie"
        menu += "\n2. Update movie's stock"
        menu += "\n3. Search for a customer"
        menu += "\n4. Print all customer"
        menu += "\n5. Register a new customer"
        menu += "\n6. List all the DVDs in store"
        menu += "\n7. Exit Application"
        print(menu)

    #print menu for customers
    def userMenu():
        menu = ""
        menu += "\n1. Rent a DVD"
        menu += "\n2. Return a DVD"
        menu += "\n3. List all the DVDs in store"
        menu += "\n4. Search for a DVD"
        menu += "\n5. Exit Application"
        print(menu)
    
    print("Welcome to DVD application!")
    
    #print option for user
    printOption()
    operation = int(input("Selected mode: "))
    print()

    #if user is an admin
    if operation == 1: 
        adminMenu()
        option1 = int(input("Selected option: "))

        while option1 != 7:
            #option will add new DVD into the system
            if option1 == 1: 
                dvdType.addNewDVD()
                adminMenu()
                option1 = int(input("Selected option: "))  
                print()              

            #option will update a movie's stock
            elif option1 == 2:
                dvdType.updateMovieStock()
                adminMenu()
                option1 = int(input("Selected option: "))  
                print()

            #option will print all the customer in the system
            elif option1 == 3: 
                customerListType.searchCustomer()
                adminMenu()
                option1 = int(input("Selected option: "))
                print()

            #option will register new customer into the database and linked list
            elif option1 == 4: 
                customerListType.printCustomers()
                adminMenu()
                option1 = int(input("Selected option: "))
                print()
            
            #option will register new customer into the database and linked list
            elif option1 == 5: 
                customerListType.registerCustomer()
                adminMenu()
                option1 = int(input("Selected option: "))
                print()

            #option will list all DVDs the store has with all its details
            elif option1 == 6: 
                print("List of DVDs in the store: ")
                dvdType.printDVDList()
                adminMenu()
                option1 = int(input("Selected option: "))
                print()

            #if user input numbers that are not listed on the menu
            else: 
                print("Invalid input! Please enter a valid option!\n")
                adminMenu()
                option1 = int(input("Selected option: "))
                print()
        #message printed when the user exit the system
        print("Thank you for using DVD application! See you next time!")
    
    #the operations if the user is a customer
    if operation == 2: 
        userMenu()
        option2 = int(input("Selected option: "))

        while  option2 != 5:
            #option will allow user to rent a movie 
            if option2 == 1: 
                dvdType.rentDVD()
                userMenu()
                option2 = int(input("Selected option: "))
                print()
            
            #option will allow user to return a movie to the store
            elif option2 == 2:
                dvdType.returnDVD()
                userMenu()
                option2 = int(input("Selected option: "))
                print()
            
            #option will list all DVDs along with its details the store has
            elif option2 == 3:
                print("List of DVDs in the store: ")
                dvdType.printDVDList()
                userMenu()
                option2 = int(input("Selected option: "))
                print()
            
            #option will search the DVD according to user's input
            elif option2 == 4:
                movie = input("Enter searched movie title: ")
                dvdType.searchTitle(movie)
                userMenu()
                option2 = int(input("Selected option: "))
                print()
            
            #if user input numbers that are not listed on the menu
            else: 
                print("Invalid input! Please enter a valid input!\n")
                userMenu()
                option2 = int(input("Selected option: "))
                print()

        #message printed when the user exit the system
        print("Thank you for using DVD application! See you next time!")