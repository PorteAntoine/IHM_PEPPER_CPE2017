import csv
fileobj = open('montreal/objects.csv','r')
filepers = open('montreal/list_person_final.csv','r')
fileloc = open('montreal/locations.csv','r')
#creation des listes de cles pour chacuns des csv independamment de la question
objreader = csv.reader(fileobj, delimiter=';')
persreader =  csv.reader(filepers, delimiter=';')
locreader = csv.reader(fileloc, delimiter=',')
objects = []
persons = []
locations= []
keys = []
keysp = []
keysl = []

for row in locreader:
    locations.append(row)
l1=0
for i in range(len(locations)):
    if len(locations[i])>l1:
        l1 = len(locations[i])
l2 = i
for row in objreader:
    objects.append(row)
m1=0
for i in range(len(objects)):
    if len(objects[i])>m1:
        m1 = len(objects[i])
m2 = i
for row in persreader:
    persons.append(row)
p1=0
for i in range(len(persons)):
    if len(persons[i])>p1:
        p1 = len(persons[i])
p2 = i

def compare_keys(s1,s2):

    for i in range(1,len(objects)):
        for j in range(len(objects[0])):
            if objects[i][j] in s1:
                if not objects[i][j] in s2:
                    return False
    for i in range(1,len(persons)):
        for j in range(len(persons[0])):
            if persons[i][j] in s1:
                if not persons[i][j] in s2:
                    return False
    for i in range(1,len(locations)):
        for j in range(len(locations[0])):
            if locations[i][j] in s1:
                if not locations[i][j] in s2:
                    return False
    for i in range(1,len(objects)):
        for j in range(len(objects[0])):
            if objects[i][j] in s2:
                if not objects[i][j] in s1:
                    return False
    for i in range(1,len(persons)):
        for j in range(len(persons[0])):
            if persons[i][j] in s2:
                if not persons[i][j] in s1:
                    return False
    for i in range(1,len(locations)):
        for j in range(len(locations[0])):
            if locations[i][j] in s2:
                if not locations[i][j] in s1:
                    return False
    return True