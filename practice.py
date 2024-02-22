# Difference between  lists and Tuples 

#Tuple 
person_a = ('name' , '18', 'Seneca', 'Chicago') # or without the poarenthesis 

#List 
Seneca = ['Jaime', 'Lola', 'Arai', 'Aria' 'Ethan']

# to access a syntax in a tuple 
person_a[2] # to access the third person in the syntax

# python for loop
my_name = "Lola"
for letter in my_name:
    print (letter)

    # learning about enumerate 
    groceries = ['roast beef', 'bread', 'water']
    for index, item in enumerate(groceries, 1):
        print (f'{index}. {item}')

    # write a for loop  that loops over the list and prints the current items in the list 
        rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        for color in rainbow:
         print(color)

    #Edit the code so that the for loop uses the enumerate method. 
     #Add a print statement above the existing print statement that prints the index of the current element.
        for index, color in enumerate(rainbow):
          print("Index:", index)
          print("Color:", color)


    #Range 
          #Range takes in 3 arguments 
          #Range is like a regular for loop
          for i in range (10): #this makes the range go from 0-9
             print(i)

        #For ranges that start at a specific index 
             for i in range (5,10):
                print(i)

 #Write a for loop that iterates over a range with a stop value of 10 (assume the start value is 0 and the step value is 1).
#The body of the for loop should append the current value to the provided list called my_list.
#To append a value to a list, use the syntax my_list.append(val).
my_list = []

for i in range(10):
    my_list.append(i)

#Sequence operation
    
    #SLICES 
# It crops out  a section in a list and only prints the elements inbetween the  indeces selected 
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

#slice example 
rainbow[1:4] # this will print out orange, yellow and green

rainbow[3:] #prints out 3rd index all the way untol the end 

rainbow [::2] # prints out every other element 

rainbow [::-1] #prints out index in reverse 

#slices working with strings 
my_name = Damilola 

my_name[:4] # prints out Dami 

my_name [4:] #prints out Lola

nums = (1,2,3,4,5,6,7,8,9,10)
len(nums) # returns the length of an object

max(nums) # returns the maximum value 

min(nums) # returns the minimum value

# how to write if statement 
docs = 'tuple is tuple'
if 'tuple' in docs:
   print('tuple')
else: 
   print('')

#METHODS
   #count method 
docs = ('Tuples are immutable sequences, typically used to store collections of heterogeneous data '
        '(such as the 2-tuples produced by the enumerate() built-in). '
        'Tuples are also used for cases where an immutable sequence of homogeneous data is needed '
        '(such as allowing storage in a set or dict instance).')

print(docs.count('tuple')) # counts how many times tuple appears in the above sentence 
                           # However this is an exact match 

 
    
#index method 
teachers = ['Aleana', 'Ashley', 'Nicole', 'Treasure']

print(teachers.index('Nicole')) #this will return 2 because Nicole is at index 2 and the 3rd element in the list 
                                # this will also return 2 if Nicole is repeated again in the list because it gives the index of 
                                # the first time the element appears in the list 
                                # if Nicole was not in the list, it would give a value error 

#CONCATENATION
object1 = [1,2,3,4,5]
object2 = [6,7,8,9,10]

object1 = object1 + object2

#REPETITION
str = 'python'

print(str*5) # prints str 5 times, might wanna add spacing 

 