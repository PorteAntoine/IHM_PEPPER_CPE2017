from naoqi import ALProxy
from naoqi import qi
import time



def test_question_showImage(robot_ip, robot_port):
    # Getting the service ALDialog
    ALDialog = ALProxy('ALDialog',robot_ip,robot_port)

    # stop topic active (pose probleme sinon en programmation)
    ALDialog.stopTopics( ALDialog.getAllLoadedTopics())
    
    #Query
    topic_content = ('topic: ~example_topic_content()\n'
                       'language: enu\n'
                       'concept:(predicat) [color location]\n'
                       'concept:(object) [sky smurf]\n'
                        'u: (hello) Hello human  \n'
                        'u: (apple) Okay  ^call(ALTabletService.showImage("http://198.18.0.1/apps/tablette_test/img/apple.jpg")) \n'
                        'u: (pineapple) Okay  ^call(ALTabletService.showImage("http://198.18.0.1/apps/tablette_test/img/ananas.jpg"))\n'
                        'u: (banana) Okay  ^call(ALTabletService.showImage("http://198.18.0.1/apps/tablette_test/img/banana.jpg")) \n')
    
    # Loading the topics directly as text strings
    topic = ALDialog.loadTopicContent(topic_content)

    # Activating the loaded topics
    ALDialog.subscribe('myModule')
    ALDialog.activateTopic(topic)

    raw_input(u"Press 'Enter' to continue")

    ALDialog.deactivateTopic(topic)
    ALDialog.unloadTopic(topic)
    ALDialog.unsubscribe('myModule')

    
def test_website(robot_ip, robot_port):
    tabletservice = ALProxy("ALTabletService", robot_ip, robot_port)
    val1 = tabletservice.showWebview("http://198.18.0.1/index.html")


    

def main(robot_ip, robot_port):
    tabletservice = ALProxy("ALTabletService", robot_ip, robot_port)
    
    # load image
    val = tabletservice.preLoadImage("http://198.18.0.1/apps/tablette_test/img/image1.png")
    val = tabletservice.preLoadImage("http://198.18.0.1/apps/tablette_test/img/banana.jpg")
    val = tabletservice.preLoadImage("http://198.18.0.1/apps/tablette_test/img/ananas.jpg")
    val = tabletservice.preLoadImage("http://198.18.0.1/apps/tablette_test/img/apple.jpg")
    val = tabletservice.showImage("http://198.18.0.1/apps/tablette_test/img/image1.png")
    time.sleep(2)
    test_question_showImage(robot_ip, robot_port)

if __name__ == '__main__':
    robot_ip = "169.254.127.84"
    robot_port = 9559
    main(robot_ip, robot_port)
