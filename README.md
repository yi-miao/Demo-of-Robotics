# Demo-of-Robotics
Demo and play with PiCar-X from SunFounder

I use this product to demo some fundamental functions of robot.

Environment
1. DreamQuest mini pc (8G RAM, 256 DDR) runing Windows 11 Pro (upgraded from Windows 10 Pro) and VNC Viewer
2. Raspberry Pi 3 B+ running Raspbian bullseye with VNC Server enabled
3. PiCar-X from Sunfounder purchased from Amazon in October 2023
4. LongWei DC Power Supply Variable 30V 10A set at 8.0V to power PiCar (with currency ~0.4-0.8A)
5. Nulaxy Cell Phone Stand to hold PiCar
6. Logitech F310 wired gamepad

Basic Functions 
1. Drive wheels move, forward and backward
2. Steering wheels move, turn left and right
3. Camera control, turn left, right, up and down
4. Live video streaming
5. Text to speed, say "stop!" when detecting obstacle, say "turn left", "move forward" or "turn right" when tracking 
6. Object detection, using ultrasound sensor to measure distance from object in front
7. Line Tracking, using IR sensor to find the relative position to track line

Steps:
1. Assembly PiCar-X following instructions
2. Install Pi OS on Raspberry Pi SBC and configure it
3. Install VNC Viewer
4. Install PiCar-X packages: robot-hat and picar-x
5. Install python-opencv package (I do NOT use vilib package)
6. Create a python utility, control.py, for all the basic functions
7. Create a demo.py to demonstrate each of the basic functions
8. Connect Logitech gamepad to a Raspberry Pi USB port
9. Turn on Raspberry Pi
10. Connect to PiCar-C/Rapberry Pi from mini PC with VNC Viewer
11. Run:  python demo.py
12. Use gamepad left joystick to control the wheels, right joystick to control the camera
13. Move a sheet with black tape on it to simulate the track line to test the tracking function (visual/printed and audio/sound messages)
14. Move hand close to the front of PiCar-X and away to test the detecting function (visual/printed and audio/sound messages)

Playing with Robotics is fun!

Notes:
I did also play computer vision and AI functions such as image classification and object detection, but found my Raspberry Pi 3B+ is not powerful enough for them. Model training took almost forever! So I sperate Robot functions and AI functions, and play AI functions on another more powerful machine.

References:
[1] DreamQuest: https://www.amazon.ca/gp/product/B09DYLYXK2/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1 
[2] PiCar-X: https://www.amazon.ca/gp/product/B08PYMWNC4/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1
[3] PiCar-X Document: https://docs.sunfounder.com/projects/picar-x/en/latest/
[4] Nulaxy Cell Phone Stand: https://www.amazon.ca/gp/product/B08CJZ6LSK/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&th=1
[5] Logitech F310: https://www.amazon.ca/Logitech-940-000110-Gamepad-F310/dp/B003VAHYQY/ref=sr_1_1?keywords=logitech%2Bf310&qid=1699902411&sr=8-1&th=1
