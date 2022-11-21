# 라이트 기능
import datetime
import engine
import Gear
import Braeak
now = datetime.datetime.now()

normalLights = 0
autos = 0
reverseLights = 0
breakLights = 0
highBeams = 0
tailLights = 0
fogLights = 0


def normalLight():
    global normalLights
    if normalLights == 0:
        normalLights = 1
        return normalLights
    elif normalLights == 1:
        normalLights = 0
        return normalLights

def highBeam():
    global highBeams
    if highBeams == 0:
        highBeams = 1
        return highBeams
    elif highBeams == 1:
        highBeams = 0
        return highBeams

def  fogLight():
    global fogLights
    if fogLights == 0:
        fogLights = 1
        return fogLights
    elif fogLights == 1:
        fogLights = 0
        return fogLights

def auto():
    global autos
    global normalLights
    if autos == 0:
        autos = 1
        if 6 <= now.hour <= 19:
            normalLights = 0
            return autos
        else:
            normalLights = 1
            return autos
    if autos == 1:
        autos = 0
        return autos

def reverseLight():
    global reverseLights
    if Gear.a == 1:
        reverseLights = 1
        return reverseLights
    else:
        reverseLights = 0
        return reverseLights

def breakLight():
    pass
    global breakLights
    if Braeak.a == 0:
        breakLights = 1
        return breakLights
    else:
        breakLights = 0
        return breakLights



def taillight():
    global tailLights
    if engine.engines == 1:
        tailLights = 1
        return tailLights
    else:
        tailLights = 0
        return tailLights





