# -*- encoding: UTF-8 -*-
""" Say 'hello, you' each time a human face is detected

"""

import sys
import argparse
from SET_KNOWLEDGE import defineDialog
import qi

# from akinator import Answerthequestion

NAO_IP = "169.254.89.161"
NAO_PORT = "9559"
topf_path ="/home/nao/naoqi/topic_pack/main/main_topic_enu.top"

# Global variable to store the HumanGreeter module instance
def main(session,topf_path):
    dialog_p = session.service('ALDialog')
    dialog_p.setLanguage("English")
    topf_path = topf_path.decode('utf-8')
    topic = dialog_p.loadTopic(topf_path.encode('utf-8'))
    setKnowledge = defineDialog(session, dialog_p)
    setKnowledge.set_knowledge(topf_path)
    try:
        raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:\n")
    finally:
        # stopping the dialog engine
        dialog_p.unsubscribe('myModule')
        # Reset knoledge
    # Deactivating all topics
    dialog_p.deactivateTopic(topic)

    # now that the dialog engine is stopped and there are no more activated topics,
    # we can unload all topics and free the associated memory
    dialog_p.unloadTopic(topic)

    print "unload done"
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=51926,                   help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + NAO_IP + ":" + NAO_PORT)
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session,topf_path)
