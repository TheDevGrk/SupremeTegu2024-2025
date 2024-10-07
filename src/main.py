# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       eligo                                                        #
# 	Created:      9/5/2024, 8:04:51 AM                                         #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

controller = Controller()
controllerEnabled = True

rightFront = Motor(Ports.PORT3)
rightBack = Motor(Ports.PORT4)
leftFront = Motor(Ports.PORT1) 
leftBack = Motor(Ports.PORT2)

intakeMotor = Motor(Ports.PORT10)
conveyorMotor = Motor(Ports.PORT20)

speed = 100

def driveTask():
    if controllerEnabled:
        while True:
            driveStraight = controller.axis2.position()
            driveTurn = controller.axis4.position()

            rightDrive = driveStraight - driveTurn
            leftDrive = driveStraight + driveTurn
            x = 1

            if rightDrive > 100 or rightDrive < -100:
                x = rightDrive / 100

                leftDrive /= x

            if leftDrive > 100 or leftDrive < -100:
                x = leftDrive / 100

                rightDrive /= x

            rightFront.spin(REVERSE, rightDrive, PERCENT)
            rightBack.spin(FORWARD, rightDrive, PERCENT)
            leftBack.spin(REVERSE, leftDrive, PERCENT)
            leftFront.spin(FORWARD, leftDrive, PERCENT)

def intakeForward():
    intakeMotor.spin(REVERSE, 100, PERCENT)

def intakeBackward():
    intakeMotor.spin(FORWARD, 100, PERCENT)
            
def intakeStop():
    intakeMotor.stop()

def conveyorStart():
    conveyorMotor.spin(FORWARD, 100, PERCENT)

def conveyorStop():
    conveyorMotor.stop()

def compDrive():
    controllerEnabled = True

def autonomous():
    controllerEnabled = False

drive = Thread(driveTask)

competition = Competition(driveTask, autonomous)


controller.buttonL2.pressed(intakeForward)
controller.buttonL2.released(intakeStop)

controller.buttonL1.pressed(intakeBackward)
controller.buttonL1.released(intakeStop)

controller.buttonR2.pressed(conveyorStart)
controller.buttonR2.released(conveyorStop)