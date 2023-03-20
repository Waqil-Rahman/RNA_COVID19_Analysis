def freq(virus_sequence_list):
#Using the mapping module we count the frequency by counting the number of -2's and etc. in each list
#We store the separate frequencies in its respected variable
#We repeat this for A,C,G,T
    freq_A = mapping(virus_sequence_list).count(-2)
    freq_C = mapping(virus_sequence_list).count(-1)
    freq_G = mapping(virus_sequence_list).count(1)
    freq_T = mapping(virus_sequence_list).count(2)
    return [freq_A,freq_C,freq_G,freq_T]
nucleotides = ['A','C','G','T']
#We arrange the nucleotides in alphabetical order 
plt.bar(nucleotides,freq(str2),color='blue')
#We create the bar plot graph and ensure the colour of the bars are blue
plt.ylabel('Frequncey')
plt.xlabel('Nucleotides')
plt.show()
print (freq(str2))

def freq_2(x):
    AA=AC=AG=AT=CA=CC=CG=CT=GA=GC=GG=GT=TA=TC=TG=TT=0
    #We make all the  possible combinations in the string equal zero from when we start counting
    for i in range(len(x)-1):
    #The loop will go through the entire list x
        if x[i] == 'A':
    #When going through the list we find the 'A' the following happens:
            if x[i+1] == 'A':
    #If the next element in the list is another 'A' we add 1 to the list of AA combinations
                AA = AA+1
            elif x[i+1] == 'C':
                AC = AC+1
    #If the next letter is not A but it is C we add 1 to the AC list
    #We carry on with this to cover all combinations
            elif x[i+1] == 'G':
                AG = AG+1
            else:
                AT = AT+1
    #We use else here as the only other option is the AT combination and we need to end this loop search
        elif x[i] == 'C':
            if x[i+1] == 'A':
                CA = CA+1
            elif x[i+1] == 'C':
                CC = CC+1
            elif x[i+1] == 'G':
                CG = CG+1
            else:
                CT = CT+1
        elif x[i] == 'G':
            if x[i+1] == 'A':
                GA = GA+1
            elif x[i+1] == 'C':
                GC = GC+1
            elif x[i+1] == 'G':
                GG = GG+1
            else:
                GT = GT+1
        else:
        #We use else here as the only other option is the T combinations and we need to end this loop search
            if x[i+1] == 'A':
                TA = TA+1
            elif x[i+1] == 'C':
                TC = TC+1
            elif x[i+1] == 'G':
                TG = TG+1
            else:
                TT = TT+1
    nucleotides_combination = ('AA','AC','AG','AT','CA','CC','CG','CT','GA','GC','GG','GT','TA','TC','TG','TT')
    sequence_freq_2 = (AA,AC,AG,AT,CA,CC,CG,CT,GA,GC,GG,GT,TA,TC,TG,TT)
    sequence_2 = dict(zip(nucleotides_combination,sequence_freq_2))
#This dictionary function puts all the combinations together 
#This is able to sort the count value to each respective combination in the list 
#As a result it is easy to read what the frequency is of each combination
    return sequence_2

plt.bar(freq_2(str2).keys(),freq_2(str2).values())
#We create the bar plot graph
plt.xlabel("Nucleotides Combinations")
plt.ylabel("Frequencies")
plt.show()
#This shows the values of each combination
print (freq_2(str2)) 
#Our dictionary function is put into work as we can see it from the output

all_combinations_value = list(freq_2(str2).values()) 
#This changes the freq_2 returns (sequence_2) into a list of only values
total_nucleotides_value = list(freq(str2)) 
#This gets the total number of nucleotides and puts it into a list
#We do the above to calculate the different values in the matrix
T_AA = (all_combinations_value[0]/total_nucleotides_value[0])
T_AC = (all_combinations_value[1]/total_nucleotides_value[0])
T_AG = (all_combinations_value[2]/total_nucleotides_value[0])
T_AT = (all_combinations_value[3]/total_nucleotides_value[0])
T_CA = (all_combinations_value[4]/total_nucleotides_value[1])
T_CC = (all_combinations_value[5]/total_nucleotides_value[1])
T_CG = (all_combinations_value[6]/total_nucleotides_value[1])
T_CT = (all_combinations_value[7]/total_nucleotides_value[1])
T_GA = (all_combinations_value[8]/total_nucleotides_value[2])
T_GC = (all_combinations_value[9]/total_nucleotides_value[2])
T_GG = (all_combinations_value[10]/total_nucleotides_value[2])
T_GT = (all_combinations_value[11]/total_nucleotides_value[2])
T_TA = (all_combinations_value[12]/total_nucleotides_value[3])
T_TC = (all_combinations_value[13]/total_nucleotides_value[3])
T_TG = (all_combinations_value[14]/total_nucleotides_value[3])
T_TT = (all_combinations_value[15]/total_nucleotides_value[3])
matrix_T = np.array([[T_AA,T_AC,T_AG,T_AT],
            [T_CA,T_CC,T_CG,T_CT],
            [T_GA,T_GC,T_GG,T_GT],
            [T_TA,T_TC,T_TG,T_TT]])
#We use the array function to display the matrix as an actual matrix in python
print('First T row matrix total:', (np.sum([T_AA,T_AC,T_AG,T_AT])))
print('Second T row matrix total:', (np.sum([T_CA,T_CC,T_CG,T_CT])))
print('Thrid T row matrix total:', (np.sum([T_GA,T_GC,T_GG,T_GT],)))
print('Forth T row matrix total:', (np.sum([T_TA,T_TC,T_TG,T_TT])))
#We do the above to ensure the matrix is correct as all values should be 1 or close to 1
print(matrix_T)
heat_map = seaborn.heatmap(matrix_T,annot=True)
#We use the seaborn module to output a heatmap 
#We use the annotations in the heatmap function and set as True to see the values in the heatmap
plt.show()
#We use the above function to plot the values of matrix_T as a heatmap
eval_A,evec_A=la.eig(matrix_T)
#We use the above function to calculate eigenvalues of matrix_T
print("The eigenvalues are:", eval_A)
print("The largest eigenvalue of matrix_T is:", str(max(eval_A)))
print("This is close to 1")
print(str(matrix_T@evec_A[:,0]),"Tv is the is the same as v")

def deviation(x):
    k_list = [] #First we need the empty k_list to put in values from list x
    for i in range(0,len(x)): #We go through the list from the start till the length of list x is reached (Loop)
        k = np.power(2,i) 
#We get the value i from list x and check if it is a power of 2 
#If it is an integer we store the value in k 
        if k>(len(x)-1): #If the k value is larger than the list's x length then we stop the loop
            break 
        delta_k = np.max(x[:k+1])-np.min(x[:k+1])
#We use the above to calculate the change in k from the formalae in the question
        k_list.append((k,delta_k))
#We add all the needed data into the k_list by using the append function
    return k_list
#Now the function will output the needed data

x = [0,1,2,3,4,5,6,7,8] #Testing
print (deviation(x)) #Works
x = [1,1,1,1] #Testing
print (deviation(x)) #Works

r_1=[random.choice([-2,2]) for i in range(len(virus_walk))] 
#As from previous questions we need to generate a random walk path
#Look back at [2.6] code to see the full explanation and code
l_1 = (deviation(walker(r_1)))
#We implement the deviation function onto the walk
x_1,y_1=map(list,zip(*l_1))
#This map fuction seperates all the sublists  
#This is able to sort the x and y into each respective list 
print("This shows our cooridinates:",l_1)
print("This shows our x-cooridinates:",x_1)
print("This shows our y-cooridinates:",y_1)
print('Therefore from above we can verify our coordinates work to put into a scatter graph')
#From above we can verify our new map function works and is now ready to be inputted into a scatter graph
plt.scatter(x_1,y_1,color='red',label = 'Random 1')
#Repeat this 5 times
r_2=[random.choice([-2,2]) for i in range(len(virus_walk))] 
l_2 = (deviation(walker(r_2)))
x_2,y_2=map(list,zip(*l_2))
plt.scatter(x_2,y_2,color='blue',label = 'Random 2')
r_3=[random.choice([-2,2]) for i in range(len(virus_walk))] 
l_3 = (deviation(walker(r_3)))
x_3,y_3=map(list,zip(*l_3))
plt.scatter(x_3,y_3,color='green',label = 'Random 3')
r_4=[random.choice([-2,2]) for i in range(len(virus_walk))] 
l_4 = (deviation(walker(r_4)))
x_4,y_4=map(list,zip(*l_4))
plt.scatter(x_4,y_4,color='purple',label = 'Random 4')
r_5=[random.choice([-2,2]) for i in range(len(virus_walk))] 
l_5 = (deviation(walker(r_5)))
x_5,y_5=map(list,zip(*l_5))
plt.scatter(x_5,y_5,color='yellow',label = 'Random 5')
#Now we do the same thing but for the detrended_virus_walk
l = (deviation(detrended_virus_walk))
x_detrended,y_detrended=map(list,zip(*l))
plt.scatter(x_detrended,y_detrended,color='black',label = 'Detrended')
plt.yscale('log')#This ensures the y-axis is logarithmic  
plt.xscale('log')#This ensures the x-axis is logarithmic  
plt.legend(frameon=False,loc='upper left')
#I use the legend to show what point is what 
#I've also put the location from 'loc' into the 'upper left' to make sure the legend isn't in the way of the data points
plt.show()

coordinates = list(zip(np.log(x_detrended),np.log(y_detrended)))
#The above takes the x-coordinates and y-coordinates of the deviated detrended_virus_walk
#We put back the log10() into the coordinates as it was removed from the previous [3.5] code
#The zip combines each x and y together to the correct pairing (ensures the coordinates are unchanged)
#The list turns the zip format into a form we can work with
A = np.exp(linear_fit(coordinates)[1])
B = linear_fit(coordinates)[0]
#We use the above formulas to calculate the power_law function
#We use the linear_fit function respectively on all x and y coordinates
power_law = [(A)*(i**B) for i in x_detrended]
#We use the above formulas to calculate the power_law fucntion by recalling on our named variables
print('A=',A,"B=",B)
#The above shows the values of both A and B
plt.scatter(x_detrended,y_detrended,label='Deviated Detrended virus walk')
#We use the scatter function to plot all the points of the Deviated detrended virus walk
#I ensure the colour of the points is set to make it different to the Power Law Function line
plt.xscale('log') #This ensures the x-axis is logarithmic  
plt.yscale('log') #This ensures the y-axis is logarithmic  
plt.plot(x_detrended,power_law,label='Power Law Function',color='red')
#We use the plot function to plot the Power Law Function
#I ensure the colour of the line is set to make it different to the Deviated detrended virus walk points
plt.legend(loc='upper left')
#I use the legend to show what point is what 
#I've also put the location from 'loc' into the 'upper left' to make sure the legend isn't in the way of the data points
plt.show()
