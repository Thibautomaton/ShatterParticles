

class Particle(object):
    def __init__(self, x, y, r_):
        self.location = PVector(x, y)
        self.velocity = PVector(random(-4, 4), random(0, 4))
        self.acceleration = PVector(0,0)
        
        self.home = PVector(x,y)
        self.returning=False
        
        self.angle = 0
        self.lifespan = 255
        
        self.r = r_
        
    def update(self):
        self.lifespan-=1
        
        self.velocity += self.acceleration
        self.location +=self.velocity
        
        self.acceleration.mult(0)
        
    def display(self):
        pushMatrix()
        translate(self.location.x, self.location.y)
        rotate(self.angle)
        fill(0, self.lifespan)
        stroke(0, self.lifespan)
        rectMode(CENTER)
        rect(0, 0, self.r, self.r)
        
        popMatrix()
        
    def isDead(self):
        if self.lifespan<0:
            return True
        else:
            return False
        
    def applyForce(self, force):
        self.acceleration += force
        
    def returnHome(self):
        direction = self.home-self.location
        direction.mult(0.05)
        self.velocity = direction
        self.location+=self.velocity
        if self.lifespan<255:
            self.lifespan+=1
            
        
        
        
        
        
        
    
