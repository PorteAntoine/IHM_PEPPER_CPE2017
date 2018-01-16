import csv

fileobj = open('montreal/objects.csv','r') 
filekey = open('keys.csv','r')
fileanswer = open('answers.txt','w')

objreader = csv.reader(fileobj, delimiter=';')
keyreader = csv.reader(filekey, delimiter=',')

objects = []
keys =  [] 
for row in objreader:
	objects.append(row)
for row in keyreader:
	keys.append(row)

m1=0

for i in range(len(objects)):
	if len(objects[i])>m1:
		m1 = len(objects[i])
m2 = i	

for i in range(0,len(keys)-1):
  if keys[i][len(keys[i])-1] is '':
    keys[i].pop()
    
prefix=['do','heavier','lighter','smaller','bigger','heaviest','lightest','smallest','biggest','which','where','what','how many']

def what(keys):
  v=0
  c=0
  p=0
  for i in range(0,len(keys)):
    if keys[i] == keys[i].lower():
      v+=1
      values.append(keys[i])
      #print(keys[i])
    elif keys[i] == keys[i].upper() and keys[i] != 'WHAT':
      p+=1
      pref.append(keys[i])
    elif keys[i] != 'WHAT':
      c+=1
      categ.append(keys[i])
      #print(keys[i])
    if v==1 and c==1 and p==0:
      for j in range(len(objects[0])):	
	if categ[0] == objects[0][j]:
	  for index in range(len(objects)):
	    if values[0] in objects[index] :
	      fileanswer.write('The ' + objects[0][j] + ' of the ' + objects[index][0] + ' is ' +objects[index][j] + '\n')

def howmany(keys):
  v=0
  c=0
  p=0
  for i in range(0,len(keys)):
    if keys[i] == keys[i].lower():
      v+=1
      values.append(keys[i])
      #print(keys[i])
    elif keys[i] == keys[i].upper() and keys[i] != 'HOW MANY':
      p+=1
      pref.append(keys[i])
    elif keys[i] != 'HOW MANY':
      c+=1
      categ.append(keys[i])
      #print(keys[i])
    if v>0 :
     
      counter =0
      for index in range(len(objects)):	
	belong = True
	for index2 in range(len(values)):
	  if not values[index2] in objects[index]:
	    belong = False
	if belong == True:
	  counter+=1
  fileanswer.write('There are ' + str(counter)+ ' items belonging to the ')
  for p in range(len(values)):
    fileanswer.write(values[p])
  fileanswer.write(' category\n')
  
def do(keys):
  v=0
  c=0
  p=0
  for i in range(0,len(keys)):
    if keys[i] == keys[i].lower():
      v+=1
      values.append(keys[i])
      #print(keys[i])
    elif keys[i] == keys[i].upper() and keys[i] != 'DO':
      p+=1
      pref.append(keys[i])
    elif keys[i] != 'DO':
      c+=1
      categ.append(keys[i])
      #print(keys[i])
    counter =0
    valors=[]
  if v==2:
    for cat in range(len(objects[0])):
      if objects[0][cat] in categ:
        valors.append(cat)
    belong = True
    for k in range(len(valors)):
	storage= []
	for index in range(len(objects)):
	  if objects[index][0] in values : 
	    storage.append(objects[index][valors[k]])
	    for s in range(len(storage)):
	      if not storage[s] == storage[0] :
		belong = False
	if belong == False:
	  break
    if belong == True:
      fileanswer.write('That is correct, '+ values[0] + ' and ' + values[1] + ' belong to the same category\n')
    else:
      fileanswer.write('Incorrect, '+ values[0] + ' and ' + values[1] + ' do not belong to the same category\n')
  
  
def where(keys):
  v=0
  c=0
  p=0
  for i in range(0,len(keys)):
    if keys[i] == keys[i].lower():
      v+=1
      values.append(keys[i])
  for j in range(len(values)):
    for i in range(len(objects)):
      if objects[i][0] == values[j]:
	fileanswer.write('the ' + objects[i][0] + ' is in the '+objects[i][3]+ ' which is located in the ' + objects[i][4]+'\n')
   
def which(keys):
  v=0
  c=0
  p=0
  for i in range(0,len(keys)):
    if keys[i] == keys[i].lower():
      v+=1
      values.append(keys[i])
      #print(keys[i])
    elif keys[i] == keys[i].upper() and keys[i] != 'WHICH':
      p+=1
      pref.append(keys[i])
    elif keys[i] != 'WHICH':
      c+=1
      categ.append(keys[i])
      #print(keys[i])
    if v==1 and c==1 and p==0:
      for j in range(len(objects[0])):	
	if categ[0] == objects[0][j]:
	  for index in range(len(objects)):
	    if values[0] in objects[index] :
	      fileanswer.write('the '+ values[0] + ' belongs to the ' + objects[index][j] + ' ' +objects[0][j] +'\n')
  if v ==2 and p==1:
      v1 = -1
      v2 = 50
      v3 = 0
      if pref[0]in ['BIGGER','BIGGEST']:
	for index in range(1,len(objects)):
	  if objects[index][0] in values:
	    if v1 <= objects[index][8]:
	      v1= objects[index][8]
	      v3 +=1
	      ibig = index
      if pref[0]in ['SMALLEST','SMALLER']:
	for index in range(1,len(objects)):
	  if objects[index][0] in values:
	    if v2 >= int(objects[index][8]):
	      v2= int(objects[index][8])
	      v3 +=1
	      ibig = index
      if pref[0]in ['HEAVIER','HEAVIEST']:
	for index in range(1,len(objects)):
	  if objects[index][0] in values:
	    if v1 <= objects[index][7]:
	      v1= objects[index][7]
	      v3 +=1
	      ibig = index
      if pref[0]in ['LIGHTER','LIGHTEST']:
	for index in range(1,len(objects)):
	  if objects[index][0] in values:
	    if v2 >= int(objects[index][7]):
	      v2= int(objects[index][7])
	      v3 +=1
	      ibig = index
      if v3 ==1:
	fileanswer.write('The ' + pref[0].lower() +' object between ' +values[0]+' and '+values[1]+ ' is ' + objects[ibig][0] + '\n')
      elif pref[0] in ['LIGHTER','LIGHTEST','HEAVIER','HEAVIEST']:
	fileanswer.write('The ' + values[0] + ' and the ' + values[1] + ' have the same weight\n')
      elif pref[0] in ['BIGGER','BIGGEST','SMALLEST','SMALLER']:
	fileanswer.write('The ' + values[0] + ' and the ' + values[1] + ' have the same size\n')
  if v ==1 and p==1:
      print(keys)
      v1 = -1
      v2 = 50
      if pref[0]in ['BIGGER','BIGGEST']:
	for index in range(1,len(objects)):
	  if values[0] in objects[index]:
	    if v1 <= objects[index][8]:
	      v1= objects[index][8]
	      ibig = index
      if pref[0]in ['SMALLEST','SMALLER']:
	for index in range(1,len(objects)):
	  if values[0] in objects[index]:
	    if v2 >= int(objects[index][8]):
	      v2= int(objects[index][8])
	      ibig = index
      if pref[0]in ['HEAVIER','HEAVIEST']:
	for index in range(1,len(objects)):
	  if values[0] in objects[index]:
	    if v1 <= objects[index][7]:
	      v1= objects[index][7]
	      ibig = index
      if pref[0]in ['LIGHTER','LIGHTEST']:
	for index in range(1,len(objects)):
	  if values[0] in objects[index]:
	    if v2 >= int(objects[index][7]):
	      v2= int(objects[index][7])
	      ibig = index
      fileanswer.write('The ' + pref[0].lower() +' '+ values[0] + ' object is ' + objects[ibig][0] + '\n')
  
for i in range(len(keys)):
  categ=[]
  values=[]
  pref=[]
  fileanswer.write('answer ' + str(i) + '\n')
  for j in range(0,len(keys[i])):
    if keys[i][j] == 'WHAT':
      what(keys[i])
    if keys[i][j] == 'WHERE':
      where(keys[i])
    if keys[i][j] == 'WHICH':
      which(keys[i])
    if keys[i][j] == 'HOW MANY':
      howmany(keys[i])
    if keys[i][j] == 'DO':
      do(keys[i])

#print(keys)
      
 