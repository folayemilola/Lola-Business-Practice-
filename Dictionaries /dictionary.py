#dictionaries and key value pairs
#dictionaries are meant for organization

course = {'student': 'Lola', 'title': 'Practicing Dictionaries', 'supervisor' : 'Wajiw'}

#course = {'supervisor' : 'Wajiw', 'Gates', 'Mo'}
# key value pairs cannopt have more than value 
print(course['supervisor'])
print(course.keys()) # calls all the key value pairs in the dictionary
print(course)

#changing the value of the key value pair
course['student']= 'Lola Folayemi'
course['title'] = 'Seneca scholar'
print (course)


#adding a new key value pair 
course['music'] = 'Candy by Doja cat'
print (course)

#deleting key value pairs 
del(course['title'])
print(course)

#key value pairs with numbers do not need quotations over numbers

