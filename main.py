from ursina import *

app = Ursina()

class arm(Entity):
    def __init__(self, add_to_scene_entities=True, enabled=True, **kwargs):
        super().__init__(add_to_scene_entities, enabled, **kwargs)
        self.model=Cylinder(6, start=-.5)
        self.color = color.blue

class hinge(Entity):
    def __init__(self, add_to_scene_entities=True, enabled=True, **kwargs):
        super().__init__(add_to_scene_entities, enabled, **kwargs)
        self.model="Cube"
        self.texture = "white_cube"

#rotation functions
def spin(key):
    if key == "x":
        base.rotate((0,5,0))
    if key == "v":
        base.rotate((0,-5,0))


def spin1(key):
    if key == "e":
        hinge1.rotate((0,0,5))
    if key == "q":
        hinge1.rotate((0,0,-5))

def spin2(key):
    if key == "d":
        hinge2.rotate((0,0,5))
    if key == "a":
        hinge2.rotate((0,0,-5))

def spin3(key):
    if key == "c":
        hinge3.rotate((0,0,5))
    if key == "z":
        hinge3.rotate((0,0,-5))        

def spin4(key):
    if key == "6":
        hinge4.rotate((0,5,0))
    if key == "4":
        hinge4.rotate((0,-5,0))
    if key == "8":
        hinge4.rotate((5,0,0))
    if key == "2":
        hinge4.rotate((-5,0,0))

#building arm    
base = hinge()
base.position = (0,-4,0)
base.input = spin

arm1 = arm()
arm1.parent = base
arm1.position = (0,1,0)

hinge1 = hinge()
hinge1.parent = arm1
hinge1.position = (0,1,0)
hinge1.input = spin1

arm2 = arm()
arm2.parent = hinge1
arm2.position = (0,1,0)

hinge2 = hinge()
hinge2.parent = arm2
hinge2.position = (0,1,0)
hinge2.input = spin2

arm3 = arm()
arm3.parent = hinge2
arm3.position = (0,1,0)

hinge3 = hinge()
hinge3.parent = arm3
hinge3.position = (0,1,0)
hinge3.input = spin3

arm4 = arm()
arm4.parent = hinge3
arm4.position = (0,1,0)

hinge4 = hinge()
hinge4.parent = arm4
hinge4.position = (0,1,0)
hinge4.input = spin4

finger = hinge()
finger.parent = hinge4
finger.scale = (0.2,1,0.2)
finger.position = (0.5,0.5,0)

finger2 = hinge()
finger2.parent = hinge4
finger2.scale = (0.2,1,0.2)
finger2.position = (-0.5,0.5,0)

finger3 = hinge()
finger3.parent = hinge4
finger3.scale = (0.2,1,0.2)
finger3.position = (0,0.5,0.5)

finger4 = hinge()
finger4.parent = hinge4
finger4.scale = (0.2,1,0.2)
finger4.position = (0,0.5,-0.5)

app.run()