import RPi.GPIO as GPIO
import time
 
CONTROL_PIN = 21
PWM_FREQ = 50
STEP=90  
GPIO.setmode(GPIO.BCM)
GPIO.setup(CONTROL_PIN, GPIO.OUT)
       
def angle_to_duty_cycle(angle=0):
    duty_cycle = (0.04 * PWM_FREQ) + (0.195 * PWM_FREQ * angle / 180)
    return duty_cycle

def change_pwm_go(a):
    angle = a
    dc = angle_to_duty_cycle(90)
    GPIO.setup(CONTROL_PIN, GPIO.OUT)
    pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ)
    pwm.start(dc)
    if angle < 0:
        angle = 0 - angle
        for loc_angle in range(0, int(angle+1), 1):
            dc = angle_to_duty_cycle(90 + loc_angle)
            print("DC = {}".format(dc))
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)
    else:
        for loc_angle in range(0, int(angle+1), 1):
            dc = angle_to_duty_cycle(90 - loc_angle)
            print("Angle = {}, DC = {}".format(loc_angle, dc))
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)

    pwm.stop()

def change_pwm_back(a):
    angle = a
    dc = angle_to_duty_cycle(90)
    GPIO.setup(CONTROL_PIN, GPIO.OUT)
    pwm = GPIO.PWM(CONTROL_PIN, PWM_FREQ)
    pwm.start(dc)
    if angle < 0:
        for loc_angle in range(int(angle), 1, 1):
            dc = angle_to_duty_cycle(90 - loc_angle)
            print("DC = {}".format(dc))
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)
    else:
        angle = 0 - angle
        for loc_angle in range(int(angle), 1, 1):
            dc = angle_to_duty_cycle(90 + loc_angle)
            print("Angle = {}, DC = {}".format(loc_angle, dc))
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)
    pwm.stop()
