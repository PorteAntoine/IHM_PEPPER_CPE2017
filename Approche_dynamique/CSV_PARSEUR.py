import csv
from Object import Object
from Person import Person
from Localization import Localization

class CSV_PARSEUR():

    #init fonction
    #############################################################################################

    def __init__(self, path_file_objects, path_file_persons,path_file_localization):
        self.objects = []
        self.persons = []
        self.localizations = []
        self.path_file_objects = path_file_objects
        self.path_file_persons = path_file_persons
        self.path_file_localization = path_file_localization
        self.object_transformations()
        self.person_transformations()
        self.localization_transformations()

    # Function to generate a .top file from a .csv file with fixed questions and fixed answers
    #
    # argument : - the path of the file to parse (must be .csv)
    #            - the name of the file .top to generate (must be a new name to not overwrite a file)
    ################################################################################################

    def questions_answers_direct(self, file_path, final_file_name):
        file_questions_answer = open(file_path.encode('utf-8'),'rb')
        final_file = open(final_file_name+".top","w")

        final_file.write("topic: ~test()\n")
        final_file.write("language: enu\n")

        read = csv.reader(file_questions_answer, delimiter=";")

        for raw in read:
            final_file.write("u:("+raw[0]+") "+raw[1]+"\n")

    # Function to transform lists from a .csv file into object definition
    #
    # argument : None
    ################################################################################################

    def object_transformations(self):
        objects_file = open(self.path_file_objects.encode('utf-8'),'rU')

        read = list(csv.reader(objects_file, delimiter=";"))
        for raw in read[1:]:
            object = Object()
            object.name = raw[0]
            object.type = raw[1]
            object.category = raw[2]
            object.localization = raw[3]
            object.room = raw[4]
            object.color = raw[5]
            object.shape = raw[6]
            object.size = raw[7]
            object.weight = raw[8]

            self.objects.append(object)

    # Function to transform lists from a .csv file into person definition
    #
    # argument : None
    ################################################################################################

    def person_transformations(self):
        person_file = open(self.path_file_persons.encode('utf-8'),'rU')

        read = list(csv.reader(person_file, delimiter=";"))

        for raw in read[1:]:
            person = Person()
            person.name = raw[0]
            person.gender = raw[1]
            person.age = raw[2]
            person.position = raw[3]
            self.persons.append(person)

    def localization_transformations(self):
        localization_file = open(self.path_file_localization.encode('utf-8'), 'rU')

        read = list(csv.reader(localization_file, delimiter=";"))

        for raw in read[1:]:
            localization = Localization()
            localization.room = raw[0]
            localization.name = raw[1]
            localization.placement = raw[2]
            localization.beacon = raw[3]
            self.localizations.append(localization)
    # Return the number of person in the room

    def get_number_person(self):
        return len(self.persons)



if __name__ == '__main__':

    Parseur = CSV_PARSEUR("list_objects_final.csv", "list_persons_final.csv")
