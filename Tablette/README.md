# PARTIE SUR LA GESTION DE LA TABLETTE
dossier :
  - "ProjectChorégraphe" contient le(s) projet(s) à installer sur le robot 
  - "Script_python"  
    

  
# Comment utiliser ?

### 1 - Mettre les photos dans la mémoire :

- Par chorégraphe :

Dans un projet chorégraphe (tablette_test présent dans le github est un exemple), importer dans un dossier 'html' les images à afficher

Dans le robot pannel, installer l'application du projet dans le robot.  
          
          
- OU directement en copiant les images:

Copier les images dans le robot à :

     .local/share/apps/{_nomApplication_}/html/..  
  
    
### 2 - Script Python :
Dans l'example suivant, les images ont étaient copiées dans l'application nommée _"tablette_test"_ et dans le dossier _"/html/img_ de cette application.

     tabletservice = ALProxy("ALTabletService", robot_ip, robot_port)
     val = tabletservice.preLoadImage("http://198.18.0.1/apps/tablette_test/img/image1.png")
     val = tabletservice.showImage("http://198.18.0.1/apps/tablette_test/img/image1.png")
     
ATTENTION : dans l'URL, il ne faut écrire le dossier html

