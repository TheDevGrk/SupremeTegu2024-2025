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

rightFront = Motor(Ports.PORT3, True)
rightBack = Motor(Ports.PORT4)
leftFront = Motor(Ports.PORT1, True) 
leftBack = Motor(Ports.PORT2)

left = MotorGroup(leftFront, leftBack)
right = MotorGroup(rightFront, rightBack)

piston = Pneumatics(brain.three_wire_port.h)

driveTrain = DriveTrain(left, right, 70, 422, 319, MM, 0.5)


intakeMotor = Motor(Ports.PORT11)
conveyorMotor = Motor(Ports.PORT20)

def autonTesting():
    driveTrain.turn_for(RIGHT, 90, DEGREES)


def driveTask():
    while True:
        driveStraight = -1 * controller.axis4.position()
        driveTurn = controller.axis2.position()

        rightDrive = driveStraight - driveTurn
        leftDrive = driveStraight + driveTurn
        x = 1

        if rightDrive > 100 or rightDrive < -100:
            x = rightDrive / 100

            leftDrive /= x

        if leftDrive > 100 or leftDrive < -100:
            x = leftDrive / 100

            rightDrive /= x

        right.spin(FORWARD, rightDrive, PERCENT)
        left.spin(FORWARD, leftDrive, PERCENT)
        

def intakeForward():
    intakeMotor.spin(REVERSE, 100, PERCENT)

def intakeBackward():
    intakeMotor.spin(FORWARD, 100, PERCENT)
            
def intakeStop():
    intakeMotor.stop()

def conveyorStart():
    conveyorMotor.spin(FORWARD, 60, PERCENT)

def conveyorBackwards():
    conveyorMotor.spin(REVERSE, 60, PERCENT)

def conveyorStop():
    conveyorMotor.stop()

def pistonOpen():
    piston.open()

def pistonClose():
    piston.close()

def compDrive():
    controllerEnabled = True

def autonomous():
    brain.screen.print("Auton")

def stopMotors():
    rightFront.stop()
    rightBack.stop()
    leftFront.stop()
    leftBack.stop()



# drive = Thread(driveTask)

# competition = Competition(driveTask, autonTesting)


controller.buttonL2.pressed(intakeForward)
controller.buttonL2.released(intakeStop)

controller.buttonL1.pressed(intakeBackward)
controller.buttonL1.released(intakeStop)

controller.buttonR2.pressed(conveyorStart)
controller.buttonR2.released(conveyorStop)

controller.buttonR1.pressed(conveyorBackwards)
controller.buttonR1.released(conveyorStop)

controller.buttonA.pressed(autonTesting)
controller.buttonA.released(stopMotors)

controller.buttonUp.pressed(pistonOpen)
controller.buttonDown.pressed(pistonClose)