class Process_person():

    def __init__(self):
        self.oldest_person = []
        self.youngest_person = []
    
    def hasAttribute(self,list_persons,attr):

        # retourne sous forme de liste le nom de toutes les personnes qui possedent l'attribut attr
        # list_persons est une liste de "person"
        # attr est une string pouvant contenir un age, une position etc.
        hasAttribute_list = []
        for i in list_persons:
            if i.gender == attr or i.age == str(attr) or i.position == attr or (int(i.age) < 18 and attr == "children") or (int(i.age) > 17 and attr == "adult"):
                hasAttribute_list.append(i.name)
        return hasAttribute_list

    def hasTwoAttribute(self,list_persons,attr1,attr2):

        # retourne sous forme de liste le nom de toutes les personnes qui possedent les 2 attributs attr
        # list_persons est une liste de "person"
        # attr est une string pouvant contenir un age, une position etc.
        hasAttribute_list = []
        for i in list_persons:
            if i.gender == attr1 or i.age == str(attr1) or i.position == attr1 or (int(i.age) < 19 and attr1 == "children") or (int(i.age) > 17 and attr1 == "adult"):
                if i.gender == attr2 or i.age == str(attr2) or i.position == attr2 or (int(i.age) < 19 and attr2 == "children") or (int(i.age) > 17 and attr2 == "adult"):
                    hasAttribute_list.append(i.name)
        print hasAttribute_list
        return hasAttribute_list

    def boolAttribute(self, list_persons, attr):

        # retourne vrai ou faux a une question de type "Est ce que <nom de personne> est <attribut>"
        # list_persons est une liste de "person"
        # attr est une string pouvant contenir un age, une position etc.
        for i in list_persons:
            if i.gender != attr and i.age != str(attr) and i.position != attr and (int(i.age) >= 19 or attr != "children") and (int(i.age) <= 17 or attr != "adult"):
                return False
        return True

    def oldest(self,list_persons):

        # retourne le nom de la personne la plus agee
        # list_persons est une liste de "person"
        self.oldest_person=[]
        age_list = []
        for i in list_persons:
            age_list.append(int(i.age))

        max_age = max(age_list)
        for i in list_persons:
            if int(i.age) == max_age:
                self.oldest_person.append(i.name)
        return self.oldest_person

    def youngest(self,list_persons):
        
        # retourne le nom de la personne la moins agee
        # list_persons est une liste de "person"
        self.youngest_person=[]
        age_list = []
        for i in list_persons:
            age_list.append(int(i.age))

        min_age = min(age_list)
        for i in list_persons:
            if int(i.age) == min_age:
                self.youngest_person.append(i.name)
        return self.youngest_person

    def sameAge(self, list_persons):

        # renvoie vrai si les personnes de la liste ont le meme age
        # list_persons est une liste de "person"
        if len(list_persons)>0:
            attr = list_persons[0].age
            result = self.boolAttribute(list_persons,attr)
            return result

    def sameGender(self, list_persons):

        # renvoie vrai si les personnes de la liste ont le meme sexe
        # list_persons est une liste de "person"
        if len(list_persons)>0:
            attr = list_persons[0].gender
            result = self.boolAttribute(list_persons,attr)
            return result

    def samePosition(self, list_persons):

        # renvoie vrai si les personnes de la liste ont la meme position
        # list_persons est une liste de "person"
        if len(list_persons)>0:
            attr = list_persons[0].position
            result = self.boolAttribute(list_persons,attr)
            return result

