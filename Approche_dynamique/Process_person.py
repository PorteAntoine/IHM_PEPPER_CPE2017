from CSV_PARSEUR import CSV_PARSEUR

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
            if i.gender == attr or i.age == attr or i.position == attr:
                hasAttribute_list.append(i.name)
        return hasAttribute_list

    def boolAttribute(self, list_persons, name, attr):

        # retourne vrai ou faux a une question de type "Est ce que <nom de personne> est <attribut>"
        # list_persons est une liste de "person"
        # attr est une string pouvant contenir un age, une position etc.
        for i in list_persons:
            if i.name == name:
                if i.gender == attr or i.age == attr or i.position == attr:
                    return True
                else:
                    return False

    def oldest(self,list_persons):

        # retourne le nom de la personne la plus agee
        # list_persons est une liste de "person"
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
        age_list = []
        for i in list_persons:
            age_list.append(int(i.age))

        min_age = min(age_list)
        for i in list_persons:
            if int(i.age) == min_age:
                self.youngest_person.append(i.name)
        return self.youngest_person
    
if __name__ == '__main__':
    Parseur = CSV_PARSEUR()
    Parseur.person_transformations("person.csv")
    process = Process_person()
    print process.hasAttribute(Parseur.persons,"male")
    print process.oldest(Parseur.persons)
    print process.youngest(Parseur.persons)
    print process.boolAttribute(Parseur.persons,"Barbara","lying")
