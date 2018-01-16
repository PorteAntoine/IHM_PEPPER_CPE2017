# PARTIE SUR LA GESTION DE LA TABLETTE
dossier :
  - "ProjectChorégraphe" contient le(s) projet(s) à installer sur le robot 
  - "Script_python" 
      - "Tablet_python_showImage" permet d'afficher des images en disant _"banana"_ ou  _"apple"_ ou _"pineapple"_
      - "Tablet_python_webView"   permet d'afficher des textes en disant _"banana"_ ou  _"apple"_ ou _"pineapple"_
      - "Tablet_python_webViewEvent" permet d'afficher l'historique des questions/réponses et la dernière en affichage dynamique
    
  
# Comment utiliser la tablette ?

### 1 - Mettre les photos dans la mémoire :

- Par chorégraphe :

Dans un projet chorégraphe (_"tablette_test"_ présent dans le github est un exemple), importer dans un dossier 'html' les images à afficher

Dans le robot pannel, installer l'application du projet dans le robot.  
          
          
- OU directement en copiant les images:

Copier les images dans le robot à :

     .local/share/apps/PackageManager/{_nomApplication_}/html/..  
  
  
### 2 - Mettre le contenu des WebPages :
Avec les mêmes methodes que pour les photos, mettre les fichiers .html dans le dossier _/html_

Mettre les éventuelles fichiers JS et CSS si vous en avez créé.


### 3 - Script Python : 

- Pour afficher des images:

Dans l'example suivant, les images ont été copiées dans l'application nommée _"tablette_test"_ et dans le dossier _"/html/img_ de cette application.

     tabletservice = ALProxy("ALTabletService", robot_ip, robot_port)
     val = tabletservice.preLoadImage("http://198.18.0.1/apps/tablette_test/img/image1.png")
     val = tabletservice.showImage("http://198.18.0.1/apps/tablette_test/img/image1.png")
     
- Pour afficher des pages web:

Dans l'example suivant, le fichier index2.html a été copié dans le dossier html

     tabletservice = ALProxy("ALTabletService", robot_ip, robot_port)
     val = tabletservice.loadUrl("http://198.18.0.1/apps/tablette_test/index2.html")
     val = tabletservice.showWebview()


ATTENTION : dans l'URL, il ne faut pas écrire le dossier html

# Comment utiliser les exemples ?

- Ouvrir le projet _"tablette_test"_ dans chorégraphe

- installer l'application dans le robot

- lancer le script python voulue
