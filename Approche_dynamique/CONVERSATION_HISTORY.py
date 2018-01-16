# -*- encoding: UTF-8 -*-
""" Say 'hello, you' each time a human face is detected

"""

import sys
import time

from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

from optparse import OptionParser

NAO_IP = "localhost"
NAO_PORT = 62526
topf_path = 'C:\\Users\\aurel\\Documents\\COURS\\CPE\\Robotique\\PROJET_MAJEUR\\IHM_PEPPER_CPE2017\\Approche_dynamique\\top\\concept.top'
name_of_test = "ORIGINAL"

# Global variable to store the HumanGreeter module instance
HumanGreeter = None
memory = None
dialog_p = None
answer_given = False

class HumanGreeterModule(ALModule):
    def __init__(self, name, topf_path):
        ALModule.__init__(self, name)

        # Must be an absolute path
        self.topic_path = topf_path

        self.questions = []
        self.questions_understood = []
        self.answers_given = []

        global memory
        memory = ALProxy("ALMemory")
        memory.subscribeToEvent("Dialog/LastAnswer",
            "HumanGreeter",
            "onLastAnswer")


    def onLastAnswer(self, *_args):

        global answer_given
        answer_given = True # We have an answer from the robot
        memory.unsubscribeToEvent("Dialog/LastAnswer",
            "HumanGreeter")

        self.questions_understood.append(memory.getData("Dialog/LastInput"))
        self.answers_given.append(memory.getData("Dialog/LastAnswer"))

        # Subscribe again to the event
        memory.subscribeToEvent("Dialog/LastAnswer",
            "HumanGreeter",
            "onLastAnswer")

    def set_dialogue(self):
        global dialog_p, answer_given
        synchronisation = False # initialize the global variable
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

        input = ""
        while input != "EXIT":
            input = raw_input(u"Enter your question. Write EXIT to exit : ")

            if input != "EXIT":
                if answer_given == False:
                    self.questions.append(input)
                    self.questions_understood.append("Nothing understood")
                    self.answers_given.append("No answer from the robot")

                if answer_given:
                    self.questions.append(input)
                    answer_given = False


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

    myBroker = ALBroker("myBroker",
       "0.0.0.0",   # listen to anyone
       0,           # find a free port and use it
       pip,         # parent broker IP
       pport)       # parent broker port

    global topf_path
    global name_of_test
    global HumanGreeter
    HumanGreeter = HumanGreeterModule("HumanGreeter", topf_path)

    HumanGreeter.set_dialogue()

    log_file_name = "./TEST/TEST_" + name_of_test + "_" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
    log_file = open(log_file_name,'w')
    # Print the history of the dialog with the robot and save it into a log file
    print "_________HISTORIQUE DE LA DISCUSSION___________"
    i = 1
    for question, question_understood, answer in zip(HumanGreeter.questions, HumanGreeter.questions_understood, HumanGreeter.answers_given):
        print "Question asked by human was : " + question
        log_file.write("Question asked by human number %d : %s \n" % (i, question))
        print "Question understood by pepper was : " + question_understood
        log_file.write("Question understood by pepper number %d : %s \n" %(i,question_understood))
        print "Answer of the robot : " + answer
        log_file.write("Answer of pepper number %d : %s \n" %(i,answer))
        log_file.write("------------------------------------------------ \n")
        i += 1
    print
    print "Interrupted by user, shutting down"
    myBroker.shutdown()
    sys.exit(0)

if __name__ == "__main__":
    main()