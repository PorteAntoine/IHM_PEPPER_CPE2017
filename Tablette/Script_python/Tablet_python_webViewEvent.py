import sys
import time

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
from naoqi import qi


from optparse import OptionParser

NAO_IP = "localhost"
robot_ip = "localhost"
robot_ip = "169.254.41.224"
robot_port = 9559
#robot_port = 55234

# Global variable to store the HumanGreeter module instance
HumanGreeter = None
memory = None
dialog_p = None


class HumanGreeterModule(ALModule):
    def __init__(self, name):
        ALModule.__init__(self, name)

        self.questions = []
        self.answers = []

        self.tts = ALProxy("ALTextToSpeech")

        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("Dialog/LastAnswer",
            "HumanGreeter",
            "onLastAnswer")


    def onLastAnswer(self, *_args):
        """ This will be called each time a face is
        detected.
        """
        # Unsubscribe to the event when talking,
        # to avoid repetitions
        memory.unsubscribeToEvent("Dialog/LastAnswer",
            "HumanGreeter")

        self.questions.append(memory.getData("Dialog/LastInput"))
        self.answers.append(memory.getData("Dialog/LastAnswer"))




        # AJOUT TABLETTE
        #---------------
        string = ""
        i=1
        memtab =  ALProxy("ALMemory", robot_ip, robot_port)

        # for Conversation_history
        for question, answer in zip(HumanGreeter.questions, HumanGreeter.answers):
            string += str(i) + "- " + question + "? " + answer + "<br>"
            i=i+1
        memtab.insertData("keyword_CH", string)

        # for show last input/answer
        string = memtab.getData("Dialog/LastInput") + "? " +memtab.getData("Dialog/LastAnswer")
        memtab.insertData("keyword_typed", string)
        
        #Load URL Web page tablet
        tabletservice = ALProxy("ALTabletService", robot_ip, robot_port)
        tabletservice.showWebview("http://198.18.0.1/apps/tablette_test/index2.html")
        # FIN AJOUT TABLETTE
        #---------------




        # Subscribe again to the event
        memory.subscribeToEvent("Dialog/LastAnswer",
            "HumanGreeter",
            "onLastAnswer")

        

        

    def set_dialogue(self):
        global dialog_p
        dialog_p = ALProxy('ALDialog')
        #dialog_p.setLanguage("English")
        # stop topic active (pose probleme sinon en programmation)
        dialog_p.stopTopics( dialog_p.getAllLoadedTopics())
    
        # Load topic - absolute path is required
        topic = ('topic: ~example_topic_content()\n'
                           'language: enu\n'
                           'u: (how are you today) Hello human, I am fine thank you and you?\n'
                           'u: (What is your name) My name is Brian\n')

        topic = dialog_p.loadTopicContent(topic)

        # Start dialog
        dialog_p.subscribe('myModule')

        # Activate dialog
        dialog_p.activateTopic(topic)

        raw_input(u"Press 'Enter' to exit.")

        # Deactivate topic
        dialog_p.deactivateTopic(topic)

        # Unload topic
        dialog_p.unloadTopic(topic)

        # Stop dialog
        dialog_p.unsubscribe('myModule')


def main():
    """ Main entry point
    """
    parser = OptionParser()
    parser.add_option("--pip",
        help="Parent broker port. The IP address or your robot",
        dest="pip")
    parser.add_option("--pport",
        help="Parent broker port. The port NAOqi is listening to",
        dest="pport",
        type="int")
    parser.set_defaults(
        pip=NAO_IP,
        pport=51177)

    (opts, args_) = parser.parse_args()
    pip   = robot_ip
    pport = robot_port
    
    
    
    # We need this broker to be able to construct
    # NAOqi modules and subscribe to other modules
    # The broker must stay alive until the program exists
    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       pip,         # parent broker IP
       pport)       # parent broker port

    
    
    # Warning: HumanGreeter must be a global variable
    # The name given to the constructor must be the name of the
    # variable
    global HumanGreeter
    HumanGreeter = HumanGreeterModule("HumanGreeter")

    HumanGreeter.set_dialogue()

    
    print "_________HISTORIQUE DE LA DISCUSSION___________"
    for question, answer in zip(HumanGreeter.questions, HumanGreeter.answers):
        print "Question understood by pepper : " + question
        print "Answer of the robot : " + answer

    print
    print "Interrupted by user, shutting down"
    myBroker.shutdown()
    sys.exit(0)

if __name__ == "__main__":
    main()
