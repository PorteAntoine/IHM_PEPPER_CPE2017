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
        print "MyModule init"
        self.session = session
        self.parseur = parseur
        self.utils = Utils()
        self.processObject=Process_object()


    #return a string containing the heaviest object

    def boolAttribute(self, listOfNames, attr):
        print "MyModule process an object"
        result = ""
        print listOfNames
        result = self.processObject.boolAttribute(self.utils.getObjectListbyName(self.parseur.objects, listOfNames),attr)
        return str(result)

    def sameCategory(self, name1, name2):
        print "MyModule process an object"
        listofNames = []
        listofNames.append(name1)
        listofNames.append(name2)
        result = ""
        result = self.processObject.sameCategory(self.utils.getObjectListbyListName(self.parseur.objects,listofNames))
        return str(result)

    def heaviest(self, listOfNames):
        print "MyModule process an object"
        resultHeaviest=""
        print listOfNames
        resultHeaviest = self.processObject.heaviest(self.utils.getObjectListbyName(self.parseur.objects, listOfNames))
        return str(resultHeaviest)

    def lightest(self, listOfNames):
        print "MyModule process an object"
        resultlightest=""
        print listOfNames
        resultlightest = self.processObject.lightest(self.utils.getObjectListbyName(self.parseur.objects, listOfNames))
        return str(resultlightest)

    def biggest(self, listOfNames):
        print "MyModule process an object"
        resultbiggest=""
        print listOfNames
        resultbiggest = self.processObject.biggest(self.utils.getObjectListbyName(self.parseur.objects, listOfNames))
        return str(resultbiggest)

    def little(self, listOfNames):
        print "MyModule process an object"
        resultlittle=""
        print listOfNames
        resultlittle = self.processObject.little(self.utils.getObjectListbyName(self.parseur.objects, listOfNames))
        return str(resultlittle)

