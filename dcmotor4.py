import sys
import time
import RPi.GPIO as GPIO

coordinate_list =
{
    "Taipei": [25.0, 121.0],
    "London": [51.5, 0.0],
    "New York": [40.7, -74.0],
    "Buenos Aires": [-34.5, -58.3],
    "Sydney": [-33.0, 151.1],
    "Jakarta": [-6, 107.0],
    "Kyiv": [50.6, 30.5],
    "Lisbon": [38.3, -9.0],
    "Chungqing": [29.5, 106.5],
    "Cairo": [30.0, 31.2]
}

intro_list = {
    "Taipei": "",
    "London": "",
    "New York": "",
    "Buenos Aires": "",
    "Sydney": "",
    "Jakarta": "",
    "Kyiv": "",
    "Lisbon": "",
    "Chungqing": "",
    "Cairo": ""
}

def revolution(longtitude: int, latitude: int):
     
    GPIO.setmode(GPIO.BCM)
     
    STEPS_PER_REVOLUTION = (int)(2058 * (longtitude / 180.0))#32 * 64
    SEQUENCE = [[1, 0, 0, 0], 
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 1],
                [1, 0, 0, 1]]

    STEPPER_PINS = [6, 13, 19, 26]

    for pin in STEPPER_PINS:
      GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, GPIO.LOW)
     
    SEQUENCE_COUNT = len(SEQUENCE)
    PINS_COUNT = len(STEPPER_PINS)
     
    sequence_index = 0
    direction = 1
    steps = 0

    wait_time = 3/float(1000)
     
    try:
        print('按下 Ctrl-C 可停止程式')
        print('steps={}'.format(STEPS_PER_REVOLUTION))
        while True:
            
            for pin in range(0, PINS_COUNT):
                GPIO.output(STEPPER_PINS[pin], SEQUENCE[sequence_index][pin])
     
            steps += 1
            if steps >= STEPS_PER_REVOLUTION:
                break
    ##        direction = 1

            #print('index={}, direction={}, steps={}'.format(sequence_index, direction, steps))
            sequence_index+=1
    ##        if sequence_index == SEQUENCE_COUNT:
    ##            break
            sequence_index %= SEQUENCE_COUNT
     
            
            time.sleep(wait_time)
    except KeyboardInterrupt:
        print('關閉程式')
    finally:
        GPIO.cleanup()
        
    GPIO.setmode(GPIO.BCM)
     
    STEPS_PER_REVOLUTION = (int)(2058 * (latitude / 180.0))#32 * 64
    SEQUENCE = [[1, 0, 0, 0], 
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 1],
                [1, 0, 0, 1]]

    STEPPER_PINS = [17, 18, 27, 22]

    for pin in STEPPER_PINS:
      GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, GPIO.LOW)
     
    SEQUENCE_COUNT = len(SEQUENCE)
    PINS_COUNT = len(STEPPER_PINS)
     
    sequence_index = 0
    direction = 1
    steps = 0

    wait_time = 3/float(1000)
     
    try:
        print('按下 Ctrl-C 可停止程式')
        print('steps={}'.format(STEPS_PER_REVOLUTION))
        while True:
            
            for pin in range(0, PINS_COUNT):
                GPIO.output(STEPPER_PINS[pin], SEQUENCE[sequence_index][pin])
     
            steps += 1
            if steps >= STEPS_PER_REVOLUTION:
                break
    ##        direction = 1

            #print('index={}, direction={}, steps={}'.format(sequence_index, direction, steps))
            sequence_index+=1
    ##        if sequence_index == SEQUENCE_COUNT:
    ##            break
            sequence_index %= SEQUENCE_COUNT
     
            
            time.sleep(wait_time)
    except KeyboardInterrupt:
        print('關閉程式')
    finally:
        GPIO.cleanup()
        
def reverse(longtitude: int, latitude: int):
     
    GPIO.setmode(GPIO.BCM)
     
    STEPS_PER_REVOLUTION = (int)(2058 * (longtitude / 180.0))#32 * 64
    SEQUENCE = [[1, 0, 0, 0], 
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 1],
                [1, 0, 0, 1]]

    STEPPER_PINS = [6, 13, 19, 26]

    for pin in STEPPER_PINS:
      GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, GPIO.LOW)
     
    SEQUENCE_COUNT = len(SEQUENCE)
    PINS_COUNT = len(STEPPER_PINS)
     
    sequence_index = 0
    direction = 1
    steps = 0

    wait_time = 3/float(1000)
     
    try:
        print('按下 Ctrl-C 可停止程式')
        print('steps={}'.format(STEPS_PER_REVOLUTION))
        while True:
            
            for pin in range(0, PINS_COUNT):
                GPIO.output(STEPPER_PINS[pin], SEQUENCE[sequence_index][pin])
     
            steps += 1
            if steps >= STEPS_PER_REVOLUTION:
                break
    ##        direction = 1

            #print('index={}, direction={}, steps={}'.format(sequence_index, direction, steps))
            sequence_index-=1
    ##        if sequence_index == SEQUENCE_COUNT:
    ##            break
            sequence_index %= SEQUENCE_COUNT
     
            
            time.sleep(wait_time)
    except KeyboardInterrupt:
        print('關閉程式')
    finally:
        GPIO.cleanup()
        
    GPIO.setmode(GPIO.BCM)
     
    STEPS_PER_REVOLUTION = (int)(2058 * (latitude / 180.0))#32 * 64
    SEQUENCE = [[1, 0, 0, 0], 
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 1],
                [1, 0, 0, 1]]

    STEPPER_PINS = [17, 18, 27, 22]

    for pin in STEPPER_PINS:
      GPIO.setup(pin,GPIO.OUT)
      GPIO.output(pin, GPIO.LOW)
     
    SEQUENCE_COUNT = len(SEQUENCE)
    PINS_COUNT = len(STEPPER_PINS)
     
    sequence_index = 0
    direction = 1
    steps = 0

    wait_time = 3/float(1000)
     
    try:
        print('按下 Ctrl-C 可停止程式')
        print('steps={}'.format(STEPS_PER_REVOLUTION))
        while True:
            
            for pin in range(0, PINS_COUNT):
                GPIO.output(STEPPER_PINS[pin], SEQUENCE[sequence_index][pin])
     
            steps += 1
            if steps >= STEPS_PER_REVOLUTION:
                break
    ##        direction = 1

            #print('index={}, direction={}, steps={}'.format(sequence_index, direction, steps))
            sequence_index-=1
    ##        if sequence_index == SEQUENCE_COUNT:
    ##            break
            sequence_index %= SEQUENCE_COUNT
     
            
            time.sleep(wait_time)
    except KeyboardInterrupt:
        print('關閉程式')
    finally:
        GPIO.cleanup()
        
if __name__ == '__main__':
    
    while True:
        latitude = input("Latitude:")
        longtitude = input("Longtitude:")
        
        revolution(double(x), double(y))
        reverse(double(x), double(y))
