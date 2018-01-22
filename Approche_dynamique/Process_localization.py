class Process_localization():

    def __init__(self):
        self.init = []


    def hasAttribute(self,list_localization,attr):

        # retourne sous forme de liste le nom de tous les objets qui possedent l'attribut attr
        # list_objects est une liste d'"objects"
        # attr est une string pouvant contenir une categorie, une couleur, une forme, une taille, un type, une localisation, un poids ou une salle
        hasAttribute_list = []
        print list_localization
        for i in list_localization:
            if(attr=="beacon") :
                if (i.beacon == "True" or i.beacon =="true") :
                    hasAttribute_list.append(i.name)
            if (attr == "placement"):
                if (i.placement == "True" or i.placement == "true"):
                    hasAttribute_list.append(i.name)
            if i.name == attr or i.room == attr :
                hasAttribute_list.append(i.name)
        print(hasAttribute_list)
        return hasAttribute_list
