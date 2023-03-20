def mapping(x):
    x_N = [] #Start a new empty list
    for item in x: #This loop searches through the elements in x
        if item == ('A'): #When going through the elements in the list x it looks for 'A'
            x_N.append(int(-2)) #Replaces the string value 'A' and adds the integer -2 
        elif item == ('C'): #Same method as before but for the rest of the values now
            x_N.append(int(-1))
        elif item == ('G'):
            x_N.append(int(1))
        elif item == ('T'):
            x_N.append(int(2))
    return x_N #Returns the replaced letter-list into a number-list
x = str2[0:6] #Testing from str2
str2_map = print (mapping(x)) #Works

def walker(x):
    y=[0] #Intial value is given as y(0)=0
    for n in range (0,len(x)): #The loop will numerate until the end of the value of x which n-1 length
        y_new = y[n] + x[n] #This is the recursive equation adapted to the function
        y.append(y_new) #Generates the walk list and adds to the list of y values which will be n length
    return y #The function will now return the y list after going through the initial x list
x = [1,2,3,4] #Testing
print (walker(x)) #Works and proven by some simple mental arithmetic

def linear_fit(z):
    x_average = ((sum(x[0] for x in z))/len(z)) 
#Firstly we recall the 0th element which is the x-coordinates from list z
#Then sum up all the x-coordinates values 
#Then divide it by the number of coordinates in the list which is the same number of x values
#This would give us our average value of x and we do the same for the rest need to find 'a' 
    y_average = ((sum(y[1] for y in z))/len(z))
#Same as before but we choose [1] as that would give us y-coordinates values
    xy_average = ((sum((xy[0]*xy[1]) for xy in z))/len(z))
#Before we sum the equation we first multiply the 0th element and 1st element to get x*y to get xy average
    xsqr_average = ((sum((x[0]**2) for x in z))/len(z))
#Before we sum we square the x-coordinate values
    a = (xy_average -(x_average*y_average))/(xsqr_average-(x_average**2))
#Apply the formulae to find the gradient by recalling from our variable
    b = y_average - (a*x_average)
#Apply the formulae to find b by recalling from our variable
    return a,b

def linear_fit_test(z):
    a,b=np.polyfit(*zip(*z), 1)
    return a,b
#Use above function to test to see if our function work
z=[(2,4),(3,5),(5,7),(7,10),(9,15)]
#I choose these coordinates as the answers to them is on website I found to help with me understanding the least squares fit
#https://www.mathsisfun.com/data/least-squares-regression.html This is the website I used (30/04/2021)
print(linear_fit(z))
print(linear_fit_test(z))
#As we can see it functions and verified by 2 methods 

def linear_trend(z):
    coordinates = list(enumerate(z)) 
#This takes in the list and indexes it into a tubule 
    a = linear_fit(coordinates)[0] 
#This takes the first value from list z and puts it through the linear_fit function
    b = linear_fit(coordinates)[1]
#This takes the second value from list z and puts it through the linear_fit function
    y = []
#Start a new empty list
    for i in range(len(coordinates)): 
        y.append(a*i+b)
#This makes the new list the length of list z
#This adds the new coordinates into the linear trend into the list
    return y

z = [(2,4),(3,5),(5,7),(7,10),(9,15)] #Testing from the previous question
z1 = (linear_fit(z)) #Use the previous example’s answer to make sure it’s the same length 
print (linear_trend(z1)) # We can see that the function works

virus_walk = walker(mapping(str2)) #This is the virus_walk plot labelled in blue on the graph
best_fit = linear_trend(walker(mapping(str2))) #This is the straight line fit given from previous functions
plt.plot(virus_walk) #Using the plot function we can plot the graph
plt.plot(best_fit)  #Using the plot function we can plot the graph
plt.ylim(-200,2200) # We can adjust the axis to fit the graph
plt.xlim(-500,31000)
plt.show() #This plots the first graph with the first two functions
ap = linear_trend(virus_walk) #This creates the (ap+b) element of the detrended_virus_walk
detrended_virus_walk = [] #We need to create a new empty list for the detrended_virus_walk graph points
for p in range(0,len(virus_walk)): 
#We use this to make sure the length of detrended_virus_walk is the same as virus_walk 
#Also this ensures we use the same p-th element during the subtraction  
    detrended_virus_walk.append(virus_walk[p]- ap[p])
#We implement the new detrended_virus_walk formalae into the append to fill in the empty list with new elements
#This adds new coordinates into the detrended_virus_walk into the list
plt.plot(detrended_virus_walk) #Using the plot function we can plot the graph
plt.show()#This plots the second graph

y_1=[random.choice([-2,2]) for i in range(len(virus_walk))] 
#We are using the function random.choice to generate random numbers between {-2,2}
#We keep on generating this random list until it is the length of virus_walk
#We choose virurs_walk as it is the same length as walker(mapping(str2)) established from [2.5] code
plt.plot(walker(y_1),color='red',label = 'Random 1') 
#We now plot the walker random graph using the function of walkers and input the random number list into it
#I also assign a colour to it and label so we can identity which line is which
#Now we repeat 5 times
y_2=[random.choice([-2,2]) for i in range(len(virus_walk))]
plt.plot(walker(y_2),color='blue', label = 'Random 2') 
y_3=[random.choice([-2,2]) for i in range(len(virus_walk))]
plt.plot(walker(y_3),color='purple', label = 'Random 3') 
y_4=[random.choice([-2,2]) for i in range(len(virus_walk))]
plt.plot(walker(y_4),color='yellow', label = 'Random 4') 
y_5=[random.choice([-2,2]) for i in range(len(virus_walk))]
plt.plot(walker(y_5),color='green', label = 'Random 5') 
plt.plot(detrended_virus_walk,color='black', label = 'Detrended')
#We now plot the detrended_virus_walk and assign the label 'Detrended' to it
plt.legend(frameon=False,loc='upper center', ncol=3)
#I have inserted the legend for the graph so it is easy to read
#Using the function of the legend, I've placed it in a place of the graph so it is out of the way and easily read
