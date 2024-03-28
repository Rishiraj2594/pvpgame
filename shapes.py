import numpy as np

class Particle():
   def __init__(self, pos, mass):
      self.mass = mass
      self.position = np.array(pos)
      self.velocity = np.zeros(2)
      self.acceleration = np.zeros(2)
   
   def apply_acceleration(self, acc):
      self.acceleration = acc

   def update(self, dt):
      self.velocity = np.add(self.velocity, self.acceleration*dt) ## Velocity updated
      self.position = np.add(self.velocity*dt, 0.5*self.acceleration*dt*dt)   ## Position Updated
 
