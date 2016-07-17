from PIL import Image, ImageDraw, ImageFont
from gen_messages import get_lines
import uuid

def draw_center_text(draw_obj, W, H, font_path, font_name, text, y_pos, font_size, font_color):
    font  =  ImageFont.truetype ( font_path + font_name, font_size )
    text_x, text_y = font.getsize(text)
    x = (W - text_x)/2
    draw_obj.text ( (x, y_pos), text, font=font, fill=font_color )

def get_filename(prefix='tplogo', filetype='png'):
    filename = '%s_%s.%s' % ( prefix, str(uuid.uuid4().fields[-1]), filetype )
    return filename

def gen_logo(outputdir='logos/'):
    W, H = (400, 250)
    COLOR_BLUE = (0,0,116)
    COLOR_RED = (174,0,4)
    FONT_PATH = 'fonts/'
    img_output = outputdir + get_filename()

    message = [{
        'text': 'TRUMP',
        'y': 135,
        'size': 35,
        'color': COLOR_BLUE,
        'font': 'Berthold_Akzidenz_Grotesk_Bold_Extended.otf'
    }, {
        'text': 'PENCE',
        'y': 175,
        'size': 26,
        'color': COLOR_RED,
        'font': 'Berthold_Akzidenz_Grotesk_Bold_Extended.otf'
    }, {
        'text': 'MAKE AMERICA GREAT AGAIN!',
        'y': 215,
        'size': 16,
        'color': COLOR_BLUE,
        'font': 'Berthold_Akzidenz_Grotesk_Bold.otf'
    }]


    # Get random messages and replace appropriately in dictionary
    random_message = get_lines()
    message[0]['text'] = random_message[0]
    message[1]['text'] = random_message[1]
    message[2]['text'] = message[2]['text'].replace('GREAT', random_message[2])

    base = Image.open("logo_template.png").convert('RGBA')
    txt = Image.new('RGBA', base.size, (255,255,255,0))
    draw = ImageDraw.Draw(txt)

    for line in message:
        draw_center_text(draw, W, H, FONT_PATH, line['font'], line['text'].upper(), line['y'], line['size'], line['color'])

    out = Image.alpha_composite(base, txt)
    out.save(img_output)
    return img_output
    
