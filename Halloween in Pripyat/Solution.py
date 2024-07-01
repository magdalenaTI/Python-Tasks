import math


class Candy:

    def __init__(self, mass, uranium):
        self.mass = mass
        self.uranium = uranium

    def get_uranium_quantity(self):
        return self.mass * self.uranium
    
    def get_mass(self):
        return self.mass
    
    def __gt__(self, other):
        if(self.get_mass() > other.get_mass()):
            return True
        return False


class Person:

    def __init__(self, position):
        self.position = position

    def get_position(self):
        return self.position
    
    def set_position(self, new_position):
        self.position = new_position


class Kid(Person):

    kid_uranium = 0

    def __init__(self, position, initiative):
         super().__init__(position)
         self.initiative = initiative

    def get_initiative(self):
        return self.initiative
    
    def add_candy(self, mass, uranium):
        self.candy = Candy(mass, uranium)
        self.kid_uranium += self.candy.get_uranium_quantity()

    def is_critical(self):
        if (self.kid_uranium > 20):
            return True
        return False
    
    def __lt__(self, other):
        if(self.get_initiative() < other.get_initiative()):
            return True
        return False
    
    def get_closest(self, hosts):
        min_dist = float('inf')
        distances = list()
        for host in hosts:
            curr_dist = math.dist(self.get_position(), host.get_position())
            if(curr_dist <  min_dist):
                min_dist = curr_dist
                closest_host = host

            if curr_dist in distances:
                    idx = distances.index(curr_dist)
                    closest_host = min(host, hosts[idx])
            else:
                distances.append(curr_dist)
        return closest_host


class Host(Person):

    candies = []

    def __init__(self, position, candies):
         super().__init__(position)
         for i in candies:
             host_candy = Candy(i[0], i[1])
             self.candies.append(host_candy)

    def remove_candy(self, func):
        if(len(self.candies) == 0):
            return None
        return func(self.candies)
    
    def __lt__(self, other):
        if(self.get_position()[0] < other.get_position()[0]):
            return True
        elif(self.get_position()[0] == other.get_position()[0] and self.get_position()[1] < other.get_position()[1]):
            return True
        else: 
            return False



class FluxCapacitor():

    victims = []
    hosts = list()

    def __init__(self, participants):
        for i in participants:
            if( isinstance(i, Host) ):
                self.hosts.append(i)

        for kid in participants:
            if( isinstance(kid, Kid) ):
               
                closest_host = kid.get_closest(self.hosts)
    
                kid.set_position(closest_host.get_position())
                candy = closest_host.remove_candy(max)
                kid.add_candy(candy.get_mass(), candy.get_uranium_quantity())
            
                if(kid.is_critical()):
                    self.victims.append(kid)

                if(self.get_victim() != None):
                    return
    
    def get_victim(self):
        if(len(self.victims) == 0):
            return None
        return self.victims
    
