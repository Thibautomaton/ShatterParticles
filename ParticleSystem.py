from Particle import Particle

class ParticleSystem(object):
    def __init__(self, x, y, r):
        self.location = PVector(x, y)
        
        self.particles = []
        
        self.rows = 20
        self.cols = 20
        
        self.x = x
        self.y = y
        
        self.r = r
        
        self.breaking = False
        self.home = True
        
        self.gravity = PVector(0, 0.1)
        
        for i in range(self.rows*self.cols):
            self.addParticle(x + (i%self.cols)*self.r, y + int(i/self.rows)*self.r, self.r)
        
    def addParticle(self, x,y, r):
        self.particles.append(Particle(x, y, r))
        
    def removeParticles(self):
        self.particles=[]
        
    def update(self):
        if self.breaking:
            for p in self.particles:

                p.applyForce(self.gravity)
                p.update()
                
            self.particles = [p for p in self.particles if not p.isDead()]
            
        if not self.breaking:
            for p in self.particles:
                p.returnHome()
                if (p.location-p.home).mag()<1:
                    p.location = p.home.copy()
                    
                    p.velocity = PVector(0,0)
        
    def display(self):
        for p in self.particles:
            p.display()
            
    # def reset(self, x, y):
    #     self.particles= []
    #     self.breaking=False
    #     for i in range(self.rows*self.cols):
    #         self.addParticle(x + (i%self.cols)*self.r, y + int(i/self.rows)*self.r, self.r)
        
        
    def shatter(self):
        print("SHATTER")
        self.breaking=True
        for p in self.particles:
            p.applyForce(self.gravity)
            p.velocity = PVector(random(-4, 4), random(-2, 8))
            #p.acceleration = PVector(0,0)
            p.lifespan = 255
        
        
