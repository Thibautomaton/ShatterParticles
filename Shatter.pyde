from ParticleSystem import ParticleSystem


def setup():
    global ps
    size(1459, 720)
    ps = ParticleSystem(150, 150, 5)
    
    
def draw():
    background(255)
    print("draw")
    
    ps.update()
    ps.display()
    
    
def mousePressed():
    if mouseButton==LEFT and not ps.breaking:
        ps.shatter()
    elif mouseButton==RIGHT and ps.breaking:
        ps.breaking = False
        #ps.removeParticles()
