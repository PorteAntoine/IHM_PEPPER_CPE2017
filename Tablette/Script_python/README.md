# Script python pour la tablette

### 1 - Les différents scripts :

- _"Tablet_python_showImage.py"_  petit programme qui (dans un .top) affiche des images en fonction de ce que l'on lui demande  
          
- _"Tablet_python_webView.py"_  petit programme qui (dans un .top) affiche une page web avec le nom des fruits qu'on lui dit

- _"Tablet_python_webViewEvent.py"_ pprogramme qui affiche sur page web l'historique de la discussion et la dernière question/réponse

- _"TabletModule.py"_ class de la tablette à implémenter
  
  
### 2 - Comment utiliser la class  :

* Nom de la classe : 

          TabletModule
 
* Initialisation  :
 
          Tablet = TabletModule("Tablet","tablette_test")

 avec _"Tablet"_ nom du module créé et _"tablette_test"_ le nom de l'application de la tablette où sont garder en mémoire les fichiers
   
* Fonctions :

---

  1. appTablet_history
  
          Tablet.appTablet_history(memory, questions, answers)

fonction à appeler pour afficher une page web de l'historique de la discussion et la dernière question/réponse. à appeler dans un event "dialog/LastAnswer" après le remplissage d'un historique de discussion
   
 _"memory"_  : lien vers la mémoire du robot qui doit être défini avant dans le programme principal
   
 _"questions"_  : liste des questions posées

 _"answers"_  : liste des réponses posées

---

   2. appTablet_test

          Tablet.appTablet_test(memory, string_titre, string_1, string_2, string_3, string_pourcentage)
                    
fonction à appeler pour afficher une page web de l'historique de la discussion et la dernière question/réponse. à appeler dans un event "dialog/LastAnswer" après le remplissage d'un historique de discussion
   
 _"memory"_  : lien vers la mémoire du robot qui doit être défini avant dans le programme principal
   
 _"string_titre"_  : string contenant le titre de la page web du test

 _"string_1"_  : string contenant le premier texte à afficher
 
  _"string_2"_  : string contenant le deuxième texte à afficher
  
  _"string_3"_  : string contenant le troisième texte à afficher
 
  _"string_pourcentage"_  : string contenant le pourcentage de l'avancé du test (entre 0 et 100)
  
---
          
                    



  
  
