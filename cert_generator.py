from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os

TEXT_Y_PIXEL = 610
TEXT_SIZE = 50
TEMPLATE_IMG = "template.jpg"
NAME_LIST_TXT = "participants_name.txt"
FONT_TTF_FILE = "Montserrat-SemiBold.ttf"

print(
    f"0. run: pip install -r requirements.txt\n1. Adjust final arguments (Variables with full uppercase) in cert_generator.py\n2. download font ttf file and place at the same directory\n3. save all target names as {NAME_LIST_TXT}\n4. place template image as {TEMPLATE_IMG}")
input("Press enter to start generate.")


def output_cert(name):
    img = Image.open(TEMPLATE_IMG)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)
    font = ImageFont.truetype(FONT_TTF_FILE, TEXT_SIZE)
    # draw.text((x, y),"Sample Text",(r,g,b))
    img_width, img_height = img.size
    text_width, text_height = font.getsize(name)

    draw.text((img_width/2 - text_width/2, TEXT_Y_PIXEL),
              name, (0, 0, 0), font=font)
    img.save(f'output/{name}.jpg')
    print('Generated', name)


if __name__ == "__main__":
    os.makedirs('output', exist_ok=True)
    names = []
    with open(NAME_LIST_TXT, 'r') as f:
        names = f.readlines()

    for name in names:
        name = name.replace("\n", "")
        name = name.replace("/", "")
        output_cert(name)
