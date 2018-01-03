
#-------------------------------------------------

# This fucntion gets the file
def openFile():
    #enter name of file
    goodFile = False
    while goodFile == False:
        fname = input("Enter name of data file: ")

        # Begin exception handling
        try:
            # Try to open the file using the name given
            airlineFile = open(fname, 'r')
            # If the name is valid, set Boolean to true to exit loop
            goodFile = True
        except IOError:

            # If the name is not valid - IOError exception is raised
             print("Invalid filename, please try again ... ")


    return airlineFile

#This function gets the data from the file and turns them into lists 
def getInfo():
    #Open file using the previous openfile function
    infile = openFile()

    #Initialize Lists
    airlineList = []
    flightNumberList = []
    dTimeList = []
    aTimeList = []
    priceList = []
 
    line = infile.readline()

    # make loop to go through lines and add data to lists
    while line != "":
        line = line.strip()
        airline , flightNumber , dTime , aTime , price = line.split(",")
        airlineList = airlineList + [airline]
        flightNumberList = flightNumberList + [flightNumber]
        dTimeList = dTimeList + [dTime]
        aTimeList = aTimeList + [aTime]
        priceList = priceList + [price]
        line = infile.readline()
    infile.close()
 
    #return the lists
    return airlineList , flightNumberList , dTimeList , aTimeList, priceList


#This function makes a list of options for the user to choose from
def Menu():
    #set the options for the user as print statements
    print("")
    print("Please choose one of the following options:")
    print("1 - Find all the flights on a particular airline")
    print("2 - Find the cheapest flight")
    print("3 - Find all flights less than a specified price")
    print("4 - Find the shortest flight")
    print("5 - Find all flights that depart withtin a specified range")
    print("6 - Find the average price for a specified airline")
    print("7 - Quit")

    #asks user to pick an option and puts it in a variable 
    choice = input("Enter your choice --> ")
    try:
        choice = int(choice)
    except ValueError:
        print("Could not convert input to an interger.")
    print("")

    #returns the variable also known as the choice of the user
    return choice

#This function finds all the flights in a particular airline
def findFlight(airlineList , flightNumberList , dTimeList , aTimeList, priceList,airlineSearch):
    print("These flights match your criteria")
    #Loops through airline list
    for i in range(len(airlineList)):
        #Checks if airline searching for matches the one in list 
        if airlineSearch == airlineList[i]:
            #returns the data 
            print(airlineList[i] ,"Flight Number" , flightNumberList[i] , "Departure Time", dTimeList[i], "Arrival Time" , aTimeList[i] , priceList[i])
                  
#This function finds the cheapest flight
def cheapFlight(airlineList , flightNumberList , priceList):
    # sets lowest price to first price 
    lowestPrice = priceList[0]
    flightNumber = flightNumberList[0]
    airline = airlineList[0]
    
    # loop through and compare values to the lowest
    for i in range(len(priceList)):

        #if price is lower set found price as lowest and the indexs the same as lowest
        if priceList[i]<lowestPrice:
            lowestPrice = priceList[i]
            flightNumber = flightNumberList[i]
            airline = airlineList[i]
    print("The cheapest flight is", airline , flightNumber ,"at", lowestPrice)

#This function finds all the flights less than a certain price
def flgihtsLow(maxPrice, airlineList , flightNumberList , dTimeList , aTimeList, priceList):
    
    print("These flights match your criteria")
# loop price list if price is less than input price
    for i in range(len(priceList)):
        if priceList[i]< maxPrice:
            print(airlineList[i] ,"Flight Number" , flightNumberList[i] , "Departure Time", dTimeList[i], "Arrival Time" , aTimeList[i] , priceList[i])


#This function finds the shortest flight
def shortestFlight(dTimeList , aTimeList, airlineList , flightNumberList):
    #Initialize lists
    newList = []
    newList2 = []
    newList3 = [] 

    #removes : from departure list items   
    for i in range(len(dTimeList)):
        item = dTimeList[i]
        front , back = item.split(":")
        new = front+back
        #turns to an int and adds to new list1
        new = int(new)
        newList.append(new)
    #removes : from arrival list items
    for j in range(len(aTimeList)):
        item2 = aTimeList[j]
        front2 , back2 = item2.split(":")
        new2 = front2+back2
        #turns to int and adds to new list2
        new2 = int(new2)
        newList2.append(new2)
    #subtracts the departure time from arrival times and puts value in new list
    for k in range(len(newList)):
        item3 = newList2[k] - newList[k]
        newList3.append(item3)

    #initilizes variables
    shortest = newList3[0]
    flightNumber = flightNumberList[0]
    airline = airlineList[0]
    # loops through list 3 to find index's of lists with shortest flight duration
    for l in range(len(newList3)):
        if newList3[l]<shortest:
            shortest = newList3[l]
            flightNumber = flightNumberList[l]
            airline = airlineList[l]
    #uses change function to convert the flight duration to minutes
    shortest = change(shortest)
    
    print("The shortest flight is", airline , flightNumber ,"at", shortest)
#this function takes shortest and turn it into a value in minutes 
def change(shortest):
    #changes shortest to string
    shortest = str(shortest)
    #initializes variables
    value = 0
    value2 = 0
    v1 = 0
    v2 = 0
    v3 = 0 

    #loops through characters of shortest
    for i in range(len(shortest)):
        # stores each character as a variable
        hi = shortest[i]
        #takes first number and multiplys by 60
        if hi == shortest[0]:
            hi = int(hi)
            hi = 60*hi
            value = hi
        #takes second number and stores in variable 
        elif hi == shortest[1]:
            v1 = hi
        #takes third number and stores in variable
        elif hi == shortest[2]:
            v2 = hi
    #combines combines the second 2 variables
    v3 = v1 + v2
    v3 = int(v3)
    #add second 2 variables to first number 
    value2 = value + v3
    #return the shortest in minutes 
    return value2
         
#This function finds flights that depart in a specified range
def findTime(airlineList , flightNumberList , dTimeList , aTimeList, priceList):
    #intilizes lists and variables
    list2 = []
    list1 = dTimeList
    new=0 
    #asks user to input high and low ranges
    lowRange = input("input low range: ")
    highRange = input("highrange")
    # takes high and low ranges, takes out the ':' and turnes them to integers  
    front1 , back1 = lowRange.split(":")
    front2 , back2 = highRange.split(":")
    lowRange1 = int(front1+back1)
    highRange1 = int(front2 + back2)
    #loops throught departure time list and removes ':' and adds to new list
    for i in range(len(list1)):
        yo = list1[i]
        front , back = yo.split(":")
        new = front+back
        new = int(new)
        list2.append(new)
    #loops through the new list and finds all the flights in the specified range
    for k in range(len(list2)):
        if list2[k]>lowRange1 and list2[k]<highRange1:
            print(airlineList[k] , flightNumberList[k] , dTimeList[k] , aTimeList[k], priceList[k])

#This function finds average price for a speficied airline
def findAvg(airlineName,airlineList, priceList):
    #intilize sum
    suM= 0
    denom = 0
    list1 = []
    avg = 0
    
    # loop through airline list
    for i in range(len(priceList)):
        sign, price = priceList[i].split("$")
        price = int(price)
        #adds price to new list 
        list1.append(price)
    #loops through airlinelist and uses the index of the flights that match to the price to the sum
    for j in range(len(airlineList)):
        if airlineName == airlineList[j]:
            suM = suM + list1[j]
            #increments the denominator
            denom = denom+1
    #computes average
    print(suM/denom)


def m():
    #gets lists
    airlineList , flightNumberList , dTimeList , aTimeList, priceList = getInfo()
    print(airlineList , flightNumberList , dTimeList , aTimeList, priceList)
    #starts the menu and performs the above functions based on the choice the user picks 
    choice = Menu()
    if choice == 1:
        airlineSearch = input("Enter Flight to search for: ")
        flight = findFlight(airlineList , flightNumberList , dTimeList , aTimeList, priceList,airlineSearch)
        print(flight)
    elif choice ==  2:
        cheapestFlight = cheapFlight(airlineList , flightNumberList , priceList)
        print(cheapestFlight)
    elif choice == 3:
          maxPrice = input("enter price starting with a $ ")
          lowFlights = flgihtsLow(maxPrice, airlineList , flightNumberList , dTimeList , aTimeList, priceList)
          print(lowFlights)
    elif choice == 4:
        shortFlight = shortestFlight(dTimeList , aTimeList,airlineList , flightNumberList)
        print(shortFlight)
    elif choice == 5:
        dFlights = findTime( airlineList , flightNumberList , dTimeList , aTimeList, priceList)
        print(dFlights)
    elif choice == 6:
        airlineName = input("Enter name of airline: ")
        avg = findAvg(airlineName, airlineList, priceList)
        print(avg)
    elif choice == 7:
        print("Good-bye")
        
    
                  

                  
                      
                  


