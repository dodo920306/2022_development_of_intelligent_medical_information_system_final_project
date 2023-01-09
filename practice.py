import time

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import Adafruit_SSD1306

def display_text(text, mood, *args):
    FONT_SIZE = 10
    disp = Adafruit_SSD1306.SSD1306_128_32(rst = 0)

    disp.begin()
    disp.clear()
    disp.display()

    width = disp.width
    height = 10

    # 1 bit pixel
    #image = Image.new('1', (width, height))
    image = Image.open(str(mood)).convert('1')
    
    #disp.image(image)
    #disp.display()

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype("./ARIALUNI.TTF", FONT_SIZE)

    pos = width

    maxwidth, unused = draw.textsize(text, font = font) 

    while True:
        draw.rectangle((0, 0, width, height), outline = 0, fill = 0)
        
        x = pos
        for i, c in enumerate(text):
            # Stop drawing if off the right side of screen.
            if x > width:
                break
            # Calculate width but skip drawing if off the left side of screen.
            if x < -10:
                char_width, char_height = draw.textsize(c, font=font)
                x += char_width
                continue
            # Calculate offset from sine wave.
            #y = offset+math.floor(amplitude*math.sin(x/float(width)*2.0*math.pi))
            y = 0
            # Draw text.
            draw.text((x, y), c, font=font, fill=255)
            # Increment x position based on chacacter width.
            char_width, char_height = draw.textsize(c, font=font)
            x += char_width
        # Draw the image buffer.
        disp.image(image)
        disp.display()
        # Move position for next frame.
        pos -= 2
        # Start over if text has scrolled completely off left side of screen.
        if pos < -maxwidth:
            #pos = startpos
            print('emotion printing...')
            break
        # Pause briefly before drawing next frame.
        
    disp.clear()
    disp.display()


    # if len(args) > 0:
    #     for i, item in enumerate(args):
    #         draw.text((0, (i + 1) * FONT_SIZE-1), item, font = font, fill = 255)
