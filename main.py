from shapes import Particle
from pyglet.window import Window 
from pyglet.app import run
from pyglet.shapes import Circle, Rectangle

p1 = Particle((100, 100), 1)

screen = Window()

@screen.event
def on_draw():
   screen.clear()
   Circle(p1.position[0], p1.position[1], 1, color=(255, 255, 255)).draw()
   Rectangle(0, 0, 100, 100, (255, 0, 0)).draw(
   )

run()