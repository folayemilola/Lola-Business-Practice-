course = {'student': 'Lola', 'title': 'Practicing Dictionaries', 'supervisor' : 'Wajiw'}

#regular iteration
for item in course:
    print(course[item])
#the above prints out the value but not the keys 
    
#for accessing key value pairs printing both keys and their values
for item in  course.items():
    print(item)

#for printing each item in the dictionary wothout the quotation and without  pairing them as key value pairs 
    for key, value in course.items():
        print(key)
        print(value)

 #I can print keys separately and values separately 
