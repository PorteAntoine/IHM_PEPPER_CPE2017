import csv

fileobj = open('montreal/objects.csv','r') 

filequestion = open('questions.txt','r')
filekey = open('keys.csv','w')
objreader = csv.reader(fileobj, delimiter=';')

objects = []
questions = []

for row in objreader:
	objects.append(row)
	
m1=0

for i in range(len(objects)):
	if len(objects[i])>m1:
		m1 = len(objects[i])
m2 = i	

print(str(m1)+' '+str(m2))

remains=''
for row in filequestion:
	questions.append(row)
prefix = ['do','heavier','lighter','smaller','bigger','heaviest','lightest','smallest','biggest','which','where','what','how many']
print(objects[0][0])
for i in range (0,len(questions)):
	remains = ''
	#print('question n' + str(i))
	#filekey.write('question n' + str(i)+'\n')
	for k in range(0,len(prefix)):
	   if prefix[k].lower() in questions[i].lower():
	     #print(prefix[k])
	     filekey.write(prefix[k].upper()+ ',')
	for k in range (0,m2+1):
		for l in range(0,m1):
			#print('i :'+str(i)+';'+'k :'+str(k)+';'+'l :'+str(l)+';')
			if ' '+objects[k][l].lower()+' ' in questions[i].lower():
				#print(objects[k][l])
				if not(objects[k][l] in remains):
				  remains += objects[k][l]
				  filekey.write(objects[k][l]+ ',')			  
	filekey.write('\n')









		
