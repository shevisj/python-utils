from SunFounder_Ultrasonic_Avoidance import Ultrasonic_Avoidance
from picar import front_wheels
from picar import back_wheels
import time
import picar
import random

force_turning = 0    # 0 = random direction, 1 = force left, 2 = force right, 3 = orderdly

picar.setup()

ua = Ultrasonic_Avoidance.Ultrasonic_Avoidance(20)
fw = front_wheels.Front_Wheels(db='config')
bw = back_wheels.Back_Wheels(db='config')
fw.turning_max = 45

forward_speed = 70
backward_speed = 70

back_distance = 10
turn_distance = 20

timeout = 10
last_angle = 90
last_dir = 0

def rand_dir():
	global last_angle, last_dir
	if force_turning == 0:
		_dir = random.randint(0, 1)
	elif force_turning == 3:
		_dir = not last_dir
		last_dir = _dir
		print 'last dir  %s' % last_dir
	else:
		_dir = force_turning - 1
	angle = (90 - fw.turning_max) + (_dir * 2* fw.turning_max)
	last_angle = angle
	return angle

def stop():
	bw.stop()
	fw.turn_straight()

def opposite_angle():
	global last_angle
	if last_angle < 90:
		angle = last_angle + 2* fw.turning_max
	else:
		angle = last_angle - 2* fw.turning_max
	last_angle = angle
	return angle

def runTest():
    fw.turn_straight()
    bw.backward()
    bw.speed = forward_speed
    sleep(1)
    bw.stop()

if __name__ == '__main__':
	try:
		runTest()
	except KeyboardInterrupt:
		stop()
