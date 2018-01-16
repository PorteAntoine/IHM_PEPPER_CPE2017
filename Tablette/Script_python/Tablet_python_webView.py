from naoqi import ALProxy
from naoqi import qi
import time

robot_ip = "169.254.141.186"
package_id = "tablette_test"

robot_ip = "localhost"
robot_ip = "169.254.63.2"
robot_port = 9559
#robot_port = 55234


url_base = "" #pas à remplir
    

def test_website(robot_ip, robot_port):
    tabletservice = ALProxy("ALTabletService", robot_ip, robot_port)
    val1 = tabletservice.showWebview("http://198.18.0.1/apps/tablette_test/index3.html")

    # Getting the service ALDialog
    ALDialog = ALProxy('ALDialog',robot_ip,robot_port)

    # stop topic active (pose probleme sinon en programmation)
    ALDialog.stopTopics( ALDialog.getAllLoadedTopics())
    
    #Query
    topic_content = ('topic: ~example_topic_content()\n'
                       'language: enu\n'
                       'concept:(predicat) [color location]\n'
                       'concept:(object) [sky smurf]\n'
                        'u: (hello) Hello human  '
                        '^call(ALMemory.insertData("keyword", "Hello")) '
                        '^call(ALTabletService.loadUrl("http://198.18.0.1/apps/tablette_test/index2.html")) '
                        '^call(ALTabletService.showWebview()) \n'
                        'u: (apple) Okay'
                        '^call(ALMemory.insertData("keyword", "apple")) '
                        '^call(ALTabletService.loadUrl("http://198.18.0.1/apps/tablette_test/index2.html")) '
                        '^call(ALTabletService.showWebview()) \n'
                        'u: (pineapple) Okay '
                        '^call(ALMemory.insertData("keyword", "pineapple")) '
                        '^call(ALTabletService.loadUrl("http://198.18.0.1/apps/tablette_test/index2.html")) '
                        '^call(ALTabletService.showWebview()) \n'
                        'u: (banana) Okay  '
                        '^call(ALMemory.insertData("keyword", "banana")) '
                        '^call(ALTabletService.loadUrl("http://198.18.0.1/apps/tablette_test/index2.html")) '
                        '^call(ALTabletService.showWebview()) \n')
    
    # Loading the topics directly as text strings
    topic = ALDialog.loadTopicContent(topic_content)

    # Activating the loaded topics
    ALDialog.subscribe('myModule')
    ALDialog.activateTopic(topic)

    raw_input(u"Press 'Enter' to continue")

    ALDialog.deactivateTopic(topic)
    ALDialog.unloadTopic(topic)
    ALDialog.unsubscribe('myModule')
    

def main(robot_ip, robot_port):
        tabletservice = ALProxy("ALTabletService", robot_ip, robot_port)

        # store Url de base
        ip = tabletservice.robotIp()
        url_base = 'http://' + ip + '/apps/' + package_id + '/'
        
        # load image
        url_image = url_base + 'img/'
        val = tabletservice.preLoadImage(url_image + 'image1.png')
        val = tabletservice.preLoadImage(url_image + 'banana.jpg')
        val = tabletservice.preLoadImage(url_image + 'ananas.jpg')
        val = tabletservice.preLoadImage(url_image + 'apple.jpg')
        val = tabletservice.showImage(url_image + 'image1.png')
        time.sleep(0.5)
        test_website(robot_ip, robot_port)
       
        
     

if __name__ == '__main__':
    main(robot_ip, robot_port)
