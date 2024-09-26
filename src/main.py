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

rightFront = Motor(Ports.PORT1)
rightBack = Motor(Ports.PORT2)
leftFront = Motor(Ports.PORT3)
leftBack = Motor(Ports.PORT4)

speed = 100

def driveTask():
    while True:
        driveStraight = controller.axis1.position()
        driveTurn = controller.axis3.position()

        if driveTurn == 0:
            rightFront.spin(FORWARD, driveStraight, PERCENT)
            rightBack.spin(REVERSE, driveStraight, PERCENT)
            leftBack.spin(FORWARD, driveStraight, PERCENT)
            leftFront.spin(REVERSE, driveStraight, PERCENT)
        else:
            rightFront.spin(FORWARD, driveTurn, PERCENT)
            rightBack.spin(REVERSE, driveTurn, PERCENT)
            leftFront.spin(REVERSE, driveTurn, PERCENT)
            leftBack.spin(FORWARD, driveTurn, PERCENT)
            


drive = Thread(driveTask)