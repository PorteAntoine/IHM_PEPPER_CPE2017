from naoqi import ALProxy
import time


class Commande():
    def __init__(self):

        self.robot_ip = "169.254.85.73"
        self.robot_port = 9559
        self.top_path = "/home/nao/naoqi/topic_pack/"
        self.concept_path = self.top_path+"concept/concept_enu.top"
        self.drink_path = self.top_path+"drink/drink_enu.top"
        self.food_path = self.top_path+"food/food_enu.top"

    def main(self):
        self.concept(self.robot_ip, self.robot_port, self.concept_path)

        
    def drink(self, robot_ip, robot_port, topic_path):

        dialog = ALProxy('ALDialog',robot_ip,robot_port)

        topic_path=topic_path.decode('utf-8')
        topic = dialog.loadTopic(topic_path.encode('utf-8'))

        dialog.subscribe('myModule')
        dialog.activateTopic(topic)

        print "drink topic activated"

        raw_input(u"Press 'Enter' to continue")

        dialog.deactivateTopic(topic)
        dialog.unloadTopic(topic)
        dialog.unsubscribe('myModule')
        

    def food(self, robot_ip, robot_port, topic_path):

        dialog = ALProxy('ALDialog',robot_ip,robot_port)

        topic_path=topic_path.decode('utf-8')
        topic = dialog.loadTopic(topic_path.encode('utf-8'))

        dialog.subscribe('myModule')
        dialog.activateTopic(topic)

        print "food topic activated"

        raw_input(u"Press 'Enter' to continue")

        dialog.deactivateTopic(topic)
        dialog.unloadTopic(topic)
        dialog.unsubscribe('myModule')


    def concept(self, robot_ip, robot_port, topic_path):

        dialog = ALProxy('ALDialog',robot_ip, robot_port)
        memory = ALProxy('ALMemory',robot_ip, robot_port)

        
        topic_path=topic_path.decode('utf-8')
        topic = dialog.loadTopic(topic_path.encode('utf-8'))

        dialog.subscribe('myModule')
        dialog.activateTopic(topic)

        print "concept topic activated"

        memory.insertData("food",0)
        memory.insertData("drink",0)
        Food = memory.getData("food")
        Drink = memory.getData("drink")

        while Food == 0 and Drink ==0:
            Food = memory.getData("food")
            Drink = memory.getData("drink")
            time.sleep(1)

        print "food :",Food,"drink :", Drink

        if Food == "1":
            self.food(self.robot_ip, self.robot_port, self.food_path)

        if Drink == "1":
            self.drink(self.robot_ip, self.robot_port, self.drink_path)

        dialog.deactivateTopic(topic)
        dialog.unloadTopic(topic)
        dialog.unsubscribe('myModule')


if __name__ == '__main__':
    commande = Commande()
    commande.main()
