import random
import math

from gamelib import *

#The Pitch
#It begins...
#It’s so dark. How did you get here? What time is it? You sit still and wonder what’s going on. 
#Oh no. Now what? You hear some footsteps to the left. A hushed “braaaiiinnnnsss” echoing throughout the room. Great. 
#You sit still for a little longer and listen carefully. The place sounds infested. You can’t see anything, but you get up and start running. 
#Figuring out what to do next. You’re not about to die here. 

#The Response
#"Well that's just lazy writing... but go for it."

#The Directions
#Your job is to describe what you’re going to do to survive the zombie apocalypse by filling in the code for the PlayerCharacter class in the zombie.py file. The only goal is to remain alive until the end of the game, even if the zombies are still alive. 

class ZombieCharacter(ICharacter):
    def __init__(self, obj_id, health, x, y, map_view):
        ICharacter.__init__(self, obj_id, health, x, y, map_view)

    def selectBehavior(self):
        prob = random.random()

        # If health is less than 50%, then heal with a 10% probability
        if prob < 0.1 and self.getHealth() < self.getInitHealth() * 0.5:
            return HealEvent(self)

        # Pick a random direction to walk 1 unit (Manhattan distance)
        x_off = random.randint(-1, 1)
        y_off = random.randint(-1, 1)

        # Check the bounds
        map_view = self.getMapView()
        size_x, size_y = map_view.getMapSize()
        x, y = self.getPos()
        if x + x_off < 0 or x + x_off >= size_x:
            x_off = 0
        if y + y_off < 0 or y + y_off >= size_y:
            y_off = 0

        return MoveEvent(self, x + x_off, y + y_off)

class PlayerCharacter(ICharacter):
    def __init__(self, obj_id, health, x, y, map_view):
        ICharacter.__init__(self, obj_id, health, x, y, map_view)
        # You may add any instance attributes you find useful to save information between frames

    def selectBehavior(self):
        #Behavior will be based on health
        curr_health=self.getHealth()
        inithealth=self.getInitHealth()
        willscan=False
        if (curr_health % 30) == 0 or curr_health>inithealth * 0.9: #scan when health is a multiple of 30 or when basically at full health like at the beginning of the game
            willscan=True
            
        #heal
        # If health is less than 50%, then heal yourself
        if curr_health < inithealth * 0.5:
            return HealEvent(self)  

        #attack when a previous scan showed zombies
        results = self.getScanResults()
        lenresults=len(results)
        if lenresults!=0 and willscan==False:
            for i in (0,lenresults):    
                zombie = results[i].getID()
                return AttackEvent(self, zombie)
        #scan or move:
        # Pick a random direction to walk 1 unit (Manhattan distance)
        x_off = random.randint(-1, 1)
        y_off = random.randint(-1, 1)  
        # Check the bounds
        map_view = self.getMapView()
        size_x, size_y = map_view.getMapSize()
        x, y = self.getPos()
        if x + x_off < 0 or x + x_off >= size_x:
            x_off = 0
        if y + y_off < 0 or y + y_off >= size_y:
            y_off=0
        #scan every time health is a multiple of 30.
        if willscan==True :
            return ScanEvent(self)
        #if not scanning, move randomly
        else:
            return MoveEvent(self, x + x_off, y + y_off)  
        
        
        pass
    
