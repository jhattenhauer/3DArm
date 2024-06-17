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

def spin():
    base.rotation_y += 100 * (held_keys["1"] - held_keys["3"]) * time.dt

def spin1():
    hinge1.rotation_z += 100 * (held_keys["7"] - held_keys["4"]) * time.dt

def spin2():
    hinge2.rotation_z += 100 * (held_keys["8"] - held_keys["5"]) * time.dt

def spin3():
    hinge3.rotation_z += 100 * (held_keys["9"] - held_keys["6"]) * time.dt

def spin4():
    hinge4.rotation_z += 100 * (held_keys["w"] - held_keys["s"]) * time.dt
    hinge4.rotation_y += 100 * (held_keys["a"] - held_keys["d"]) * time.dt

#building arm    
base = hinge()
base.position = (0,-4,0)
base.update = spin

arm1 = arm()
arm1.parent = base
arm1.position = (0,1,0)

hinge1 = hinge()
hinge1.parent = arm1
hinge1.position = (0,1,0)
hinge1.update = spin1

arm2 = arm()
arm2.parent = hinge1
arm2.position = (0,1,0)

hinge2 = hinge()
hinge2.parent = arm2
hinge2.position = (0,1,0)
hinge2.update = spin2

arm3 = arm()
arm3.parent = hinge2
arm3.position = (0,1,0)

hinge3 = hinge()
hinge3.parent = arm3
hinge3.position = (0,1,0)
hinge3.update = spin3

arm4 = arm()
arm4.parent = hinge3
arm4.position = (0,1,0)

hinge4 = hinge()
hinge4.parent = arm4
hinge4.position = (0,1,0)
hinge4.update = spin4



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