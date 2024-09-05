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

motorTest = Motor(Ports.PORT1)

def driveTask():
    motorTest.set_velocity(75, RPM)
    motorTest.spin(FORWARD)

drive = Thread(driveTask)