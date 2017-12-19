from naoqi import ALProxy


def main(robot_ip, robot_port, topic_path):


    
    dialog = ALProxy('ALDialog',robot_ip,robot_port)

    topic_path=topic_path.decode('utf-8')
    topic = dialog.loadTopic(topic_path.encode('utf-8'))

    dialog.subscribe('myModule')
    dialog.activateTopic(topic)

    raw_input(u"Press 'Enter' to exit")

    dialog.deactivateTopic(topic)
    dialog.unloadTopic(topic)
    dialog.unsubscribe('myModule')


if __name__ == '__main__':

    robot_ip = "169.254.20.175"
    robot_port = 9559
    topic_path = "/home/nao/naoqi/topic_pack/concept/concept_enu.top"
    main(robot_ip, robot_port, topic_path)
