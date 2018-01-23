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

    def hasTwoAttribute(self,list_objects,attr1,attr2):

        # retourne sous forme de liste le nom de tous les objets qui possedent les 2 attributs attr
        # list_objects est une liste d'"objects"
        # attr est une string pouvant contenir une categorie, une couleur, une forme, une taille, un type, une localisation, un poids ou une salle
        hasAttribute_list = []
        for i in list_objects:
            if i.category == attr1 or i.color == attr1 or i.shape == attr1 or i.size == attr1 or i.type == attr1 or i.localization == attr1 or i.weight == attr1 or i.room == attr1:
                if i.category == attr2 or i.color == attr2 or i.shape == attr2 or i.size == attr2 or i.type == attr2 or i.localization == attr2 or i.weight == attr2 or i.room == attr2:
                    hasAttribute_list.append(i.name)
        return hasAttribute_list

    def boolAttribute(self, list_objects , attr):

        # retourne vrai si tous les objets de la list_objects possedent l'attribut attr, faux sinon
        # list_objects est une liste d'"objects"
        # attr est une string pouvant contenir une categorie, une couleur, une forme, une taille, un type, une localisation, un poids ou une salle
        for i in list_objects:
            if i.category != attr and i.color != attr and i.shape != attr and i.size != attr and i.type != attr and i.localization != attr and i.weight != attr and i.room != attr:
                return False
        return True

    def sameCategory(self, list_objects):

        # renvoie vrai si les objets de la liste sont dans la meme categorie
        # list_objects est une liste d'"objects"
        if len(list_objects)>0:
            attr = list_objects[0].category
            return self.boolAttribute(list_objects,attr)

    def sameType(self, list_objects):

        # renvoie vrai si les objets de la liste sont dans la meme type
        # list_objects est une liste d'"objects"
        if len(list_objects) > 0:
            attr = list_objects[0].type
            return self.boolAttribute(list_objects, attr)

    def sameRoom(self, list_objects):

        # renvoie vrai si les objets de la liste sont dans la meme type
        # list_objects est une liste d'"objects"
        if len(list_objects) > 0:
            attr = list_objects[0].room
            return self.boolAttribute(list_objects, attr)

    def sameColor(self, list_objects):

        # renvoie vrai si les objets de la liste sont dans la meme type
        # list_objects est une liste d'"objects"
        if len(list_objects) > 0:
            attr = list_objects[0].color
            return self.boolAttribute(list_objects, attr)

    def sameWeight(self, list_objects):

        # renvoie vrai si les objets de la liste sont dans la meme type
        # list_objects est une liste d'"objects"
        if len(list_objects) > 0:
            attr = list_objects[0].weight
            return self.boolAttribute(list_objects, attr)

    def sameSize(self, list_objects):

        # renvoie vrai si les objets de la liste sont dans la meme type
        # list_objects est une liste d'"objects"
        if len(list_objects) > 0:
            attr = list_objects[0].size
            return self.boolAttribute(list_objects, attr)

    def sameLocalization(self, list_objects):

        # renvoie vrai si les objets de la liste sont dans la meme type
        # list_objects est une liste d'"objects"
        if len(list_objects) > 0:
            attr = list_objects[0].localization
            return self.boolAttribute(list_objects, attr)


    def biggest(self,list_objects):

        # retourne le nom de l'objet le plus gros
        # list_objects est une liste d'"objects"
        self.biggest_obj = []
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
        self.heaviest_obj = []
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
        self.little_obj = []
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
        self.lightest_obj=[]
        weight_list = []
        for i in list_objects:
            weight_list.append(int(i.weight))

        min_weight = min(weight_list)
        for i in list_objects:
            if int(i.weight) == min_weight:
                self.lightest_obj.append(i.name)
        return self.lightest_obj


