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
    
    hinge4.rotation_y += 100 * (held_keys["a"] - held_keys["d"]) * time.dt

#building arm    
base = hinge(position = (0,-4,0), update = spin,)
arm1 = arm(parent = base, position = (0,1,0), visible = True)
hinge1 = hinge(parent = arm1, position = (0,1,0), update = spin1, visible = True)
arm2 = arm(parent = hinge1, position = (0,1,0), visible = True)
hinge2 = hinge(parent = arm2, position = (0,1,0), update = spin2, visible = True)
arm3 = arm(parent = hinge2, position = (0,1,0), visible = True)
hinge3 = hinge(parent = arm3, position = (0,1,0), update = spin3, visible = True)
arm4 = arm(parent = hinge3, position = (0,1,0), visible = True)
hinge4 = hinge(parent = arm4, position = (0,1,0), update = spin4, visible = True)

finger = hinge(parent = hinge4, scale = (0.2,1,0.2),position = (0.5,0.5,0), visible = True)
finger2 = hinge(parent = hinge4, scale = (0.2,1,0.2), position = (-0.5,0.5,0), visible = True)
finger3 = hinge(parent = hinge4, scale = (0.2,1,0.2), position = (0,0.5,0.5), visible = True)
finger4 = hinge(parent = hinge4, scale = (0.2,1,0.2), position = (0,0.5,-0.5), visible = True)

app.run()