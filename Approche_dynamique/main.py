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

NAO_IP = "localhost"
NAO_PORT = "61315"
topf_path = 'C:/Users/astro/Desktop/Approche_dynamique/main_topic_enu.top'
name_of_test = "APPROCHE_DYNAMIQUE"
text_file_question_path = 'C:/Users/astro/Desktop/Approche_dynamique/TEXT_TEST_FILE/test_objets.txt'

# Global variable to store the HumanGreeter module instance
def main(session)
	    dialog_p = session.service('ALDialog')
        dialog_p.setLanguage("English")
		setKnowledge = defineDialog(session, dialog_p)
        setKnowledge.set_knowledge()
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=51926,                   help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
	main(session)
