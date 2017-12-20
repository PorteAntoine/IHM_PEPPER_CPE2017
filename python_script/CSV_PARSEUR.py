import csv
from Object import Object
from Person import Person


class CSV_TOP_PARSEUR():

    #init fonction
    #############################################################################################

    def __init__(self):
        self.objects = [] # list of objects
        self.persons = []

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
    # argument : - the path of the file to parse (must be .csv)
    ################################################################################################

    def object_transformations(self, file_path):
        objects_file = open(file_path.encode('utf-8'),'rU')

        read = csv.reader(objects_file, delimiter=";")

        for raw in read:
            for i in range(0, len(list(read))):
                object = Object()
                object.name = raw[0]
                object.color = raw[1]
                object.localization = raw[2]
                self.objects.append(object)

    # Function to transform lists from a .csv file into person definition
    #
    # argument : - the path of the file to parse (must be .csv)
    ################################################################################################

    def person_transformations(self, file_path):
        person_file = open(file_path.encode('utf-8'),'rU')

        read = csv.reader(person_file, delimiter=";")

        for raw in read:
            for i in range(0, len(self.persons)):
                person = Person()
                person.age = raw[0]
                person.gender = raw[1]
                self.person.append(person)

    # Return the number of person in the room

    def get_number_person(self):
        return len(self.persons)


if __name__ == '__main__':

    Parseur = CSV_TOP_PARSEUR()
    Parseur.questions_answers_direct("fixed_questions.csv","test_2")
    Parseur.object_transformations("objects.csv")
    Parseur.person_transformations("person.csv")
