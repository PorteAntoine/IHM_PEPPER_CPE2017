# -*- encoding: UTF-8 -*-
""" Say 'hello, you' each time a human face is detected

"""

import sys
import time
import subprocess
from SET_KNOWLEDGE import defineDialog
import qi

from naoqi import ALProxy

from optparse import OptionParser
# from akinator import Answerthequestion

NAO_IP = "192.168.1.201"
NAO_PORT = "9559"
topf_path = '/home/nao/naoqi/topic_pack/main/main_topic_enu.top'
name_of_test = "APPROCHE_DYNAMIQUE"
text_file_question_path = 'D:/ProjetMajeur/IHM_PEPPER_CPE2017/Approche_dynamique/TEXT_TEST_FILE/1_questions_objets.txt'

# Global variable to store the HumanGreeter module instance
HumanGreeter = None
memory = None
dialog_p = None
answer_given = False

class HumanGreeterModule():
    def __init__(self, session):
        # Must be an absolute path

        #ALModule.__init__(self, name)
        self.topic_path = topf_path

        self.session = session

        self.questions = []
        self.questions_understood = []
        self.answers_given = []

        global memory
        memory = self.session.service("ALMemory")
        session.registerService("HumanGreeterModule", self)
        memory.subscribeToEvent("Dialog/LastAnswer",
            "HumanGreeterModule",
            "onLastAnswer")


    def onLastAnswer(self, *_args):

        global answer_given
        answer_given = True # We have an answer from the robot
        memory.unsubscribeToEvent("Dialog/LastAnswer",
            "HumanGreeterModule")

        self.questions_understood.append(memory.getData("Dialog/LastInput"))
        self.answers_given.append(memory.getData("Dialog/LastAnswer"))

        # Subscribe again to the event
        memory.subscribeToEvent("Dialog/LastAnswer",
            "HumanGreeterModule",
            "onLastAnswer")

    def set_dialogue(self):
        global dialog_p, answer_given
        demarrage = True
        log_file_name = "./TEST/TEST_" + name_of_test + "_" + time.strftime("%Y%m%d-%H%M%S") + ".txt"
        log_file = open(log_file_name, 'w')
        synchronisation = False # initialize the global variable
        dialog_p = self.session.service('ALDialog')
        dialog_p.setLanguage("English")

        # # Load the topic by it path
        global topf_path
        topf_path = topf_path.decode('utf-8')
        topic = dialog_p.loadTopic(topf_path.encode('utf-8'))
        # # -------------- TO MODIFY ----------------------
        #
        # # Start dialog
        # dialog_p.subscribe('myModule')
        #
        # # Activate dialog
        # dialog_p.activateTopic(topic)

       # #Call the dialog class
        setKnowledge = defineDialog(self.session, dialog_p)
        setKnowledge.set_knowledge()


        test_file = open(text_file_question_path,'r')
        lines = test_file.read().splitlines()
        i = 0
        erreur = 0
        for line in lines:
            reply = subprocess.Popen([r'C:\Program Files (x86)\balcon\balcon.exe', "-n", "Microsoft Zira Desktop",
                                          "-t", line],
                                         universal_newlines=True,
                                         stdout=subprocess.PIPE).communicate()

            time.sleep(5)

            if answer_given == False:
                self.questions.append(line)
                self.questions_understood.append("Nothing understood")
                self.answers_given.append("No answer from the robot")
                erreur += 1

            if answer_given:
                self.questions.append(line)
                answer_given = False
                # if self.answers_given[i] == Answerthequestion(line).answer():
                #     erreur += 1

            print "Question asked by human was : " + self.questions[i]
            log_file.write("Question asked by human number %d : %s \n" % (i+1, self.questions[i]))
            print "Question understood by pepper was : " + self.questions_understood[i]
            log_file.write("Question understood by pepper number %d : %s \n" % (i+1, self.questions_understood[i]))
            print "Answer of the robot : " + self.answers_given[i]
            log_file.write("Answer of pepper number %d : %s \n" % (i+1, self.answers_given[i]))
            print "-------------------------------------------------------"
            log_file.write("------------------------------------------------ \n")
            log_file.flush()
            i += 1

        log_file.write("Number of error : ")
        log_file.write("Percentage : ")
        log_file.write("--------------FIN DU TEST-------------------------------------")
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

    # myBroker = ALBroker("myBroker",
    #    "0.0.0.0",   # listen to anyone
    #    0,           # find a free port and use it
    #    pip,         # parent broker IP
    #    pport)       # parent broker port

    session = qi.Session()

    try:
        session.connect("tcp://" + NAO_IP + ":" + NAO_PORT)
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + NAO_IP + "\" on port " + NAO_PORT + ".\n"
                                                                                              "Please check your script arguments. Run with -h option for help.")

    reply = subprocess.Popen([r'C:\Program Files (x86)\balcon\balcon.exe', "-n", "Microsoft Zira Desktop",
                              "-t", "Starting the test"],
                             universal_newlines=True,
                             stdout=subprocess.PIPE).communicate()
    global topf_path
    global name_of_test
    global HumanGreeter
    HumanGreeter = HumanGreeterModule(session)
    HumanGreeter.set_dialogue()

    reply = subprocess.Popen([r'C:\Program Files (x86)\balcon\balcon.exe', "-n", "Microsoft Zira Desktop",
                              "-t", "This is the end of the test"],
                             universal_newlines=True,
                             stdout=subprocess.PIPE).communicate()
    print
    print "Interrupted by user, shutting down"
    #myBroker.shutdown()
    sys.exit(0)

if __name__ == "__main__":
    main()