<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Authors: David Redondo & Mariano Álvarez

This simple script lets show a quick view about how to work
with csv format
"""
import csv

# Let's read a csv file from the directory
with open('mycsvfile.csv') as csvfile:
    file = csv.reader(csvfile)
# Now we are iterating over the file to show all
# through the console
    for row in file:
        print(', ', row)
print('')
# In case we want to write to a csv file, we will use
# the method: write()

with open('mycsvfile.csv', 'w', newline='') as csvfile:
    file = csv.writer(csvfile)
    file.writerow(["SN", "Movie", "Protagonist"])


# Through the method 'writerows' we are able to
# write multiple rows with a only one method

csv_rowlist = [[1, "Lord of the Rings", "Frodo Baggins"],
               [2, "Harry Potter", "Harry Potter"]]

with open('mycsvfile.csv', 'w', newline='') as csvfile:
    file = csv.writer(csvfile)
    file.writerows(csv_rowlist)
    
with open('mycsvfile.csv') as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        print(', ', row)
        
print('')

# In addition, we can define headers, they are pretty usuful as we will see:
fieldnames = ["SN", "Movie", "Protagonist"]

# Opening the file again:

with open("mycsvfile.csv", 'w', newline='') as csv_file:
    
    csv_file = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_file.writeheader()
    csv_file.writerow({'SN': 1, 'Movie': 'Interstellar',
                      'Protagonist': 'Joseph Cooper'})
    
# Notice that we are writting over all the object, so the things that we have already written
# will be replaced by new data    
with open('mycsvfile.csv') as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        print(', ', row)
=======
# -*- coding: utf-8 -*-
"""
Authors: David Redondo & Mariano Álvarez

This simple script lets show a quick view about how to work
with csv format
"""
import csv

# Let's read a csv file from the directory
with open('mycsvfile.csv') as csvfile:
    file = csv.reader(csvfile)
# Now we are iterating over the file to show all
# through the console
    for row in file:
        print(', ', row)
print('')
# In case we want to write to a csv file, we will use
# the method: write()

with open('mycsvfile.csv', 'w', newline='') as csvfile:
    file = csv.writer(csvfile)
    file.writerow(["SN", "Movie", "Protagonist"])


# Through the method 'writerows' we are able to
# write multiple rows with a only one method

csv_rowlist = [[1, "Lord of the Rings", "Frodo Baggins"],
               [2, "Harry Potter", "Harry Potter"]]

with open('mycsvfile.csv', 'w', newline='') as csvfile:
    file = csv.writer(csvfile)
    file.writerows(csv_rowlist)
    
with open('mycsvfile.csv') as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        print(', ', row)
        
print('')

# In addition, we can define headers, they are pretty usuful as we will see:
fieldnames = ["SN", "Movie", "Protagonist"]

# Opening the file again:

with open("mycsvfile.csv", 'w', newline='') as csv_file:
    
    csv_file = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_file.writeheader()
    csv_file.writerow({'SN': 1, 'Movie': 'Interstellar',
                      'Protagonist': 'Joseph Cooper'})
    
# Notice that we are writting over all the object, so the things that we have already written
# will be replaced by new data    
with open('mycsvfile.csv') as csvfile:
    file = csv.reader(csvfile)
    for row in file:
        print(', ', row)
>>>>>>> 94cc937c85286f9ae8e1f0ecb5cd73312d4a6149
