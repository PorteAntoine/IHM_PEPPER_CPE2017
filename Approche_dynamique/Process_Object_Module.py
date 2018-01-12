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
    def heaviest(self, listOfNames):
        """
        """
        print "MyModule process an object"
        resultHeaviest=""
        print listOfNames
        resultHeaviest = self.processObject.heaviest(self.utils.getObjectListbyName(self.parseur.objects, listOfNames))
        return str(resultHeaviest)

