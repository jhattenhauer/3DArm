from ursina import *

app = Ursina()

class base(Entity):
    def __init__(self, add_to_scene_entities=True, enabled=True, **kwargs):
        super().__init__(add_to_scene_entities, enabled, **kwargs)
        self.model= "cube"
        self.texture = "white_cube"
        self.scale = (0.45,1,0.45)
        
    def update(self):
        self.rotation_y += held_keys['c'] * time.dt * 100
        self.rotation_y -= held_keys['z'] * time.dt * 100

class arm1(Entity):
    def __init__(self, add_to_scene_entities=True, enabled=True, **kwargs):
        super().__init__(add_to_scene_entities, enabled, **kwargs)
        self.model= "cube"
        self.texture = "white_cube"
        self.scale = (0.35,1,0.35)
        
    def update(self):
        self.rotation_y += held_keys['d'] * time.dt * 100 #stacking commands with children allow for rotation of whole tower
        self.rotation_y -= held_keys['a'] * time.dt * 100
        self.rotation_y += held_keys['c'] * time.dt * 100
        self.rotation_y -= held_keys['z'] * time.dt * 100
    def input(self, key):
        if key == "w":
            self.rotate((self.rotation_x + 1,0,0), base_block)
        if key == "s":
            self.rotate((self.rotation_x - 10,0,0), base_block)


base_block = base()   
arm = arm1()

arm.origin = (0,-1,0)     
app.run()