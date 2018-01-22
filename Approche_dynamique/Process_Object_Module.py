#!/usr/bin/env python
# -*- coding: utf-8 -*-

# run with python 03_...py --qi-url="tcp://ip_robot:9559"

import qi
from Process_object import Process_object
from Utils import Utils
class ProcessObjectModule:
    """
    Wow, there should be some doc here too
    """
    def __init__(self, session,parseur):
        """
        """
        print "MyModule Objects init"
        self.session = session
        self.parseur = parseur
        self.utils = Utils()
        self.processObject=Process_object()
        self.tts=session.service("ALTextToSpeech")

    def numberAttribute(self, attr):
        print "MyModule process the number of objects having the attribute ", "<" , attr , ">"
        result = ""
        result = self.processObject.hasAttribute(self.parseur.objects, attr)
        return str(len(result))

    def numberTwoAttribute(self, attr1, attr2):
        print "MyModule process the number of objects having the attributes ", "<" , attr1 , "> and <", attr2, ">"
        result = ""
        result = self.processObject.hasTwoAttribute(self.parseur.objects, attr1, attr2)
        return str(len(result))

    def hasAttribute(self, attr):
        print "MyModule process the list of object having the attribute ", "<" , attr , ">"
        result = ""
        result = self.processObject.hasAttribute(self.parseur.objects, attr)
        if not result:
            result = "nothing"
        return self.tts.say(str(result))

    def hasTwoAttribute(self, attr1, attr2):
        print "MyModule process the list of objects having the attributes " , "<" , attr1 , ">", " and " , "<" , attr2 , ">"
        result = ""
        result = self.processObject.hasTwoAttribute(self.parseur.objects, attr1, attr2)
        if not result:
            result = "nothing"
        return self.tts.say(str(result))

    def boolAttribute(self, listOfNames, attr):
        print "MyModule process if the list of names have the same attribute ", "<" , attr , ">"
        result = ""
        result = self.processObject.boolAttribute(self.utils.getObjectListbyName(self.parseur.objects, listOfNames),attr)
        return str(result)

    def sameCategory(self, name1, name2):
        print "MyModule process if ", "<", name1, "> and ", "<", name2, ">", " are in the same category"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processObject.sameCategory(self.utils.getObjectListbyListName(self.parseur.objects,listofNames))
        return str(result)

    def heavyName(self, name1, name2):
        print "MyModule process the heaviest object between ", "<", name1, "> and ", "<", name2, ">"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processObject.heaviest(self.utils.getObjectListbyListName(self.parseur.objects,listofNames))
        return str(result)

    def lightName(self, name1, name2):
        print "MyModule process the lightest object between ", "<", name1, "> and ", "<", name2, ">"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processObject.lightest(self.utils.getObjectListbyListName(self.parseur.objects,listofNames))
        return str(result)

    def littleName(self, name1, name2):
        print "MyModule process the smallest object between ", "<", name1, "> and ", "<", name2, ">"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processObject.little(self.utils.getObjectListbyListName(self.parseur.objects,listofNames))
        return str(result)

    def bigName(self, name1, name2):
        print "MyModule process the biggest object between ", "<", name1, "> and ", "<", name2, ">"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processObject.biggest(self.utils.getObjectListbyListName(self.parseur.objects,listofNames))
        return str(result)

    def sameType(self, name1, name2):
        print "MyModule process if ", "<", name1, "> and ", "<", name2, ">", " have the same type"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processObject.sameType(self.utils.getObjectListbyListName(self.parseur.objects,listofNames))
        return str(result)

    def sameRoom(self, name1, name2):
        print "MyModule process if ", "<", name1, "> and ", "<", name2, ">", " are in the same room"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processObject.sameRoom(self.utils.getObjectListbyListName(self.parseur.objects,listofNames))
        return str(result)

    def sameColor(self, name1, name2):
        print "MyModule process if ", "<", name1, "> and ", "<", name2, ">", " have the same color"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processObject.sameColor(self.utils.getObjectListbyListName(self.parseur.objects,listofNames))
        return str(result)

    def sameWeight(self, name1, name2):
        print "MyModule process if ", "<", name1, "> and ", "<", name2, ">", " have the same weight"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processObject.sameWeight(self.utils.getObjectListbyListName(self.parseur.objects,listofNames))
        return str(result)

    def sameSize(self, name1, name2):
        print "MyModule process if ", "<", name1, "> and ", "<", name2, ">", " have the same size"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processObject.sameSize(self.utils.getObjectListbyListName(self.parseur.objects,listofNames))
        return str(result)

    def sameLocalization(self, name1, name2):
        print "MyModule process if ", "<", name1, "> and ", "<", name2, ">", " have the same localization"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processObject.sameLocalization(self.utils.getObjectListbyListName(self.parseur.objects,listofNames))
        return str(result)

    def heaviest(self, listOfNames):
        print "MyModule process the heaviest object in the list"
        resultHeaviest=""
        resultHeaviest = self.processObject.heaviest(self.utils.getObjectListbyName(self.parseur.objects, listOfNames))
        return str(resultHeaviest)

    def lightest(self, listOfNames):
        print "MyModule process the lightest object in the list"
        resultlightest=""
        resultlightest = self.processObject.lightest(self.utils.getObjectListbyName(self.parseur.objects, listOfNames))
        return str(resultlightest)

    def biggest(self, listOfNames):
        print "MyModule process the biggest object in the list"
        resultbiggest=""
        resultbiggest = self.processObject.biggest(self.utils.getObjectListbyName(self.parseur.objects, listOfNames))
        return str(resultbiggest)

    def little(self, listOfNames):
        print "MyModule process the smallest object in the list"
        resultlittle=""
        resultlittle = self.processObject.little(self.utils.getObjectListbyName(self.parseur.objects, listOfNames))
        return str(resultlittle)

    def heaviestattr(self, attr):
        print "MyModule process the heaviest object in the list with this attr", "<", attr, ">"
        heavylist = self.processObject.hasAttribute(self.parseur.objects, attr)
        resultHeaviest = ""
        resultHeaviest = self.processObject.heaviest(self.utils.getObjectListbyName(self.parseur.objects, str(heavylist)))
        return str(resultHeaviest)

    def lightestattr(self, attr):
        print "MyModule process the lightest object in the list with this attr", "<", attr, ">"
        lightlist = self.processObject.hasAttribute(self.parseur.objects, attr)
        print lightlist
        resultLightest = ""
        resultLightest = self.processObject.lightest(self.utils.getObjectListbyName(self.parseur.objects, str(lightlist)))
        print resultLightest
        return str(resultLightest)

    def littleattr(self, attr):
        print "MyModule process the smallest object in the list with this attr", "<", attr, ">"
        littlelist = self.processObject.hasAttribute(self.parseur.objects, attr)
        resultLittle = ""
        resultLittle = self.processObject.little(self.utils.getObjectListbyName(self.parseur.objects, str(littlelist)))
        return str(resultLittle)

    def biggestattr(self, attr):
        print "MyModule process the biggest object in the list with this attr", "<", attr, ">"
        biglist = self.processObject.hasAttribute(self.parseur.objects, attr)
        resultBiggest = ""
        resultBiggest = self.processObject.biggest(self.utils.getObjectListbyName(self.parseur.objects, str(biglist)))
        return str(resultBiggest)