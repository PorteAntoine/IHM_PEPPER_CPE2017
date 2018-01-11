#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use ALKnowledge Module"""

import qi
import argparse
import sys

def main(session):
    """
    This example uses ALKnowledge module.
    """
    # Get the service ALKnowledge.

    knowledge_service = session.service("ALKnowledge")
    # Getting the service ALDialog
    ALDialog = session.service("ALDialog")

    knowledge_service.add("tutorial", "sky", "hasColor", "blue")
    knowledge_service.add("tutorial", "smurf", "hasColor", "white")
    #Get subjects
    result = knowledge_service.getSubject("tutorial", "hasColor", "blue")
    print result #Should print ['sky', 'smurf']

    #Get predicates
    result = knowledge_service.getPredicate("tutorial", "sky", "blue")
    print result #Should print ['hasColor']

    #Get objects
    result = knowledge_service.getObject("tutorial", "smurf", "hasColor")
    print result #Should print ['blue', 'white']

    #Update
    #result = knowledge_service.update("tutorial", "smurf", "hasColor", "red")
    #result = knowledge_service.getObject("tutorial", "smurf", "hasColor")
    #print result #Should print ['red']

    #Contains
    result = knowledge_service.contains("tutorial", "smurf", "hasColor", "red")
    print result #Should print True

    #Remove
    result = knowledge_service.remove("tutorial", "smurf", "hasColor", "red")
    result = knowledge_service.contains("tutorial", "smurf", "hasColor","red")
    print result #Should print False

    #Query
    result = knowledge_service.query("tutorial", "sky", "hasColor", "?")
    print "test"
    print result #Should print ['blue']
    topic_content = ('topic: ~example_topic_content()\n'
                       'language: enu\n'
                       'concept:(predicat) [color location]\n'
                       'concept:(object) [sky smurf]\n'
                        'u:(tell me what is your position) Sure. ^call(ALRobotPosture.getPosture())\n'
                        'c1:(_*) $1\n'
                       'u: (what is the _~predicat of the _~object) $currentObj = $2 $currentPredicat=$1 The $1 of the $2 is ^call(ALKnowledge.getObject("tutorial", $currentObj, "hasColor"))\n'
                       'c1:(_*) : $1\n'
                       'u: (hello) Hello I am pepper\n')

    # Loading the topics directly as text strings
    topic_name_1 = ALDialog.loadTopicContent(topic_content)

    # Activating the loaded topics
    ALDialog.activateTopic(topic_name_1)

    # Starting the dialog engine - we need to type an arbitrary string as the identifier
    # We subscribe only ONCE, regardless of the number of topics we have activated
    ALDialog.subscribe('my_dialog_example')
    try:
        raw_input("\nSpeak to the robot using rules from both the activated topics. Press Enter when finished:")
    finally:
        # stopping the dialog engine
        ALDialog.unsubscribe('my_dialog_example')
        # Reset knoledge
    result = knowledge_service.resetKnowledge("tutorial")
    # Deactivating all topics
    ALDialog.deactivateTopic(topic_name_1)

    # now that the dialog engine is stopped and there are no more activated topics,
    # we can unload all topics and free the associated memory
    ALDialog.unloadTopic(topic_name_1)
    print "unload done"
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
