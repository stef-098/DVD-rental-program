from linkedList import *
import csv
from customerType import *

#class to store methods relating to dvd
class dvdType(): 
    def __init__(self, name, genre, producer, director, productionCompany, actor1, actor2, actor3, copiesNumber):
        self.__name = name
        self.__genre = genre
        self.__producer = producer
        self.__director = director
        self.__productionCompany = productionCompany
        self.__actor1 = actor1
        self.__actor2 = actor2
        self.__actor3 = actor3
        self.__copiesNumber = copiesNumber
    
    #method to set movie name
    def setName(self, name): 
        self.__name = name

    #method to set movie's genre
    def setGenre(self, genre): 
        self.__genre = genre
    
    #method to set movie's producer
    def setProducer(self, producer): 
        self.__producer = producer
    
    #method to set movie's director
    def setDirector(self, director): 
        self.__director = director
    
    #method to set movie's production company
    def setProductionCompany(self, productionCompany): 
        self.__productionCompany = productionCompany
    
    #method to set 3 actors' name who starred in the movie
    def setActor1(self, actor1): 
        self.__actor1 = actor1
    
    def setActor2(self, actor2): 
        self.__actor2 = actor2

    def setActor3(self, actor3): 
        self.__actor3 = actor3

    #method to set the number of copies the store has
    def setCopiesNumber(self, copiesNumber):
        self.__copiesNumber = copiesNumber

    #method to get movie's name
    def getName(self): 
        return self.__name
    
    #method to get movie's genre
    def getGenre(self): 
        return self.__genre
    
    #method to get movie's producer
    def getProducer(self): 
        return self.__producer
    
    #method to get movie's director
    def getDirector(self): 
        return self.__director
    
    #method to get movie's production company
    def getProductionCompany(self): 
        return self.__productionCompany
    
    #method to get the name of the 3 actors who starred in the movie
    def getActor1(self): 
        return self.__actor1
    
    def getActor2(self): 
        return self.__actor2
    
    def getActor3(self): 
        return self.__actor3
    
    #method to get the number of copies the store has
    def getCopiesNumber(self):
        return self.__copiesNumber

    #str method to print the details of each dvd
    def __str__(self): 
        return f'Movie name: {self.__name}\n' + f'Genre: {self.__genre}\n' + f'Producer: {self.__producer}\n' + f'Director: {self.__director}\n' + f'Production company: {self.__productionCompany}\n' + f'Actors:\n' + f'{self.__actor1}\n' + f'{self.__actor2}\n' + f'{self.__actor3}\n' + f'Number of copies: {self.__copiesNumber}\n'
  
    #method to print all DVDs within the store along with the details
    def printDVDList():
        dvdLinkList.printNodeDetails()

    #method to print all movie title in store 
    def printTitles(): 
        print("\nAll movie titles in store:")
        for item in dvdLinkList.iterateNode():
            print(item.getName())
        print()

    #method to add new movies into the system (csv file and link list)
    def addNewDVD():
        dvdList = []
        name = input("Enter movie's name: ")
        genre = input("Enter movie's genre: ")
        producer = input("Enter movie's producer: ") 
        director = input("Enter movie's director: ") 
        productionCompany = input("Enter the movie's production company: ") 
        actor1 = input("Enter the name of the actor starring the movie: ")
        actor2 = input("Enter another name of the actor starring the movie: ")
        actor3 = input("Enter other name of the actor starring the movie: ")
        copiesNumber = input("Enter number of copies of the movie: ")
        dvd2 = dvdType(name, genre, producer, director, productionCompany, actor1, actor2, actor3, copiesNumber)
        
        #input data to the .csv file
        with open("listOfMovies.csv", 'a+') as file1:
                file1.write("\n" + name + ',')
                file1.write(genre + ',')
                file1.write(producer + ',')
                file1.write(director + ',')
                file1.write(productionCompany + ',')
                file1.write(actor1 + ',')
                file1.write(actor2 + ',')
                file1.write(actor3 + ',')
                file1.write(str(copiesNumber))
        
        #input data to linked list
        dvdLinkList.addNode(dvd2)
    
    #method for customer to return DVD
    def returnDVD(): 
        details = []
        temp = 0
        custId = input("Enter your ID: ")
        data = customerList.search(custId)
        #if the customer id is not found, it will loop until customer id is found
        while data == False:
            print("Enter a valid ID, this customer doesn't exist!")
            custId = input("Enter an ID:")
            customerList.search(custId)
            data = customerList.search(custId)
        #prompt user to verify who they are, if they accidetally input the wrong ID 
        verify = input("Is this you ? If yes, enter y\n")
        while verify != 'y':
            custId = input("Enter ID: ")
            data = customerList.search(custId)
            #if the customer id is not found, it will loop until customer id is found
            while data == False:
                print("Enter a valid ID, this customer doesn't exist!")
                custId = input("Enter an ID:")
                customerList.search(custId)
                data = customerList.search(custId)
            verify = input("Is this you ? If yes, enter y\n")
        movie = input("Enter name of movie you want to return: ")
        print()
        for item in dvdLinkList.iterateNode():
            if movie == item.getName():
                temp = int(item.__copiesNumber) 
                temp += 1
                item.__copiesNumber = temp
                print(item)
        print("Return DVD is successful!")
        

    #method to search dvd from linked list
    def searchTitle(movie):
        found = False
        for item in dvdLinkList.iterateNode():
            if movie == item.getName(): 
                found = True
                break
            else: 
                found = False
        if found == True: 
            print("Movie is found!")
            print("Movie name:", item.getName())
            print("Genre:", item.getGenre())
            print("Producer:", item.getProducer())
            print("Director:", item.getDirector())
            print("Production company:", item.getProductionCompany())
            print("Actors:")
            print(item.getActor1())
            print(item.getActor2())
            print(item.getActor3())
            print("Number of copies available: ", item.getCopiesNumber())
        elif found == False: 
            print("Movie is not found!")                    
        
#method for customer to rent DVDs
    def rentDVD(): 
        #ask user for customer ID
        custId = input("Enter ID: ")
        data = customerList.search(custId)
        #if the customer id is not found, it will loop until customer id is found
        while data == False:
            print("Enter a valid ID, this customer doesn't exist!")
            custId = input("Enter an ID:")
            customerList.search(custId)
            data = customerList.search(custId)
        #prompt user to verify who they are, if they accidetally input the wrong ID 
        verify = input("Is this you ? If yes, enter y\n")
        while verify != 'y':
            custId = input("Enter ID: ")
            data = customerList.search(custId)
            while data == False:
                print("Enter a valid ID, this customer doesn't exist!")
                custId = input("Enter an ID:")
                customerList.search(custId)
                data = customerList.search(custId)
            verify = input("Is this you ? If yes, enter y\n")
        #print all dvd titles 
        dvdType.printTitles()
        movie = input("Enter title of movie: ")
        #search for the title for the movie
        for item in dvdLinkList.iterateNode():
            if movie == item.getName(): 
                found = True
                break
            else: 
                found = False
        #print message if movie name is found
        if found == True: 
            print("Number of copies available:", item.__copiesNumber)
            if  int(item.__copiesNumber) > 0:
                item.__copiesNumber -= 1
                print("Renting movie is successful!")
            elif int(item.__copiesNumber) == 0:
                print("Sorry, the movie is out of stock!")
            else:
                print("Movie doesn't exist in store!\n")
            
    #method to update the stock of the movie 
    def updateMovieStock():
        movie = input("Enter the name of the movie: ")
        found = False    
        for item in dvdLinkList.iterateNode():
            if movie == item.getName(): 
                found = True
                break
            else: 
                found = False
        #print message if the movie is found in the link list
        if found == True: 
            stock = input("Enter number of stock: ")
            item.setCopiesNumber(stock)
            print("Number of copies successfully updated!")
            print("Number of copies:", item.getCopiesNumber())
        #print message if the movie is not found
        else: 
            print("Movie is not found! Please check the spellings of the title!")

#create the link list for dvd class
dvdLinkList = linkList()
#open the csv file and input the content of the file into a list
try:
    with open("listOfMovies.csv") as file1:
        dvdList = []
        for row in file1:
            row = row.strip("\n")
            column = row.split(",")
            name = column[0]
            genre = column[1]
            producer = column[2]
            director = column[3]
            productionCompany = column[4]
            actor1 = column[5]
            actor2 = column[6]
            actor3 = column[7]
            copiesNumber = int(column[8])
            dvd = dvdType(name, genre, producer, director, productionCompany, actor1, actor2, actor3, copiesNumber)
            dvdList.append(dvd) 
except Exception as e:
            print(e) 

#insert the value in the list into a link list
dvdLinkList.head = Node(dvdList[0])   
e2 = Node(dvdList[1])
e3 = Node(dvdList[2])
e4 = Node(dvdList[3])
e5 = Node(dvdList[4])
e6 = Node(dvdList[5])
e7 = Node(dvdList[6])
e8 = Node(dvdList[7])
e9 = Node(dvdList[8])
e10 = Node(dvdList[9])
e11 = Node(dvdList[10])
e12 = Node(dvdList[11])
e13 = Node(dvdList[12])
e14 = Node(dvdList[13])
e15 = Node(dvdList[14])
e16 = Node(dvdList[15])
e17 = Node(dvdList[16])
e18 = Node(dvdList[17])
e19 = Node(dvdList[18])
e20 = Node(dvdList[19])

#link each node to each other
dvdLinkList.head.next = e2
e2.next = e3
e3.next = e4
e4.next = e5
e5.next = e6
e6.next = e7
e7.next = e8
e8.next = e9
e9.next = e10
e10.next = e11
e11.next = e12
e12.next = e13
e13.next = e14
e14.next = e15
e15.next = e16
e16.next = e17
e17.next = e18
e18.next = e19
e19.next = e20
