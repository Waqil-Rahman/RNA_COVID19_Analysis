def split(text): #This function defines the 'split' function
    return list(text)
    #This list function turns a strings characters in a list
    #The function then returns the text with the characters separated into a list

string = 'hello'  #Assign a word to the string variable  
print (split(string)) #Testing if the function 'split' works with the string
#Output shows it works

str1 = open('sequence.txt','r') 
#This opens the text file 
#The r stands for read so when the text file is opened it is read
#This process of opening and reading the sequence.txt is assigned as str1

str2 = split(str1.read().replace('\n','')) 
#We first read through str1 and put it through the split function
#The replace in the above removes any newline characters from str1
#The replace works as a removing function as we replace any newline characters with nothing shown by ''
#Finally str2 is splitting str1
