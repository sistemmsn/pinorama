import sys
import functions
import servo
import console

#Servo pins in use
panServo = 7
tiltServo = 18

name = int(sys.argv[1]) 
pans = int(sys.argv[2]) 
tilts = int(sys.argv[3]) 

#Servo configs
minPan = 2.5
maxPan = 12.5
minTilt = 2.5
maxTilt = 7

panStep = round((maxPan-minPan)/pans,1)
tiltStep = round((maxTilt-minTilt)/pans, 1)

for p in functions.step_range(minPan, maxPan, panStep):
    servo.move(panServo,p)
    for t in step_range(minTilt, maxTilt, tiltStep):
        servo .move(tiltServo,t)
        console.run("./photo " + functions.name(name,p,t))


    




