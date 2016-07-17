from PIL import Image, ImageDraw, ImageFont

def draw_center_text(draw_obj, W, H, font_path, font_name, text, y_pos, font_size, font_color):
    font  =  ImageFont.truetype ( font_path + font_name, font_size )
    text_x, text_y = font.getsize(text)
    x = (W - text_x)/2
    draw_obj.text ( (x, y_pos), text, font=font, fill=font_color )

W, H = (400, 250)
COLOR_BLUE = (0,0,116)
COLOR_RED = (174,0,4)
FONT_PATH = 'fonts/'

message = [{
    'text': 'TERRIBLE',
    'y': 125,
    'size': 50,
    'color': COLOR_BLUE,
    'font': 'Berthold_Akzidenz_Grotesk_Bold_Extended.otf'
}, {
    'text': 'PENNANCE PAID',
    'y': 175,
    'size': 30,
    'color': COLOR_RED,
    'font': 'Berthold_Akzidenz_Grotesk_Bold_Extended.otf'
}, {
    'text': 'MAKE AMERICA BAD AGAIN!',
    'y': 215,
    'size': 16,
    'color': COLOR_BLUE,
    'font': 'Berthold_Akzidenz_Grotesk_Bold.otf'
}]

base = Image.open("logo_template.png").convert('RGBA')
txt = Image.new('RGBA', base.size, (255,255,255,0))
draw = ImageDraw.Draw(txt)

for line in message:
    draw_center_text(draw, W, H, FONT_PATH, line['font'], line['text'], line['y'], line['size'], line['color'])

out = Image.alpha_composite(base, txt)
out.show()
