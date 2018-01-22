#!/usr/bin/env python
# -*- coding: utf-8 -*-

# run with python 03_...py --qi-url="tcp://ip_robot:9559"

import qi
from Process_person import Process_person
from Utils import Utils
class ProcessPersonModule:
    """
        Wow, there should be some doc here too
    """
    def __init__(self, session, parseur):
        print "MyModule Persons init"
        self.session = session
        self.parseur = parseur
        self.utils = Utils()
        self.processPerson=Process_person()
        self.tts=session.service("ALTextToSpeech")

    def numberAttribute(self, attr):
        print "MyModule process the number of persons having the attribute ", "<", attr, ">"
        result = ""
        result = self.processPerson.hasAttribute(self.parseur.persons, attr)
        return str(len(result))

    def numberTwoAttribute(self, attr1, attr2):
        print "MyModule process the number of persons having the attributes ", "<", attr1, "> and <", attr2, ">"
        result = ""
        result = self.processPerson.hasTwoAttribute(self.parseur.persons, attr1, attr2)
        return str(len(result))

    def hasAttribute(self, attr):
        print "MyModule process the list of persons having the attribute ", "<", attr, ">"
        result = ""
        result = self.processPerson.hasAttribute(self.parseur.persons, attr)
        if not result:
            result = "nobody"
        return self.tts.say(str(result))

    def hasTwoAttribute(self, attr1, attr2):
        print "MyModule process the list of persons having the attributes ", "<", attr1, ">", " and ", "<", attr2, ">"
        result = ""
        result = self.processPerson.hasTwoAttribute(self.parseur.persons, attr1, attr2)
        if not result:
            result = "nobody"
        return self.tts.say(str(result))

    def oldestattr(self, attr):
        print "MyModule process the oldest person in the list with this attr", "<", attr, ">"
        oldlist = self.processPerson.hasAttribute(self.parseur.persons, attr)
        resultOldest = ""
        resultOldest = self.processPerson.oldest(self.utils.getObjectListbyName(self.parseur.persons, str(oldlist)))
        return str(resultOldest)

    def youngestattr(self, attr):
        print "MyModule process the youngest person in the list with this attr", "<", attr, ">"
        younglist = self.processPerson.hasAttribute(self.parseur.persons, attr)
        resultYoungest = ""
        resultYoungest = self.processPerson.youngest(self.utils.getObjectListbyName(self.parseur.persons, str(younglist)))
        return str(resultYoungest)


    def oldest(self, listOfNames):
        print "MyModule process the oldest person in the list"
        resultoldest=""
        resultoldest = self.processPerson.oldest(self.utils.getObjectListbyName(self.parseur.persons, listOfNames))
        return str(resultoldest)

    def youngest(self, listOfNames):
        print "MyModule process the youngest person in the list"
        resultyoungest=""
        resultyoungest = self.processPerson.youngest(self.utils.getObjectListbyName(self.parseur.persons, listOfNames))
        return str(resultyoungest)

    def sameAge(self, name1, name2):
        print "MyModule process if ", "<", name1, "> and ", "<", name2, ">", " have the same age"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processPerson.sameAge(self.utils.getObjectListbyListName(self.parseur.persons, listofNames))
        return str(result)


    def sameGender(self, name1, name2):
        print "MyModule process if ", "<", name1, "> and ", "<", name2, ">", " have the same gender"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processPerson.sameGender(self.utils.getObjectListbyListName(self.parseur.persons, listofNames))
        return str(result)


    def samePosition(self, name1, name2):
        print "MyModule process if ", "<", name1, "> and ", "<", name2, ">", " have the same position"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processPerson.samePosition(self.utils.getObjectListbyListName(self.parseur.persons, listofNames))
        return str(result)