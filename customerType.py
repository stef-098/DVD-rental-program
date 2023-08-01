import csv
from BinarySearch import *

#class to store methods relating to customer
class customerListType():
    def __init__(self, firstName, lastName, phoneNumber, id, movieRented):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__phoneNumber = phoneNumber
        self.__id = id
        self.__movieRented = movieRented

    #method to set customer's first name
    def setFirstName(self, firstName):
        self.__firstName = firstName

    #method to set customer's last name
    def setLastName(self, lastName):
        self.__lastName = lastName
    
    #method to set customer's phone number
    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    #method to set customer id
    def setId(self, id):
        self.__id = id
    
    #method to set customer's dvd rented
    def setMovieRented(self, movieRented):
        self.__movieRented = movieRented
    
    #method to get customer's first name
    def getFirstName(self):
        return self.__firstName 
    
    #method to get customer's last name
    def getLastName(self):
        return self.__lastName 
    
    #method to get customer's phone number
    def getPhoneNumber(self):
        return self.__phoneNumber

    #method to get customer id
    def getId(self):
        return self.__id
    
    #method to set customer's rented dvd
    def getMovieRented(self):
        return self.__movieRented 
    
    #method to string customers' details 
    def __str__(self):
        return f'First name: {self.__firstName}\n' + \
            f'Last name: {self.__lastName}\n' + \
            f'Phone number: {self.__phoneNumber}\n' + \
            f'ID: {self.__id}\n' + \
            f'Movie rented: {customerListType.listString(self.__movieRented)}\n' 
        
    #changing the list format of movie rented variable to a string
    def listString(lists):
        newstring = ""
        for value in lists:
            newstring += "\n" + value 
        return newstring

        
    #compare if an object is equal to another object based on the customer id
    def __eq__(self, other): 
        return self.__id == other
    
    #compare if an object is less than the other object based on the customer id
    def __lt__(self, other):
        return self.__id < other

    #compare if an object is less than or equal to the other object based on the customer id
    def __le__(self, other):
        return self.__id <= other
    
    #compare if an object is greater than the other object based on the customer id
    def __gt__(self, other):
        return self.__id  > other

    #compare if an object is greater or equal to other object based on the customer id
    def __ge__(self, other):
        return self.__id >= other

    #method to add new customer to the system
    def registerCustomer(): 
        firstName = input("Enter first name: ")
        lastName = input("Enter last name: ")
        phoneNumber = input("Enter phone number: ")
        custId = input("Enter ID: ")
        rentedDVD = []
        dvd = input("Enter rented DVD: ")
        rentedDVD.append(dvd)
        #continue to add more dvds in customer's rented dvd
        choice = input("Is there more DVD rented by customer ? If yes, input y or Y") 
        while choice == 'Y' or choice == 'y':
            dvd = input("Enter rented DVD: ")
            rentedDVD.append(dvd)
            choice = input("Is there more DVD rented by customer ? If yes, input y or Y\n") 
        newCustomer = customerListType(firstName, lastName, phoneNumber, custId, rentedDVD)
        cust = firstName, lastName, phoneNumber, custId, rentedDVD
        #append new customer to csv file
        with open("listOfCustomers.csv", 'a+', newline='') as file2: 
            new = csv.writer(file2)
            new.writerow(cust)
        #append new customer to binary search tree
        customerList.insert(newCustomer)

    #method to search for a customer
    def searchCustomer():
        custId = input("Enter customer's ID: ")
        customerList.search(custId)
    
    #method to print all the customer in the binary tree sorted by the customer ID
    def printCustomers():
        custDetails = customerList.traversal(customerList)
        for value in custDetails:
            print(value)

#read customer details from csv file and append it to list
with open("listOfCustomers.csv") as file2:
    custList = []
    rentedDvd = []
    for row in file2:
        count = 4
        row = row.strip("\n")
        column = row.split(',')
        firstName = column[0]
        lastName = column[1]
        phoneNumber = column[2]
        custId = column[3]
        #insert movies rented by customer into the a list
        while count < (len(column) + 1): 
            rentedDvd.append(column[count])
            count += 1
            if count >= len(column):
                break
        customer = customerListType(firstName, lastName, phoneNumber, custId, rentedDvd)
        custList.append(customer)
        #clear the list so that it doesn't mix with the movies rented by other customer 
        rentedDvd = []
#insert each value from the list to binary search tree
customerList = binarySearch(custList[0])
customerList.insert(custList[1])
customerList.insert(custList[2])
customerList.insert(custList[3])
customerList.insert(custList[4])