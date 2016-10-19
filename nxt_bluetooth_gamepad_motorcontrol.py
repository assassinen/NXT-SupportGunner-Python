import pygame

from nxt.locator import find_one_brick
from nxt.motor import *
from time import sleep, clock

pygame.init()

done = False

joystick_count=pygame.joystick.get_count()
if joystick_count == 0:
    print ("Error, I didn't find any joysticks.")
else:
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()
 
brick = find_one_brick()
mc = brick.mc

rotate_engine  = Motor(brick, PORT_A)
fire_engine = Motor(brick, PORT_C)
 
#vehicle = SynchronizedMotors(left_engine, right_engine, 0)
 
angle = 0
angle_prev = 0

mc.start()
sleep(4)

while done == False:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    if joystick_count != 0:
     
        horiz_axis_pos = my_joystick.get_axis(0)
        vert_axis_pos = my_joystick.get_axis(2)
        button = my_joystick.get_button(0)
        button_exit = my_joystick.get_button(1)

    rotate = int(-1 * horiz_axis_pos * 100)

    updown = int(-1 * vert_axis_pos * 90)

    #print rotate

    if mc.is_ready(PORT_B):
        mc.move_to(PORT_B, 50, updown, 1, 0, 0)
      
    rotate_engine.run(rotate)

    if button > 0:
        fire_engine.run(100)

    if button == 0:
        fire_engine.run(0)
     
    if button_exit > 0:
        done=True
    
mc.stop()
pygame.quit()

