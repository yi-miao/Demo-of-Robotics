import pygame
import cv2
import control

pygame.init()
control.init()

size = (400,300)
window = pygame.display.set_mode(size)

speed = 25
joystick = None
run = True
cap = cv2.VideoCapture(0)
while run and cap.isOpened():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if joystick:
        left_x, left_y = (joystick.get_axis(0), joystick.get_axis(1))
        right_x, right_y = (joystick.get_axis(3), joystick.get_axis(4))
        if abs(left_x) > 0.1:
            control.rudder(int(speed*left_x))
        if abs(left_y) > 0.1:
            control.throttle(-int(speed*left_y))
        if abs(right_x) > 0.1:
            control.aileron(int(speed*right_x))
        if abs(right_y) > 0.1:
            control.elevator(-int(speed*right_y))
            
        buttons = joystick.get_numbuttons()
        if joystick.get_button(5) == 1:
            control.stop()
    else:
        if pygame.joystick.get_count() > 0:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            
    if not control.detect():
        control.track()
                
    ret, frame = cap.read()
    if ret:
        vid = pygame.image.frombuffer(
                        frame.tobytes(), 
                        frame.shape[1::-1], 
                        "BGR")
    else:
        run = False
        
    window.blit(vid, (0, 0))
    pygame.display.flip()

control.stop()
cap.release()
cv2.destroyAllWindows()
pygame.quit()
quit()
