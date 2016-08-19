# -*- encoding: UTF-8 -*- 

'''Finding Target: Finding the Target on labirinth'''

import math
import almath as m # python's wrapping of almath
import sys
import vrep
from naoqi import ALProxy
from manage_joints import get_first_handles,JointControl
from set_start_position import setStartPosition, getStartPosition
from search_algorithm import retrieve_path
from multiprocessing import Process
import threading
from time import sleep
import time
import random
import motion

labirinth = [[1,0,0,0,0,0,0], [0,0,1,1,1,0,0],[0,0,0,0,1,1,1]]


# labirinth data has the info [center position] = [x,y] on WORLD_FRAME 
labirinthData = [[[-1.7500, 0.7000],[-1.2750,0.7000],[-0.8000,0.7000],[-0.3500,0.7000],[0.1250,0.7000],[0.6250,0.7000],[1.1750,0.7000]],
                [[-1.7500,0.2750],[-1.2750,0.2750],[-0.8000,0.2750],[-0.3500,0.2750],[0.1250,0.2750],[0.6250,0.2750],[1.1750,0.2750]],
                [[-1.7500,-0.2250],[-1.2750,-0.2250],[-0.8000,-0.2250],[-0.3500,-0.2250],[0.1250,-0.2250],[0.6250,-0.2250],[1.1750,-0.2250]]]


def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints

    proxy.setSmartStiffnessEnabled(False)

    proxy.rest()
    proxy.wakeUp()

    proxy.setFallManagerEnabled(True)
    #print proxy.getSummary()

def GetRobotPositionOnLabirinth(RobotRawPosition):
    RobotDPosition = [-1,-1]
    print RobotRawPosition
    found = 0
    for column in range (7):
        y = labirinthData[0][column][0]
        #print 'raw[y] = %s | verified = [%s]' % (RobotRawPosition[0], y)
        if (math.fabs(RobotRawPosition[0] - y) < 0.25):
            #print 'match column %s' % (column)
            for line in range(3):
                x = labirinthData[line][column][1]
                #print 'raw[x] = %s | verified = [%s]' % (RobotRawPosition[1], x)
                if (math.fabs(RobotRawPosition[1] - x) < 0.25):
                    #print 'match line %s' % (line)
                    RobotDPosition  = [column, line]
                    found = 1
#                   break
        if found == 1:
            break
            
    print 'position on labirinth %s' % RobotDPosition
    return RobotDPosition
        
 
def ReachDiscreteDesiredPosition(presentPosition, desiredPosition):
    if ( presentPosition[0] == desiredPosition[0] and presentPosition[1] == desiredPosition[1]):
        return True
    else:
        return False

class Robot:
    def __init__(self, motionProxy, postureProxy, vrepclientID):
        self.mp = motionProxy
        self.pp = postureProxy
        self.RawPosition = None
        self.RawOrientation = None
        self.DiscretePosition = None
        self.vrepclientID = vrepclientID
        self.firstPosVerification = True
        self.firstOrVerification = True
        self.lastOrientation = 'R'
        

    def WalkConfigs(self):
        #####################
        ## FOOT CONTACT PROTECTION
        #####################
        #~ motionProxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION",False]])
        self.mp.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])

        #####################
        ## Enable arms control by move algorithm
        #####################
        self.mp.setMoveArmsEnabled(True, True)
        #time.sleep(5)
    

    def GetRawPosition(self):
        #####################
        ## get robot position in the WORLD_FRAME and discretizes it on a labirinth Position
        #####################
        retries = 0
        while True:
            returnCode, NaoHandle = vrep.simxGetObjectHandle(self.vrepclientID,'NAO',vrep.simx_opmode_oneshot_wait)
            retries +=1
            if (returnCode == 0 and NaoHandle is not None) or retries > 3:
                break
            retries = 0
        if returnCode == 0:
            while True:
                if self.firstPosVerification:
                    returnCode, self.RawPosition =vrep.simxGetObjectPosition(clientID, NaoHandle ,-1 , vrep.simx_opmode_streaming )
                    self.firstPosVerification = False
                else:
                    returnCode, self.RawPosition =vrep.simxGetObjectPosition(clientID, NaoHandle ,-1 , vrep.simx_opmode_buffer )
                if (returnCode == 0 and self.RawPosition is not None) or retries > 3:
                    break
            
        print 'return code [%s] and position %s' %(returnCode, self.RawPosition)
        return self.RawPosition

    def GetRawOrientation(self):
        #####################
        ## get robot position in the WORLD_FRAME and discretizes it on a labirinth Position
        #####################
        retries = 0
        while True:
            returnCode, NaoHandle = vrep.simxGetObjectHandle(self.vrepclientID,'NAO',vrep.simx_opmode_oneshot_wait)
            retries +=1
            if (returnCode == 0 and NaoHandle is not None) or retries > 3:
                break
            retries = 0
        if returnCode == 0:
            while True:
                if self.firstOrVerification:
                    returnCode, self.RawOrientation =vrep.simxGetObjectOrientation(clientID, NaoHandle ,-1 , vrep.simx_opmode_streaming )
                    self.firstOrVerification = False
                else:
                    returnCode, self.RawOrientation =vrep.simxGetObjectOrientation(clientID, NaoHandle ,-1 , vrep.simx_opmode_buffer )
                if (returnCode == 0 and self.RawOrientation is not None) or retries > 3:
                    break
            
        print 'return code [%s] and position %s' %(returnCode, self.RawOrientation)
        return self.RawOrientation

    def GetLabirinthPosition(self):
        #####################
        ## get robot position in the WORLD_FRAME and discretizes it on a labirinth Position
        #####################
        self.DiscretePosition = GetRobotPositionOnLabirinth(self.GetRawPosition())
        return self.DiscretePosition

    
    def SetThetaToMove(self, direction):
        if direction == 'R':
            targetTheta = 0
        elif direction == 'U':
            targetTheta = math.pi/2
        elif direction == 'D':
            targetTheta = -math.pi/2
        elif direction == 'L':
            targetTheta = math.pi

        currentTheta = self.GetRawOrientation()
        print 'curr theta %s' % currentTheta
        deltaTheta = targetTheta - currentTheta[2]
        while True:
            self.mp.moveTo(0, 0, deltaTheta, self.mp.getMoveConfig("Default"))
            currentTheta = self.GetRawOrientation()
            deltaTheta = targetTheta - currentTheta[2]
            print 'delta %s' %deltaTheta
            if deltaTheta < 0.04:
                break
        
    def MoveTo(self, direction):
        self.SetThetaToMove(direction)
        print 'Depois do SetThetaToMove'
        positionNow = self.GetLabirinthPosition()
        print 'Depois do GetLabirinthPosition'

        if direction == 'R':
            nextPosition = [positionNow[0]+1, positionNow[1]]
        elif direction == 'L':
            nextPosition = [positionNow[0]-1, positionNow[1]]
        elif direction == 'U':
            nextPosition = [positionNow[0], positionNow[1]-1]
        elif direction == 'D':
            nextPosition = [positionNow[0], positionNow[1]+1]
        else:
            print 'direction not supported'

        tries = 20
        step_x = 0.4
        step_y = 0
        #while not ReachDiscreteDesiredPosition(self.GetLabirinthPosition(), nextPosition):
        print 'next position %s' % nextPosition
        while True:
            print 'next position %s' % nextPosition
            self.mp.moveTo(step_x, step_y, 0, self.mp.getMoveConfig("Default"))
            step_x, step_y = self.CorrectSteps(step_x, step_y, nextPosition)
            print 'step_x %s, step_y %s' % (step_x, step_y)
            if step_x < 0.04:
                break
            
        self.lastOrientation = direction
    
    def CorrectSteps(self,step_x, step_y,nextPosition):
        current = self.GetRawPosition()
        print 'next %s' % nextPosition
        targetPoint = labirinthData[nextPosition[1]][nextPosition[0]]
        #print 'Positions: current [%s] | target [%s]' % (current, targetPoint)        
        gradx = targetPoint[0] - current[0]
        grady = targetPoint[1] - current[1]
        
        step_x = gradx
        step_y = grady
        return step_x, step_y
        
    
    def FollowPath(self, path):
        if path:
            for direction in path:
                self.MoveTo(direction)
        self.comemorate()

    def FollowIterativePath(self, path):
        self.MoveTo(getNextMovement())
    
    def getNextMovement(self):
        pass

    def comemorate(self):
        self.pp.goToPosture('LyingBack', 0.5)
    
def raffleStartPosition(clientID):
    while True:
        column = random.randint(0,6)
        line =  random.randint(0,2)
        if(labirinth[line][column] == 0):
            break

    #TODO DELETE THIS WHEN FIND A WAY TO PUT THE ROBOT IN A (RANDON) DESIRED POSITION
    #colum = 0
    #line = 2
    positionZero = []
    positionZero.append(labirinthData[line][column][0])
    positionZero.append(labirinthData[line][column][1])
    positionZero.append(0.3509641885757446) 
    orientationZero = [0,0,0]

    #setStartPosition(clientID,positionZero,orientationZero)
    return [line, column], positionZero


class StoppableThread (threading.Thread):
    def __init__(self, clientID, motionProxy):
        super(StoppableThread, self).__init__()
        self.clientID = clientID
        self.motionProxy = motionProxy
        self.exitflag = threading.Event()
    def run(self):
        print "================ Handles Initialization ================"
        Head_Yaw=[];        Head_Pitch=[];
        L_Hip_Yaw_Pitch=[]; L_Hip_Roll=[];      L_Hip_Pitch=[]; L_Knee_Pitch=[];    L_Ankle_Pitch=[];    L_Ankle_Roll=[];
        R_Hip_Yaw_Pitch=[]; R_Hip_Roll=[];      R_Hip_Pitch=[]; R_Knee_Pitch=[];    R_Ankle_Pitch=[];    R_Ankle_Roll=[];
        L_Shoulder_Pitch=[];L_Shoulder_Roll=[]; L_Elbow_Yaw=[]; L_Elbow_Roll=[];    L_Wrist_Yaw=[]
        R_Shoulder_Pitch=[];R_Shoulder_Roll=[]; R_Elbow_Yaw=[]; R_Elbow_Roll=[];    R_Wrist_Yaw=[]
        R_H=[];             L_H=[];             R_Hand=[];      L_Hand=[];
        Body = [Head_Yaw,Head_Pitch,L_Hip_Yaw_Pitch,L_Hip_Roll,L_Hip_Pitch,L_Knee_Pitch,L_Ankle_Pitch,L_Ankle_Roll,R_Hip_Yaw_Pitch,
                R_Hip_Roll,R_Hip_Pitch,R_Knee_Pitch,R_Ankle_Pitch,R_Ankle_Roll,L_Shoulder_Pitch,L_Shoulder_Roll,L_Elbow_Yaw,L_Elbow_Roll,
                L_Wrist_Yaw,R_Shoulder_Pitch,R_Shoulder_Roll,R_Elbow_Yaw,R_Elbow_Roll,R_Wrist_Yaw,L_H,L_Hand,R_H,R_Hand]
    
        get_first_handles(clientID,Body)

        while(vrep.simxGetConnectionId(clientID)!=-1):
            if self.exitflag.isSet():
                print 'End of simulation'
                break

            JointControl(self.clientID,self.motionProxy,0,Body)
            #sleep(0.005)
    def SetExitFlag(self):
        self.exitflag.set()
        
def startingComunication(clientID, motionProxy):
    try:
        thread1 = StoppableThread(clientID,motionProxy)
        thread1.start()

    except:
       print "Error: unable to start process"
       sys.exit(1)
    return thread1


def main(robotIP,clientID):
    try:
        motionProxy = ALProxy("ALMotion", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e
        exit(1)
    
    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e
        exit(1)

    #startPosition, PositionZero = raffleStartPosition(clientID)
    #setStartPosition(clientID, PositionZero)
    startPosition = [2,0]

    # Set NAO in stiffness On
    StiffnessOn(motionProxy)

    nao = Robot(motionProxy, postureProxy,clientID)

    print '========== Setting Start Position =========='
    # Making some configs to start in the correct point and to walk smoothly

    #starting comunication between vrep and nao-qi
    thread1 = startingComunication(clientID, motionProxy)
    time.sleep(5)
    
    nao.WalkConfigs()

    print '========== NAO is listening =========='


    path = retrieve_path(startPosition)
    print "================ follow the path ================"
    nao.FollowPath(path)


    print "================ Closing Comunication ================"
    thread1.SetExitFlag()
    thread1.join()



if __name__ == "__main__":
    robotIp = "127.0.0.1"

    if len(sys.argv) <= 1:
        print "Usage python motion_moveTo.py robotIP (optional default: 127.0.0.1)"
    else:
        robotIp = sys.argv[1]

    print '================ Program Sarted ================'
    
    vrep.simxFinish(-1)
    clientID=vrep.simxStart('127.0.0.1',19999,True,True,5000,5)
    if clientID!=-1:
        print 'Connected to remote API server'
    
    else:
        print 'Connection non successful'
        sys.exit('Could not connect')
    #setStartPosition(clientID)
    main(robotIp, clientID)
    print "================ Exiting Session ================"
    
    vrep.simxFinish(-1)
