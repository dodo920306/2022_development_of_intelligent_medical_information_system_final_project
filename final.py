import sys
import time
import RPi.GPIO as GPIO
import taiwanese_tts as tts
import record
import mi2s_asr_client as cstt
import chinese_tts as ctts
import pwm
import practice as pc
import threading
import browser

alias_list = {
        "台北": "Taipei",
        "臺北": "Taipei",
        "她一倍": "Taipei",
        "還被": "Taipei",
        "倫敦": "London",
        "論斷": "London",
        "紐約": "New York",
        "五月": "New York",
        "布宜諾斯艾利斯": "Buenos Aires",
        "雅加達": "Jakarta",
        "基輔": "Kyiv",
        "給付": "Kviv",
        "里斯本": "Lisboa",
        "歷史": "Lisboa",
        "歷史本": "Lisboa",
        "開羅": "Cairo",
        "重慶": "Chungqing",
        "雪梨": "Sydney",
        "學歷": "Sydney",
        "海螺": "Cairo",
        "離資本": "Lisboa"
}

coordinate_list = {
    "Taipei": [25.0, 121.0],
    "London": [51.5, 0.0],
    "New York": [40.7, -74.0],
    "Buenos Aires": [-34.5, -58.3],
    "Sydney": [-33.0, 151.1],
    "Jakarta": [-6, 107.0],
    "Kyiv": [50.6, 30.5],
    "Lisboa": [38.3, -9.0],
    "Chungqing": [29.5, 106.5],
    "Cairo": [30.0, 31.2]
}

intro_list = {
    "Taipei": "臺北市，通稱臺北，是中華民國的首都及直轄市，亦為臺灣在政治、經濟、教育、文化等領域的發展中樞。景點有著名的摩天大樓台北101與收藏眾多中國藝術品的故宮博物院。",
    "London": "英國首都，也是英國最大都市。景點有大笨鐘以及倫敦之眼。",
    "New York": "紐約市，為世界最大的城市之一，被稱為「美國文化之都」。景點有自由女神像、帝國大廈、中央公園。",
    "Buenos Aires": "布宜諾斯艾利斯自治市，是阿根廷的首都和最大城市，景點有紀念鐘塔，阿根廷國家圖書館等",
    "Sydney": "雪梨，位於澳洲東南沿海地帶，是新南威爾斯州的首府，是澳洲人口最多也是人口最稠密的城市。著名景點有雪梨歌劇院。",
    "Jakarta": "雅加達，全稱雅加達特別首都地域，是印度尼西亞首都及最大城市，雅加達是印尼的經濟、文化和政治中心，著名景點有印尼國家紀念塔。",
    "Kyiv": "基輔為烏克蘭首都，是東歐重要的工業、科學、文化及教育中心，著名景點有黃金之門。",
    "Lisboa": "里斯本，亦稱為葡京，是葡萄牙共和國的首都和最大都市，著名景點有貝倫塔與里斯本大基督像。",
    "Chungqing": "重慶市別稱山城，是中華人民共和國直轄市，長江上游地區經濟中心，著名景點有三峽大壩。",
    "Cairo": "開羅是埃及的首都，埃及第一大城市以及全國經濟、交通和文化中心，著名景點有位於西邊的吉薩金字塔。"
}

url_list = {
    "Taipei": "https://www.skyscanner.com.tw/transport/flights/tnn/tpet/230401/230430/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27547236&inboundaltsenabled=false&infants=0&originentityid=33367910&outboundaltsenabled=true&preferdirects=false&ref=home&rtn=1",
    "London": "https://www.skyscanner.com.tw/transport/flights/tnn/lond/230401/230430/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27544008&inboundaltsenabled=false&infants=0&originentityid=33367910&outboundaltsenabled=true&preferdirects=false&ref=home&rtn=1",
    "New York": "https://www.skyscanner.com.tw/transport/flights/tnn/nyca/230401/230430/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27537542&inboundaltsenabled=false&infants=0&originentityid=33367910&outboundaltsenabled=true&preferdirects=false&ref=home&rtn=1",
    "Buenos Aires": "https://www.skyscanner.com.tw/transport/flights/tnn/buea/230401/230430/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27536465&inboundaltsenabled=false&infants=0&originentityid=33367910&outboundaltsenabled=true&preferdirects=false&ref=home&rtn=1",
    "Sydney": "https://www.skyscanner.com.tw/transport/flights/tnn/syd/230401/230430/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27547097&inboundaltsenabled=false&infants=0&originentityid=33367910&outboundaltsenabled=true&preferdirects=false&ref=home&rtn=1",
    "Jakarta": "https://www.skyscanner.com.tw/transport/flights/tnn/cgki/230401/230430/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27539774&inboundaltsenabled=false&infants=0&originentityid=33367910&outboundaltsenabled=true&preferdirects=false&ref=home&rtn=1",
    "Kyiv": "https://www.skyscanner.com.tw/transport/flights/tnn/kiev/230401/230430/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27542803&inboundaltsenabled=false&infants=0&originentityid=33367910&outboundaltsenabled=true&preferdirects=false&ref=home&rtn=1",
    "Lisboa": "https://www.skyscanner.com.tw/transport/flights/tnn/lis/230401/230430/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27544072&inboundaltsenabled=false&infants=0&originentityid=33367910&outboundaltsenabled=true&preferdirects=false&ref=home&rtn=1",
    "Chungqing": "https://www.skyscanner.com.tw/transport/flights/tnn/ckg/230401/230430/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27539818&inboundaltsenabled=false&infants=0&originentityid=33367910&outboundaltsenabled=true&preferdirects=false&ref=home&rtn=1",
    "Cairo": "https://www.skyscanner.com.tw/transport/flights/tnn/cai/230401/230430/?adults=1&adultsv2=1&cabinclass=economy&children=0&childrenv2=&destinationentityid=27539681&inboundaltsenabled=false&infants=0&originentityid=33367910&outboundaltsenabled=true&preferdirects=false&ref=home&rtn=1",
}


def revolution(latitude: int, longtitude: int):
     
    GPIO.setmode(GPIO.BCM)
     
    STEPS_PER_REVOLUTION = (int)(2070 * (longtitude / 180.0))#32 * 64
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
        pwm.change_pwm_go(latitude + 12)
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
        
    
            
def reverse(latitude: int, longtitude: int):
     
    GPIO.setmode(GPIO.BCM)
     
    STEPS_PER_REVOLUTION = (int)(2070 * (longtitude / 180.0)) + 60
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
        pwm.change_pwm_back(latitude)
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

    language = 0
    text = input("請輸入你想要的語言")
    if text in ["中文", "Chinese", "z"]:
        language = 0
    elif text in ["台語", "Taiwanese", "t"]:
        language = 1
    
    while True:
        if language == 1:
            tts.tts("你想查哪座城市?")
        elif language == 0:
            ctts.ch_tts("你想查哪座城市?")
        print("錄音開始")
        record.record()
        request = cstt.recognize_request("recording.wav", language)
        city = request.replace(" ", "") 
        print(city)
        city = alias_list[city] 
        latitude = coordinate_list[city][0]
        longtitude = coordinate_list[city][1]
        thread = threading.Thread(target = ctts.ch_tts, args=(intro_list[city], )) 
        if language == 1:
            thread = threading.Thread(target = tts.tts, args=(intro_list[city], ))
        revolution(latitude, 360-longtitude)
        browser.search_page(url_list[city])
        thread.start()
        pc.display_text(intro_list[city], city + ".png")
        #tts.tts(intro_list[city])
        thread.join()
        reverse(latitude, 360-longtitude)
        
