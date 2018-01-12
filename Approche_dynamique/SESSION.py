from CSV_PARSEUR import CSV_PARSEUR
import qi
import argparse
import sys
from naoqi import ALProxy

memory = None

class SESSION():

    def __init__(self, IP, port):
        self.objects = []
        self.session = self.init_session(IP, port)
        self.historique = []
        # Service initialisation
        self.knowledge_service = self.session.service("ALKnowledge")
        self.ALDialog = self.session.service("ALDialog")
        self.questions = []
        self.answers = []
        self.topic()
        self.set_knowledge()
        self.start_dialogue()

        global memory
        memory = ALProxy("ALMemory")

        memory.subscribeToEvent("Dialog/LastInput", "HumanGreeter", "onLastInput")

    def onLastInput(self, *_args):
        print("I am in the loop")
        memory.unsubscribeToEvent("Dialog/LastInput",
            "HumanGreeter")
        print(memory.getData(["Dialog/LastInput"]))
        # Subscribe again to the event
        memory.subscribeToEvent("Dialog/LastInput",
            "HumanGreeter",
            "onLastInput")

    # this function initialize the session
    def init_session(self, IP, port):
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", type=str, default=IP,
                            help="Robot IP address. On robot or Local Naoqi: use '169.254.85.73'.")

        parser.add_argument("--port", type=int, default=port, help="Naoqi port number")

        args = parser.parse_args()
        session = qi.Session()
        try:
            session.connect("tcp://" + args.ip + ":" + str(args.port))
        except RuntimeError:
            print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) + ".\n"
                                                                                                  "Please check your script arguments. Run with -h option for help.")
            sys.exit(1)
        print("Session started")
        return session

    # this function initialize the topic
    def topic(self):
        self.topic_content = ('topic: ~firstStep()\n'
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

    # this function reset the knowledge
    def reset_knowledge(self):
        self.knowledge_service.resetKnowledge("knowledge")

    # this function set the knowledge
    def set_knowledge(self):

        parseur = CSV_PARSEUR("list_objects_final.csv", "list_objects_final.csv")
        for object in parseur.objects:
            self.knowledge_service.add("knowledge", object.name, "hasColor", object.color)
            self.knowledge_service.add("knowledge", object.name, "isoftype", object.type)
            self.knowledge_service.add("knowledge", object.name, "belongstocategory", object.category)
            self.knowledge_service.add("knowledge", object.name, "islocated", object.localization)
            self.knowledge_service.add("knowledge", object.name, "isintheroom", object.room)
            self.knowledge_service.add("knowledge", object.name, "hasColor", object.color)
            self.knowledge_service.add("knowledge", object.name, "hasShape", object.shape)
            self.knowledge_service.add("knowledge", object.name, "size", object.size)
            self.knowledge_service.add("knowledge", object.name, "weight", object.weight)
            self.objects.append(object.name)

        for person in parseur.persons:
            self.knowledge_service.add("knowledge", person.name, "isofgender", person.gender)
            self.knowledge_service.add("knowledge", person.name, "isoftheageof", person.age)
            self.knowledge_service.add("knowledge", person.name, "islocated", person.position)

    # this function start the dialogue
    def start_dialogue(self):

        # Loading the topics directly as text strings
        topic = self.ALDialog.loadTopicContent(self.topic_content)

        # Activating the loaded topics
        self.ALDialog.activateTopic(topic)

        # Starting the dialog engine - we need to type an arbitrary string as the identifier
        # We subscribe only ONCE, regardless of the number of topics we have activated
        self.ALDialog.subscribe('dialog_stage_1')
        self.ALDialog.setConcept("object", "English", self.objects)
        while(1):
            raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:")

        # stopping the dialog engine
        self.ALDialog.unsubscribe('my_dialog_example')
        # Reset knoledge
        self.reset_knowledge()
        # Deactivating all topics
        self.ALDialog.deactivateTopic(topic)
        self.ALDialog.unloadTopic(topic)
        print "unload done"

if __name__=='__main__':

    session = SESSION(IP="192.168.1.201", port=9559)
