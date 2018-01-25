from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule
import sys
import time

memory = None
SoundLocator = None
motion_service = None

class SoundLocatorModule(ALModule):
    def __init__(self, name, IP, PORT):
        myBroker = ALBroker("myBroker","0.0.0.0",0,IP,PORT)
        ALModule.__init__(self, name)
            
        #self.tts = ALProxy("ALTextToSpeech", IP, PORT)
        self.soundFound = False 
        self.soundAngle = 0.0 # continuesly gets updated during runtime

        global motion_service
        motion_service  =  ALProxy("ALMotion", IP, PORT)

        # Subscribe to the event:
        global memory
        memory = ALProxy("ALMemory", IP, PORT)
        memory.subscribeToEvent("ALSoundLocalization/SoundLocated", "SoundLocator", "onSoundLocated")


    def onSoundLocated(self, *_args):
        
        # Unsubscribe to the event 
        memory.unsubscribeToEvent("ALSoundLocalization/SoundLocated", "SoundLocator")
    
        #self.tts.say("heard you")
        soundLocation = memory.getData("ALSoundLocalization/SoundLocated")
        angles = soundLocation[1]        
        self.soundFound = True
        print("angle: " + str(angles[0]))

        #Move Robot to Sound
        
        motion_service.moveTo(0, 0, 0.3)
        self.soundFound = False

        # Subscribe again to the event
        memory.subscribeToEvent("ALSoundLocalization/SoundLocated", "SoundLocator", "onSoundLocated")
        



def main():
    #IP = "localhost"
    #PORT =51394
    IP = "pepper.local"
    PORT =9559
    myBroker = ALBroker("myBroker",
        "0.0.0.0",   # listen to anyone
        0,           # find a free port and use it
        IP,         # parent broker IP
        PORT)

    global SoundLocator
    SoundLocator = SoundLocatorModule("SoundLocator",IP,PORT)
    print motion_service
    momo = motion_service.moveTo(0, 0, 50)
    print momo
    
    try:
        while True:
            # print("-")
            time.sleep(1)
            pass
    except KeyboardInterrupt:
        print
        print "Interrupted by user, shutting down"
        myBroker.shutdown()
        sys.exit(0)


if __name__ == '__main__':
    main()
