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
    types=[]
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
        types.append(objects.type)
    for person in parseur.persons:
        knowledge_service.add("knowledge", person.name, "isofgender", person.gender)
        knowledge_service.add("knowledge", person.name, "isoftheageof", person.age)
        knowledge_service.add("knowledge", person.name, "islocated", person.position)

    topic_content = ('topic: ~firstStep()\n'
                     'language: enu\n'
                     'concept:(located) [room situated placed located find]\n'
                     'concept:(where_is) ["where is" where''s'' "where are" "where can I"]\n'
                     'concept:(can_you)[ "[can will could] you {please}" "do you think you could" "are you [ready able] to" "do you know how to"]\n'
                     'concept:(what_is) ["{"~can_you tell me" "do you know" "tell me"} [ what''s''  "what [is are was were]"]" ]\n'
                     'concept:(which_is) [~what_is "which is" "which"]\n'
-                    'concept: (heaviest) [heaviest "most important weigth"]\n'
                     'concept:(location) [localization location postition room]\n'
                     'dynamic: object\n'
                     'dynamic: category\n'
                     'dynamic: type\n'
                     'dynamic: localization\n'
    
                     #De quelle couleur est l'objet
                     'u: (~what_is {the} color {of} {the} _~object) $currentObject = $1 The color of the $currentObject is ^call(ALKnowledge.getObject("knowledge", $currentObject, "hasColor"))\n'
                     'c1:(_*)  $1\n'
                     #ou est l'objet
                     'u: (["~where_is {~located}" "~what_is {the} ~location"] {of} {the} _~object) $currentObject = $1 The $currentObject is ^call(ALKnowledge.getObject("knowledge", $currentObject, "isintheroom")) ^call(ALKnowledge.getObject("knowledge", $currentObject, "islocated"))\n'
                     'c1:(_*) in the $1\n'
                     # a quelle categorie appartient l'object 
                     'u:(~what_is * category * ~object) $currentObject = $1 The category of $currentObject is ^call(ALKnowledge.getObject("knowledge", $currentObject, "belongstocategory"))\n'
                     'c1:(_*)  $1\n'
                     # Ou puis-je trouver un objet d'une categorie specifique
                     # Quel objet d'une categorie est le plus lourd. 
                     'u: (which is the heaviest _~category) the heaviest $1 ^call(ALKnowledge.getSubject("knowledge", "belongstocategory",$1))\n'
                     'c1:(_*) is ^call(ProcessObjectModule.heaviest($1))\n'
                     'c2:(_*) $1 \n'
    
                     # Quel objet d'un type est le plus lourd. 
                     'u: (~which_is {the} ~heaviest _~type) the heaviest $1 ^call(ALKnowledge.getSubject("knowledge", "isoftype",$1))\n'
                     'c1:(_*) is ^call(ProcessObjectModule.heaviest($1))\n'

                     'u: (which is the lightest _~category) the lightest $1 ^call(ALKnowledge.getSubject("knowledge", "belongstocategory",$1))\n'
                     'c1:(_*) is ^call(ProcessObjectModule.lightest($1))\n'
                     'c2:(_*) $1 \n'
    
                     'u: (which is the biggest _~category) the biggest $1 ^call(ALKnowledge.getSubject("knowledge", "belongstocategory",$1))\n'
                     'c1:(_*) is ^call(ProcessObjectModule.biggest($1))\n'
                     'c2:(_*) $1 \n'
    
                     'u: (which is the most little _~category) the most little $1 ^call(ALKnowledge.getSubject("knowledge", "belongstocategory",$1))\n'
                     'c1:(_*) is ^call(ProcessObjectModule.little($1))\n'
                     'c2:(_*) $1 \n'
    
                     'u: (do _~object and _~object belong to the same category)  it is ^call(ProcessObjectModule.sameCategory($1,$2))\n'
                     'c1:(_*) $1 \n'
                     
                     'u: ([Hi Hello]) Hello Human\n')


    # Loading the topics directly as text strings
    topic_name_1 = ALDialog.loadTopicContent(topic_content)

    # Activating the loaded topics
    ALDialog.activateTopic(topic_name_1)

    # Starting the dialog engine - we need to type an arbitrary string as the identifier
    # We subscribe only ONCE, regardless of the number of topics we have activated
    ALDialog.subscribe('my_dialog_example')
    ALDialog.setConcept("object", "English", objects)
    ALDialog.setConcept("category", "English", categories)
    ALDialog.setConcept("type", "English", types)


    try:
        raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:\n")
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
    parser.add_argument("--ip", type=str, default="169.254.147.43",
                        help="Robot IP address. On robot or Local Naoqi: use 192.168.1.201.")

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
