from CSV_PARSEUR import CSV_PARSEUR

class Process_object():

    def __init__(self):
        self.biggest_obj = []
        self.heaviest_obj = []
        self.little_obj = []
        self.lightest_obj = []

    
    def hasAttribute(self,list_objects,attr):

        # retourne sous forme de liste le nom de tous les objets qui possedent l'attribut attr
        # list_objects est une liste d'"objects"
        # attr est une string pouvant contenir une categorie, une couleur, une forme, une taille, un type, une localisation, un poids ou une salle
        hasAttribute_list = []
        for i in list_objects:
            if i.category == attr or i.color == attr or i.shape == attr or i.size == attr or i.type == attr or i.localization == attr or i.weight == attr or i.room == attr:
                hasAttribute_list.append(i.name)
        return hasAttribute_list

    def boolAttribute(self, list_objects, name, attr):

        # retourne vrai ou faux a une question de type "Est ce que <nom d'objet> est <attribut>"
        # list_objects est une liste d'"objects"
        # attr est une string pouvant contenir une categorie, une couleur, une forme, une taille, un type, une localisation, un poids ou une salle
        for i in list_objects:
            if i.name == name:
                if i.category == attr or i.color == attr or i.shape == attr or i.size == attr or i.type == attr or i.localization == attr or i.weight == attr or i.room == attr:
                    return True
                else:
                    return False
                
        
    def biggest(self,list_objects):

        # retourne le nom de l'objet le plus gros
        # list_objects est une liste d'"objects"
        size_list = []
        for i in list_objects:
            size_list.append(int(i.size))

        max_size = max(size_list)
        for i in list_objects:
            if int(i.size) == max_size:
                self.biggest_obj.append(i.name)
        return self.biggest_obj
        
    def heaviest(self,list_objects):

        # retourne le nom de l'objet le plus lourd
        # list_objects est une liste d'"objects"
        weight_list = []
        for i in list_objects:
            weight_list.append(int(i.weight))

        max_weight = max(weight_list)
        for i in list_objects:
            if int(i.weight) == max_weight:
                self.heaviest_obj.append(i.name)
        return self.heaviest_obj

    def little(self,list_objects):

        # retourne le nom de l'objet le plus petit
        # list_objects est une liste d'"objects"
        size_list = []
        for i in list_objects:
            size_list.append(int(i.size))

        min_size = min(size_list)
        for i in list_objects:
            if int(i.size) == min_size:
                self.little_obj.append(i.name)
        return self.little_obj
    
    def lightest(self,list_objects):

        # retourne le nom de l'objet le plus leger
        # list_objects est une liste d'"objects"
        weight_list = []
        for i in list_objects:
            weight_list.append(int(i.weight))

        min_weight = min(weight_list)
        for i in list_objects:
            if int(i.weight) == min_weight:
                self.lightest_obj.append(i.name)
        return self.lightest_obj


if __name__ == '__main__':
    Parseur = CSV_PARSEUR()
    Parseur.object_transformations("objects.csv")
    process = Process_object()
    print "big : ", process.biggest(Parseur.objects)
    print "heavy : ", process.heaviest(Parseur.objects)
    print "little : ", process.little(Parseur.objects)
    print "light : ", process.lightest(Parseur.objects)
    print "has Attribute : ", process.hasAttribute(Parseur.objects, "kitchen")
    print "is it True ? ",process.boolAttribute(Parseur.objects,"pringles","red")
