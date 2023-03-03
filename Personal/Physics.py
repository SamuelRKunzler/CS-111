
class world:
    def __init__(self, y_size, x_size, cleaning=True):
        self.x_size = x_size+1
        self.y_size = y_size+1
        self.map = []
        self.objects = []
        self.objects_coords = []
        self.cleaning = cleaning
        for x in range(x_size):
            self.map.append([])
            for y in range(y_size):
                self.map[x].append(" ")
            
    def clean(self):
        self.map = []
        for x in range(self.x_size):
            self.map.append([])
            for y in range(self.y_size):
                self.map[x].append(" ")
    def add_object(self, name):

        if ([name] in self.objects) == False:
            self.objects.append(name)

    def update(self): 
        if self.cleaning:
            self.clean()

        for name in self.objects:
            self.map[int(-name.position[1])][int(name.position[0])] = name.char
        

    def print(self):
        y_string = '-'
        for y in range(len(main.map[0])):
            y_string += '-'
        print(y_string)

        for x in range(1,len(main.map)):
            string = '|'
            for y in range(1,len(main.map[x])):
                string += (main.map[x][y])
            print(string + "|")
        print(y_string)

class object:
    def __init__(self, name, mass, world, char='*', velocity=[0,0], acceleration = [0,0], force = [0,0], gravity= 9.8, position=[0,0]):
        self.position = position
        self.name = name
        self.mass = mass
        self.gravity = gravity
        self.velocity = velocity
        self.acceleration = acceleration
        self.force = [force[0], -self.gravity*self.mass + force[1]]
        self.world = world
        self.char = char
        self.world.add_object(self)
        world.update()
        

    def add_force(self, force):
        self.force[0] += force[0]
        self.force[1] += force[1]

    def update_acceleration(self):
        self.acceleration[0] = self.force[0]/self.mass
        self.acceleration[1] = self.force[1]/self.mass

    def update_velocity(self):
        self.velocity[0] = self.velocity[0] + self.acceleration[0]
        self.velocity[1] = self.velocity[1] + self.acceleration[1]
        
    def update_position(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        
    
        
    def pass_time(self):
        self.update_acceleration()
        self.update_velocity()
        self.update_position()
        

def simulate(world, time,):
    for s in range(time):
        for object in world.objects:
            object.pass_time()
            print(object.name, object.position)
        world.update()
        world.print()
    
###############################################################################
#                                                                             #
#                       The Interactive stuff!!!!                             #
#                                                                             #
#                                                                             #
#                                                                             #      
###############################################################################


main = world(160,30, cleaning=False)
dot = object("dot", 1, main, velocity=[4,3], force=[0, .8], gravity=1, char="0", position=[1,1])
square = object("square", 1, main, velocity=[1, 0], force=[1,0], gravity=.5, char="1", position=[0,1])
simulate(main, 15 )



