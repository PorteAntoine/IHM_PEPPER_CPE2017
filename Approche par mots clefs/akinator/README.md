appeler la classe comme ceci:

from akinator import Answerthequestion

print(Answerthequestion("what is the colour of the chips ?").answer())

cette classe traite toute question faisant référence au fichier csv objects ou persons ps: idéalement créer un répertoire nommé montreal au niveau de script akinator et y mettre le fichier objet.csv et persons.csv

compare_keys: cette fonction permet de comparer 2 string et de renvoyer true or false selon si les 2 string contiennent exactement les memes clés 
exemple: compare_keys("the pringles has the blue color","the color of these pringles is blue") renvoie true
         compare_keys("the pringles are red","the pringles are blue") renvoie false
