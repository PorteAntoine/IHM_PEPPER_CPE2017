import csv

fileobj = open('montreal/objects.csv','r') 
fileconcept = open('list_concept.top','w') 
objreader = csv.reader(fileobj, delimiter=';')
objects = []

for row in objreader:
	objects.append(row)

fileconcept.write('#Version 1.1\n\ntopic: ~topic_dialog_with_pepper()\n ### Concepts ###\n')

for i in range(1,len(objects[0])):
  fileconcept.write('\n\n\n### Concepts '+objects[0][i] +' ###\n')
  tampon=[]
  for j in range(1,len(objects)):
    if not objects[j][i] in tampon:
      tampon.append(objects[j][i])
      fileconcept.write('concept:('+objects[j][i].replace(' ','_') +') [ ')
      for k in range(1,len(objects)):
	if objects[k][i] == objects[j][i]:
	  if ' ' in objects[k][0]:
	    fileconcept.write('"'+objects[k][0] +'" ')
	  else:
	    fileconcept.write(objects[k][0] +' ')
      fileconcept.write(']\n')
