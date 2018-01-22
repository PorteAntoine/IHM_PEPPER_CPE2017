from CSV_PARSEUR import CSV_PARSEUR
from Utils import Utils
from Process_Object_Module import ProcessObjectModule
from Process_Localization_Module import ProcessLocalizationModule
from Process_Person_Module import ProcessPersonModule


class defineDialog :
    def __init__(self, session, ALDialog):
        self.session = session
        self.ALDialog = ALDialog

    def set_knowledge(self):

        topf_path ='C:/Users/astro/Documents/projetmaj/IHM_PEPPER_CPE2017/Approche_dynamique/main_topic_enu.top'
        self.ALDialog.stopTopics(self.ALDialog.getAllLoadedTopics())

        #    self.ALDialog.setLanguage("English")
        knowledge_service = self.session.service("ALKnowledge")

        parseur = CSV_PARSEUR("list_objects_final.csv","list_person_final.csv","list_locations_final.csv")

        #initialize AlModule to use in .top file
        processObject= ProcessObjectModule(self.session,parseur)
        processLocalization = ProcessLocalizationModule(self.session,parseur)
        processPerson = ProcessPersonModule(self.session, parseur)

        #register ALModule to use in .top fil
        self.session.registerService("ProcessObjectModule", processObject)
        self.session.registerService("ProcessLocalizationModule", processLocalization)
        self.session.registerService("ProcessPersonModule", processPerson)

        utils=Utils()

        objects = []
        categories = []
        types = []
        colors = []
        rooms = []
        shapes = []
        sizes = []
        weights = []
        localizations = []
        localizationsBeacon=[]

        persons = []
        genders = []
        ages = []
        positions = []

        #Clear knowledge to make sure it's empty before addind new entries.
        result = knowledge_service.resetKnowledge("knowledge")

        for object in parseur.objects:
            knowledge_service.add("knowledge", object.name, "hasColor", object.color)
            knowledge_service.add("knowledge", object.name, "isoftype", object.type)
            knowledge_service.add("knowledge", object.name, "belongstocategory", object.category)
            knowledge_service.add("knowledge", object.name, "islocated", object.localization)
            knowledge_service.add("knowledge", object.name, "isintheroom", object.room)
            knowledge_service.add("knowledge", object.name, "hasShape", object.shape)
            knowledge_service.add("knowledge", object.name, "size", object.size)
            knowledge_service.add("knowledge", object.name, "weight", object.weight)

            objects.append(object.name)
            categories.append(object.category)
            types.append(object.type)
            colors.append(object.color)
            rooms.append(object.room)
            shapes.append(object.shape)
            sizes.append(object.size)
            weights.append(object.weight)
            localizations.append(object.localization)


        for person in parseur.persons:
            knowledge_service.add("knowledge", person.name, "isofgender", person.gender)
            knowledge_service.add("knowledge", person.name, "isoftheageof", person.age)
            knowledge_service.add("knowledge", person.name, "islocated", person.position)
            persons.append(person.name)
            genders.append(person.gender)
            ages.append(person.age)
            positions.append(person.position)

        genders.append("children")
        genders.append("adult")

        for localization in parseur.localizations:
            knowledge_service.add("knowledge", localization.name, "isintheroom", localization.room)
            knowledge_service.add("knowledge", localization.name, "isPlacement", localization.placement)
            knowledge_service.add("knowledge", localization.name, "isBeacon", localization.beacon)
            localizationsBeacon.append(localization.name)



        topf_path = topf_path.decode('utf-8')
        topic = self.ALDialog.loadTopic(topf_path.encode('utf-8'))
        # -------------- TO MODIFY ----------------------

        # Start dialog
        self.ALDialog.subscribe('myModule')

        # Activate dialog
        self.ALDialog.activateTopic(topic)

        self.ALDialog.setConcept("object", "English", objects)
        self.ALDialog.setConcept("category", "English", categories)
        self.ALDialog.setConcept("type", "English", types)
        self.ALDialog.setConcept("color", "English", colors)
        self.ALDialog.setConcept("room", "English", rooms)
        self.ALDialog.setConcept("shape", "English", shapes)
        self.ALDialog.setConcept("size", "English", sizes)
        self.ALDialog.setConcept("weight", "English", weights)
        self.ALDialog.setConcept("localization", "English", localizations)
        self.ALDialog.setConcept("localizationBeacon", "English", localizationsBeacon)
        print(self.ALDialog.getConcept("localizationBeacon","English"))

        self.ALDialog.setConcept("allAttributs", "English", categories)
        self.ALDialog.addToConcept("allAttributs", "English", types)
        self.ALDialog.addToConcept("allAttributs", "English", colors)
        self.ALDialog.addToConcept("allAttributs", "English", rooms)
        self.ALDialog.addToConcept("allAttributs", "English", localizations)

        self.ALDialog.setConcept("person", "English", persons)
        self.ALDialog.setConcept("gender", "English", genders)
        self.ALDialog.setConcept("age", "English", ages)
        self.ALDialog.setConcept("position", "English", positions)

        self.ALDialog.addToConcept("allPersonsAttributs", "English", persons)
        self.ALDialog.addToConcept("allPersonsAttributs", "English", genders)
        self.ALDialog.addToConcept("allPersonsAttributs", "English", ages)
        self.ALDialog.addToConcept("allPersonsAttributs", "English", positions)


