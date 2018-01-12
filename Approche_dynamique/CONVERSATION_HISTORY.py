# -*- encoding: UTF-8 -*-
""" Say 'hello, you' each time a human face is detected

"""

import sys
import time
import datetime

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

NAO_IP = "localhost"
NAO_PORT = 54912
topf_path = 'C:\\Users\\aurel\\Documents\\COURS\\CPE\\Robotique\\PROJET_MAJEUR\\IHM_PEPPER_CPE2017\\Approche_dynamique\\top\\concept.top'

# Global variable to store the HumanGreeter module instance
HumanGreeter = None
memory = None
dialog_p = None


class HumanGreeterModule(ALModule):
    def __init__(self, name, topf_path):
        ALModule.__init__(self, name)

        # Must be an absolute path
        self.topic_path = topf_path

        self.questions = []
        self.answers = []

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

        # Subscribe again to the event
        memory.subscribeToEvent("Dialog/LastAnswer",
            "HumanGreeter",
            "onLastAnswer")

    def set_dialogue(self):
        global dialog_p
        dialog_p = ALProxy('ALDialog')
        dialog_p.setLanguage("English")

        # Load the topic by it path
        global topf_path
        topf_path = topf_path.decode('utf-8')
        topic = dialog_p.loadTopic(topf_path.encode('utf-8'))

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
        pport=NAO_PORT)

    (opts, args_) = parser.parse_args()
    pip   = opts.pip
    pport = opts.pport

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
    topf_path = 'C:\\Users\\aurel\\Documents\\COURS\\CPE\\Robotique\\PROJET_MAJEUR\\IHM_PEPPER_CPE2017\\Approche_dynamique\\top\\concept.top'
    global HumanGreeter
    HumanGreeter = HumanGreeterModule("HumanGreeter", topf_path)

    HumanGreeter.set_dialogue()

    log_file_name = "TEST_" + "NAME_OF_THE_TEST" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    log_file = open(log_file_name,'w')
    # Print the history of the dialog with the robot and save it into a log file
    print "_________HISTORIQUE DE LA DISCUSSION___________"
    i = 1
    for question, answer in zip(HumanGreeter.questions, HumanGreeter.answers):
        print "Last thing understood by pepper was : " + question
        log_file.write("Input number %d : %s \n" %(i,question))
        print "Output of the robot : " + answer
        log_file.write("Output number %d : %s : \n" %(i,answer))
        i =+ 1
    print
    print "Interrupted by user, shutting down"
    myBroker.shutdown()
    sys.exit(0)

if __name__ == "__main__":
    main()