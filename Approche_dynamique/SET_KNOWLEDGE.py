from CSV_PARSEUR import CSV_PARSEUR
import qi
import argparse
import sys


def main(session):

    ALDialog = session.service("ALDialog")

    #    ALDialog.setLanguage("English")
    knowledge_service = session.service("ALKnowledge")

    parseur = CSV_PARSEUR()
    parseur.object_transformations("list_objects_final.csv")
    #parseur.person_transformations("list_person_final.csv")
    objects = []
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

    for person in parseur.persons:
        knowledge_service.add("knowledge", person.name, "isofgender", person.gender)
        knowledge_service.add("knowledge", person.name, "isoftheageof", person.age)
        knowledge_service.add("knowledge", person.name, "islocated", person.position)
    


    print(knowledge_service.getObject("knowledge", "Cup", "hasColor"))


    topic_content = ('topic: ~firstStep()\n'
                     'language: enu\n'
                     'concept:(where) [where localization location situation room situated placed located find "in which"]\n'
                     'dynamic: object\n'
                     'dynamic: type\n'
                     'dynamic: category\n'
                     'dynamic: localization\n'
                     'dynamic: room\n'
                     'dynamic: color\n'
                     'u: (what is the color of _~object) $currentObject = $1 The color of the $currentObject is ^call(ALKnowledge.getObject("knowledge", $currentObject, "hasColor"))\n'
                     'c1:(_*) : $1\n'
                     'u: (~where _~object) $currentObject = $1 The $currentObject is in the ^call(ALKnowledge.getObject("knowledge", $currentObject, "isLocated"))\n'
                     'c1:(_*) : $1\n'
                     'u: (Hi) Hello human, I am fine thank you and you?\n')

    # Loading the topics directly as text strings
    topic_name_1 = ALDialog.loadTopicContent(topic_content)

    # Activating the loaded topics
    ALDialog.activateTopic(topic_name_1)

    # Starting the dialog engine - we need to type an arbitrary string as the identifier
    # We subscribe only ONCE, regardless of the number of topics we have activated
    ALDialog.subscribe('my_dialog_example')
    ALDialog.setConcept("object", "English", objects)
    try:
        raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:")
    finally:
        # stopping the dialog engine
        ALDialog.unsubscribe('my_dialog_example')
        # Reset knoledge
    result = knowledge_service.resetKnowledge("knowledge")
    # Deactivating all topics
    ALDialog.deactivateTopic(topic_name_1)
    ALDialog.unloadTopic(topic_name_1)
    print "unload done"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.201",
                        help="Robot IP address. On robot or Local Naoqi: use '169.254.85.73'.")

    parser.add_argument("--port", type=int, default=9559,                   help="Naoqi port number")
    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
