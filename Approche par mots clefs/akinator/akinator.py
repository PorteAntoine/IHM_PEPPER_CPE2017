
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# run with python 03_...py --qi-url="tcp://ip_robot:9559"

import csv
#import qi
#from Utils import Utils

class Answerthequestion:
  def __init__(self,arg):
    self.question= arg
    
  def answer(self):
    fileobj = open('montreal/objects.csv','r') 
    filepers = open('montreal/persons.csv','r')
    fileloc = open('montreal/locations.csv','r')
    #creation des listes de cles pour chacuns des csv independamment de la question
    objreader = csv.reader(fileobj, delimiter=';')
    persreader =  csv.reader(filepers, delimiter=',')
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
    
    remains=''
    prefix = ['who','how old','is there','do','heavier','lighter','smaller','bigger','heaviest','lightest','smallest','biggest','which','where','what','how many']
    
    for k in range(0,len(prefix)):
      if prefix[k].lower() in self.question.lower():
	keys.append(prefix[k].upper())
	for k in range (0,m2+1):
	  for l in range(0,m1):
	    if ' '+objects[k][l].lower()+' ' in self.question.lower():
	      if not(objects[k][l] in remains):
		remains += objects[k][l]
		keys.append(objects[k][l])
    for i in range(0,len(keys)-1):
      if keys[i][len(keys[i])-1] is '':
	keys[i].pop()
    
    for k in range(0,len(prefix)):
      if prefix[k].lower() in self.question.lower():
	keysp.append(prefix[k].upper())
	for l in range(0,p1):
	  if ' '+persons[0][l].lower()+' ' in self.question.lower():
	    keysp.append(persons[0][l])
	for k in range (1,p2+1):
	  for l in range(0,p1):
	    if ' '+persons[k][l].lower()+' ' in self.question.lower():
	      if not(persons[k][l] in remains):
		remains += persons[k][l]
		keysp.append(persons[k][l].lower())
		
    for k in range(0,len(prefix)):
      if prefix[k].lower() in self.question.lower():
	keysl.append(prefix[k].upper())
	for l in range(0,l1):
	  if ' '+locations[0][l].lower()+' ' in self.question.lower():
	    keysl.append(locations[0][l])
	for k in range (1,l2+1):
	  for l in range(0,l1):
	    if ' '+locations[k][l].lower()+' ' in self.question.lower():
	      if not(locations[k][l] in remains):
		remains += locations[k][l]
		keysl.append(locations[k][l].lower())
    
    #disjonction de cas en fonction de la quantite d'elements dans chaque liste, selection d'un seul gagnant
    if len(keys) >= len(keysp) and len(keys) >= len(keysl):
      for i in range(len(keys)):
	categ=[]
	values=[]
	pref=[]
	for i in range(0,len(keys)):
	  if keys[i] == keys[i].lower():
	    values.append(keys[i])
	  elif keys[i] == keys[i].upper() :
	    pref.append(keys[i])
	  else:
	    categ.append(keys[i])
	key= Keywords()
	key.categ=categ
	key.values=values
	key.pref=pref      
	for j in range(0,len(pref)):
	  if 'WHAT' in pref:
	    key.pref.remove('WHAT')
	    return(key.what(objects))
	    break
	  if 'WHERE' in pref:
	    key.pref.remove('WHERE')
	    return(key.where(objects))
	    break
	  if 'WHICH' in pref:
	    key.pref.remove('WHICH')
	    return(key.which(objects))
	    break
	  if 'HOW MANY' in pref:
	    key.pref.remove('HOW MANY')
	    return(key.howmany(objects))
	    break
	  if 'DO' in pref:
	    key.pref.remove('DO')
	    return(key.do(objects))
	    break
	  if 'IS THERE' in pref:
	    key.pref.remove('IS THERE')
	    return(key.is_there(objects))
	    break
    elif len(keysp) >= len(keysl):
      for i in range(len(keysp)):
	categ=[]
	values=[]
	pref=[]
	for i in range(0,len(keysp)):
	  if keysp[i] == keysp[i].lower():
	    values.append(keysp[i])
	  elif keysp[i] == keysp[i].upper() :
	    pref.append(keysp[i])
	  else:
	    categ.append(keysp[i])
	key= Keywordspersons()
	key.categ=categ
	key.values=values
	key.pref=pref      
	for j in range(0,len(keysp[i])):
	  if 'WHAT' in pref :
	    key.pref.remove('WHAT')
	    return(key.what(persons))
	    break
	  if 'HOW MANY' in pref:
	    key.pref.remove('HOW MANY')
	    return(key.howmany(persons))
	    break
	  if 'WHO' in pref :
	    key.pref.remove('WHO')
	    return(key.who(persons))
	    break
    else:
      for i in range(len(keysl)):
	categ=[]
	values=[]
	pref=[]
	for i in range(0,len(keysl)):
	  if keysl[i] == keysl[i].lower():
	    values.append(keysl[i])
	  elif keysl[i] == keysl[i].upper() :
	    pref.append(keysl[i])
	  else:
	    categ.append(keysl[i])
	key= Keyloc()
	key.categ=categ
	key.values=values
	key.pref=pref      
	for j in range(0,len(pref)):
	  if 'WHAT' in pref :
	    key.pref.remove('WHAT')
	    return(key.what(locations))
	    break
	  if 'HOW MANY' in pref:
	    key.pref.remove('HOW MANY')
	    return(key.howmany(locations))
	    break
	  if 'WHERE' in pref :
	    key.pref.remove('WHERE')
	    return(key.where(locations))
	    break
#reponse aux questions traitant sur les objets
class Keywords:
  def __init__(self):
    self.pref = []
    self.categ= []
    self.values = []  
  
  def which(self,objects):
      v=len(self.values)
      c=len(self.categ)
      p=len(self.pref)
      if v ==2 and p==1:
	  v1 = -1
	  v2 = 50
	  equality = False
	  
	  if self.pref[0]in ['BIGGER','BIGGEST']:
	    for index in range(1,len(objects)):
	      if objects[index][0] in self.values:
		if v1 <= objects[index][8]:
		  if v1 == objects[index][8]:
		    equality = True
		  v1= objects[index][8]
		  ibig = index		
	  if self.pref[0]in ['SMALLEST','SMALLER']:
	    for index in range(1,len(objects)):
	      if objects[index][0] in self.values:
		if v2 >= int(objects[index][8]):
		  if v2 == int(objects[index][8]):
		    equality = True
		  v2= int(objects[index][8])
		  ibig = index
	  if self.pref[0]in ['HEAVIER','HEAVIEST']:
	    for index in range(1,len(objects)):
	      if objects[index][0] in self.values:
		if v1 <= objects[index][7]:
		  if v1 == objects[index][7]:
		    equality ==True
		  v1= objects[index][7]
		  ibig = index
	  if self.pref[0]in ['LIGHTER','LIGHTEST']:
	    for index in range(1,len(objects)):
	      if objects[index][0] in self.values:
		if v2 >= int(objects[index][7]):
		  if v2 == int(objects[index][7]):
		    equality == True
		  v2= int(objects[index][7])
		  ibig = index
	  if equality == False:
	    return('The ' + self.pref[0].lower() +' object between ' +self.values[0]+' and '+self.values[1]+ ' is ' + objects[ibig][0] + '\n')
	  elif self.pref[0] in ['LIGHTER','LIGHTEST','HEAVIER','HEAVIEST']:
	    return('The ' + self.values[0] + ' and the ' + self.values[1] + ' have the same weight\n')
	  elif self.pref[0] in ['BIGGER','BIGGEST','SMALLEST','SMALLER']:
	    return('The ' + self.values[0] + ' and the ' + self.values[1] + ' have the same size\n')
      if v ==1 and c==1:
	for j in range(len(objects[0])):	
	  if self.categ[0] == objects[0][j]:
	    for index in range(len(objects)):
	      if self.values[0] in objects[index] :
		return('The ' + objects[0][j] + ' of the ' + objects[index][0] + ' is ' +objects[index][j] + '\n')  

      if v ==1 and p==1:
	  v1 = -1
	  v2 = 50
	  if self.pref[0]in ['BIGGER','BIGGEST']:
	    for index in range(1,len(objects)):
	      if self.values[0] in objects[index]:
		if v1 <= objects[index][8]:
		  v1= objects[index][8]
		  ibig = index
	  if self.pref[0]in ['SMALLEST','SMALLER']:
	    for index in range(1,len(objects)):
	      if self.values[0] in objects[index]:
		if v2 >= int(objects[index][8]):
		  v2= int(objects[index][8])
		  ibig = index
	  if self.pref[0]in ['HEAVIER','HEAVIEST']:
	    for index in range(1,len(objects)):
	      if self.values[0] in objects[index]:
		if v1 <= objects[index][7]:
		  v1= objects[index][7]
		  ibig = index
	  if self.pref[0]in ['LIGHTER','LIGHTEST']:
	    for index in range(1,len(objects)):
	      if self.values[0] in objects[index]:
		if v2 >= int(objects[index][7]):
		  v2= int(objects[index][7])
		  ibig = index
	  return('The ' + self.pref[0].lower() +' '+ self.values[0] + ' object is ' + objects[ibig][0] + '\n')
      if v>0 :
	counter =0
	return_str='The items which are in the category '
	for va in range(len(self.values)):
	  return_str+=self.values[va] + ' '
	return_str += 'are : '
	for index in range(len(objects)):	
	  belong = True
	  for index2 in range(len(self.values)):
	    if not self.values[index2] in objects[index]:
	      belong = False
	  if belong == True:
	    return_str+=objects[index][0]+' '
	    counter+=1
	return(return_str)
  
  
  def howmany(self,objects):
      v=len(self.values)
      c=len(self.categ)
      p=len(self.pref)
      return_str=''
      if v>0 :
	counter =0
	for index in range(len(objects)):	
	  belong = True
	  for index2 in range(len(self.values)):
	    if not self.values[index2] in objects[index]:
	      belong = False
	  if belong == True:
	    counter+=1
      return_str+='There are ' + str(counter)+ ' items belonging to the '
      for p in range(len(self.values)):
	return_str+=self.values[p]+' '
      return_str+='category\n'
      return(return_str)
     
  def where(self,objects):
    v=len(self.values)
    c=len(self.categ)
    p=len(self.pref)
    for j in range(len(self.values)):
      for i in range(len(objects)):
	if objects[i][0] == self.values[j]:
	  return('the ' + objects[i][0] + ' is in the '+objects[i][3]+ ' which is located in the ' + objects[i][4]+'\n')
  
  def do(self,objects):
    v=len(self.values)
    c=len(self.categ)
    p=len(self.pref)
    counter =0
    valors=[]
    
    if v==2:
      
      for cat in range(len(objects[0])):
	if objects[0][cat] in self.categ:
	  valors.append(cat)
      belong = True
      
      for k in range(len(valors)):
	  storage= []
	  for index in range(len(objects)):
	    if objects[index][0] in self.values : 
	      storage.append(objects[index][valors[k]])
	      for s in range(len(storage)):
		if not storage[s] == storage[0] :
		  belong = False
	  if belong == False:
	    break
      if belong == True:
	return('That is correct, the ' + self.categ[0] +' of the '+ self.values[0] + ' and ' + self.values[1] + ' is the same, which is '+ storage[0]+'\n')
      else:
	return('Incorrect, the '+ self.categ[0] +' of the '+ self.values[0] + ' and ' + self.values[1] + ' are not the same\n')
  
  def what(self,objects):
      v=len(self.values)
      c=len(self.categ)
      p=len(self.pref)
      if v==1 and c==1 and p==0:
	for j in range(len(objects[0])):	
	  if self.categ[0] == objects[0][j]:
	    for index in range(len(objects)):
	      if self.values[0] in objects[index] :
		return('The ' + objects[0][j] + ' of the ' + objects[index][0] + ' is ' +objects[index][j] + '\n')  
      if v>0 :
	counter =0
	return_str='The items which are in the category '
	for va in range(len(self.values)):
	  return_str+=self.values[va] + ' '
	return_str += 'are : '
	for index in range(len(objects)):	
	  belong = True
	  for index2 in range(len(self.values)):
	    if not self.values[index2] in objects[index]:
	      belong = False
	  if belong == True:
	    return_str+=objects[index][0]+' '
	    counter+=1
	return(return_str)

  def is_there(self,objects):
    for j in range(len(objects)):
      exists = True
      for i in range(len(self.values)):
	if not self.values[i] in objects[j]:
	  exists = False
      if exists == True:
	return('Yes ,there is at least one object with these features')
    return('No, there is no object with such features')

#reponse aux questions traitant sur les personnes
class Keywordspersons:	  
  def __init__(self):
    self.pref = []
    self.categ= []
    self.values = []  
  def what(self,persons):
      v=len(self.values)
      c=len(self.categ)
      p=len(self.pref)
      if v==1 and c==1 and p==0:
	for j in range(len(persons[0])):	
	  if self.categ[0] == persons[0][j]:
	    for index in range(len(persons)):
	      if self.values[0] in persons[index]:
		return('The ' + self.categ[0] + ' of ' + self.values[0] + ' is ' +persons[index][j] + '\n')  
  def howmany(self,persons):
      v=len(self.values)
      c=len(self.categ)
      p=len(self.pref)
      return_str=''
      if v>0 :
	counter =0
	for index in range(len(persons)):	
	  belong = True
	  for index2 in range(len(self.values)):
	    if not self.values[index2] in persons[index]:
	      belong = False
	  if belong == True:
	    counter+=1
      return_str+='There are ' + str(counter)+ ' persons belonging to the '
      for p in range(len(self.values)):
	return_str+=self.values[p]+' '
      return_str+='category\n'
      return(return_str)  
  def who(self,persons):
    v=len(self.values)
    c=len(self.categ)
    p=len(self.pref)
    return_str='The persons which are ' + self.values[0] + ' are : '
    for i in range(len(persons)):
      if self.values[0] in persons[i]:
	return_str+=persons[i][0]+ ', '
    return return_str
      
class Keyloc:	
  def __init__(self):
    self.pref = []
    self.categ= []
    self.values = []  
  def where(self,locations):
    v=len(self.values)
    c=len(self.categ) 
    p=len(self.pref)
    for i in range(len(locations)):
	if locations[i][0] == self.values[0]:
	  return('the ' + locations[i][0] + ' is in the '+locations[i][1]+ '\n')
