Programme de réponse en mode Approche dynamique.

Toutes les réponses sont générées en utilisant les objets présents dans les fichiers CSV list_locations_final.csv ; list_objects_final.csv et list_persons_final.csv
Ces fichiers sont parsés grâce au CSV_PARSEUR.
Lorsque le programme est lancé, la plupart des réponses aux questions sont process dans les différents fichier python : Process_Object_Module.py Process_Person_Module.py et Process_Localization_Module.py
Ces fichiers sont une surcouche permettant d'utiliser les réelles fonctions de process (dans un format different) qui se trouvent dans les fichier Process_Object.py, Process_Person.py et Process_Localization.py.
Le changement de format est effectué dans la librairie de fonction appelée Utils.py

Comment lancer le programme:
  * Modifier la variable NAO_IP à la ligne 13 du fichier main.py (addresse IP du robot ou "localhost")
  * Modifier la variable NAO_PORT à la ligne 14 du fichier main.py (port du robot)
  * Modifier le topf_path à la ligne 15 du fichier main.py en lui fournissant le chemin absolu vers le fichier main_topic_enu.top
            /!\ Le fichier doit se trouver sur le robot lorsque l'on utilise un robot réel (non virtuel)
  * Modifier le topf_path à la ligne 15 du fichier SET_KNOWLEDGE.py en lui fournissant le chemin absolu vers le fichier main_topic_enu.top
  * lancer le fichier main.py 
  * Attendre que la phrase Speak to the robot using rules from both the activated topics. Press Enter when finished: apparaisse dans l'invite de commande puis parler
  * Appuyer sur entrer pour quitter
