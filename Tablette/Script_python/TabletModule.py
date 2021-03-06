from naoqi import ALProxy
from naoqi import qi
from naoqi import ALModule

class TabletModule (ALModule):
    def __init__(self, name, package_id):
        ALModule.__init__(self, name)
        self.tabletservice = ALProxy("ALTabletService")
        self.url_base = 'http://' + self.tabletservice.robotIp() + '/apps/' + package_id + '/'
        

         
    def appTablet_history(self, memtab, Hquestions, Hanswers,):
        string = ""
        i=1
        nbQshow = 5
        lenQ = len(Hquestions)

        # for Conversation_history
        for question, answer in zip(Hquestions, Hanswers):
            if i> lenQ-nbQshow:
                string += str(i) + "- " + question + "? " + answer + "<br>"
            i=i+1
        memtab.insertData("keyword_CH", string)

        # for show last input/answer
        string = Hquestions[lenQ-1] + "? " + Hanswers[lenQ-1]
        memtab.insertData("keyword_typed", string)

        #Load URL Web page tablet
        self.tabletservice.showWebview(self.url_base + "history.html")

    def appTablet_test(self, memtab,titre, string_1, string_2, string_3, pourcentage):
        memtab.insertData("titre", titre)
        memtab.insertData("txt1", string_1)
        memtab.insertData("txt2", string_2)
        memtab.insertData("txt3", string_3)
        memtab.insertData("pourcentage", pourcentage)
        
        #Load URL Web page tablet
        self.tabletservice.showWebview(self.url_base + "test.html")
