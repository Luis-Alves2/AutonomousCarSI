# The Nature of Code
# Daniel Shiffman
# http://natureofcode.com
#
# Modified by Filipe Calegario

# Draws a "vehicle" on the screen

from Vehicle import Vehicle
from Food import Food
from Comidas import Comidinhas

def setup():
    global vehicle
    global foodie
    global comidinhas
    
    comidinhas = Comidinhas(0)
    
    size(640, 360)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2, velocity)
    
    x = random (640)
    y = random (360)
    
    foodie = Food(x,y,velocity)

def draw():
    background(255)
    mouse = PVector(mouseX, mouseY)
    
    # Draw an ellipse at the mouse position
    fill(127)
    stroke(200)
    strokeWeight(2)
    #ellipse(mouse.x, mouse.y, 48, 48)

    # Call the appropriate steering behaviors for our agents
    foodiex = foodie.position
    vehicle.arrive(foodiex)
    vehicle.update()
    vehicle.display()
    
    if(dist(vehicle.position,foodiex) < (foodie.r + vehicle.r - 2)):
        comidinhas.update()
        comidinhas.getComidinhas()
        x = random (640)
        y = random (360)
        foodie.respawn(x,y)
    
    foodie.display()
    
def dist(posa,posb):
    return sqrt((posa.x - posb.x) * (posa.x - posb.x) + (posa.y - posb.y) * (posa.y - posb.y))
