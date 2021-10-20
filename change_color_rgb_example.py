import copy
from PIL import Image
import colorsys
import random

def convert_palette_to_hsv(palette):
    hsv_palette = []
    for i in range(0, len(palette)):
        hsv_palette.append(colorsys.rgb_to_hsv(palette[i][0]/255.0, palette[i][1]/255.0, palette[i][2]/255.0))
        hsv_palette[i] = (round(hsv_palette[i][0]*360/10, 0)*10, round(hsv_palette[i][1], 2), round(hsv_palette[i][2], 2))
    return hsv_palette

def x_in_palette(x, palette):
    for color in palette:
        if round_color(x) == round_color(color):
            return True
    return False

def round_color(x):
    a = (round(x[0]/10, 0)*10, round(x[1], 2), round(x[2], 2))
    return a

def change_color_skin(values, palette, delta_red, delta_green, delta_blue, mode):
    new_values = copy.deepcopy(values)
    for i in range(0, len(values)):
        for j in range(0, len(values[i])):
            if(mode == 'HSV'):
                x = round_color(values[i][j])
            else:
                x = values[i][j]
            if(x_in_palette(x, palette)):
                new_values[i][j] = ((x[0] + delta_red), (x[1] + delta_green),(x[2] + delta_blue))
            else:
                new_values[i][j] = x
    return new_values

def make_image(values, name):
    image = Image.new('RGB', (len(values[0]), len(values)))
    values = [item for sublist in values for item in sublist]
    image.putdata(values)
    image.save(name + '.png')

def convert_image_to_list(image):
    rgb_image = image.convert('RGB')
    rgb_values = []
    for j in range(0, rgb_image.size[1]):
        rgb_values.append([])
        for i in range(0, rgb_image.size[0]):
            rgb_values[j].append(rgb_image.getpixel((i, j)))
    return rgb_values

def convert_list_to_rgb(values):
    new_values = copy.deepcopy(values)
    for i in range(0, len(values)):
        for j in range(0, len(values[i])):
            a = new_values[i][j]
            new_values[i][j] = colorsys.hsv_to_rgb(float(values[i][j][0]/360),
                                                   float(values[i][j][1]),
                                                   float(values[i][j][2]))
            x = new_values[i][j]
            new_values[i][j] = (int(new_values[i][j][0]*255),int(new_values[i][j][1]*255),int(new_values[i][j][2]*255))

    return new_values

def convert_list_to_hsv(values):
    new_values = copy.deepcopy(values)
    for i in range(0, len(values)):
        for j in range(0, len(values[i])):
            new_values[i][j] = colorsys.rgb_to_hsv(float(values[i][j][0])/255.0,
                                                   float(values[i][j][1])/255.0,
                                                   float(values[i][j][2])/255.0)
            new_values[i][j] = (int(new_values[i][j][0]*360),new_values[i][j][1],new_values[i][j][2])
    return new_values

#read the image®
image = Image.open('heart1.jpg')
rgb_values = convert_image_to_list(image)

purple = (89,66,148)
mid_purple = (65, 53, 115)
light_purple = (115, 54, 150)
white = (255, 255, 255)
pink = (173, 40, 157)
bright_pink = (165, 41, 155)
palette = (purple, mid_purple, light_purple, white, pink, bright_pink)

rgb_new = change_color_skin(rgb_values, palette, -10, 50, 20, 'RGB')
make_image(rgb_new, 'new_color_heart_#3')
#show image
#image.show()

