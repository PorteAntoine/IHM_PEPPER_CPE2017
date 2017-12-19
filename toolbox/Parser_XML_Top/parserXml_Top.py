# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

file = open('questions2.top','w') 
file.write('topic: ~concept()' + '\n' + 'language: enu'+ '\n'+'\n')
tree = ET.parse('questions.xml')
root = tree.getroot()
for child in root:
	for kid in child:
		if str(kid.tag) == 'q' :
			file.write('u:(' + kid.text + ')')
		elif str(kid.tag) == 'a':
			file.write(kid.text + '\n')
