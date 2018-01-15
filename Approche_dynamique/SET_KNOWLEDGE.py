from CSV_PARSEUR import CSV_PARSEUR
import qi
import argparse
import sys
from CSV_PARSEUR import CSV_PARSEUR
from Process_object import Process_object
from Utils import Utils
from Process_Object_Module import ProcessObjectModule


def main(session):

    ALDialog = session.service("ALDialog")
    ALDialog.stopTopics(ALDialog.getAllLoadedTopics())

    #    ALDialog.setLanguage("English")
    knowledge_service = session.service("ALKnowledge")
    memory_service= session.service("ALMemory")
    parseur = CSV_PARSEUR("list_objects_final.csv","list_objects_final.csv")

    processObject= ProcessObjectModule(session,parseur)
    session.registerService("ProcessObjectModule", processObject)
    utils=Utils()
    objects = []
    categories = []
    types = []
    colors = []
    localizations = []
    #memory_service.insertData("returnList", [])
   # heaviestlist = memory_service.getData("heaviestlist")

    #returnList = memory_service.getData("returnList")
    for object in parseur.objects:
        knowledge_service.add("knowledge", object.name, "hasColor", object.color)
        knowledge_service.add("knowledge", object.name, "isoftype", object.type)
        knowledge_service.add("knowledge", object.name, "belongstocategory", object.category)
        knowledge_service.add("knowledge", object.name, "islocated", object.localization)
        knowledge_service.add("knowledge", object.name, "isintheroom", object.room)
        knowledge_service.add("knowledge", object.name, "hasColor", object.color)
        knowledge_service.add("knowledge", object.name, "hasShape", object.shape)
        knowledge_service.add("knowledge", object.name, "size", object.size)
        knowledge_service.add("knowledge", object.name, "weight", object.weight)
        objects.append(object.name)
        #TODO creer un parseur pour les categories.
        categories.append(object.category)
        types.append(object.type)
        colors.append(object.color)
    for person in parseur.persons:
        knowledge_service.add("knowledge", person.name, "isofgender", person.gender)
        knowledge_service.add("knowledge", person.name, "isoftheageof", person.age)
        knowledge_service.add("knowledge", person.name, "islocated", person.position)

    topic_path = "C:/Users/astro/Documents/projetmaj/IHM_PEPPER_CPE2017/Approche_dynamique/main_topic_enu.top"
    topic_path = topic_path.decode('utf-8')
    topic = ALDialog.loadTopic(topic_path.encode('utf-8'))
    ALDialog.subscribe('myModule')
    ALDialog.activateTopic(topic)


    # Loading the topics directly as text strings
    #topic_name_1 = ALDialog.loadTopicContent(topic_content)

    # Activating the loaded topics
    #ALDialog.activateTopic(topic_name_1)

    # Starting the dialog engine - we need to type an arbitrary string as the identifier
    # We subscribe only ONCE, regardless of the number of topics we have activated
    #ALDialog.subscribe('my_dialog_example')
    ALDialog.setConcept("object", "English", objects)
    ALDialog.setConcept("category", "English", categories)
    ALDialog.setConcept("type", "English", types)
    ALDialog.setConcept("color", "English", colors)


    try:
        raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:\n")
    finally:

        # stopping the dialog engine
        ALDialog.unsubscribe('myModule')
        # Reset knoledge

    result = knowledge_service.resetKnowledge("knowledge")
    # Deactivating all topics
    ALDialog.deactivateTopic(topic)
    ALDialog.unloadTopic(topic)
    print "unload done"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="localhost",
                        help="Robot IP address. On robot or Local Naoqi: use 192.168.1.201.")

    parser.add_argument("--port", type=int, default=60714,                   help="Naoqi port number")
    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
