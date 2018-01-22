import qi
from Process_localization import Process_localization
from Utils import Utils
class ProcessLocalizationModule:
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
        self.processLocalization=Process_localization()
        self.tts=session.service("ALTextToSpeech")



    def hasAttribute(self, attr):
        print "MyModule process the list of object having the attribute ", "<", attr, ">"
        result = ""
        result = self.processLocalization.hasAttribute(self.parseur.localizations, attr)
        print result
        if not result:
            result = "nothing"
        return self.tts.say(str(result))