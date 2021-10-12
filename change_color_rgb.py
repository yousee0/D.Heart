import copy

from PIL import Image

def convert_image_to_list(image):
    rgb_image = image.convert('RGB')
    rgb_values = []
    for j in range(0, rgb_image.size[1]):
        rgb_values.append([])
        for i in range(0, rgb_image.size[0]):
            rgb_values[j].append(rgb_image.getpixel((i,j)))
    return rgb_values

def change_color_skin(values, palette, delta_red, delta_green, delta_blue, mode):
    new_values = copy.deepcopy()

#read the image
image = Image.open('heart1.jpg')
rgb_values = convert_image_to_list(image)

purple = (89,66,148)
mid_purple = (65, 53, 115)
light_purple = (115, 54, 150)
white = (255, 255, 255)
pink = (173, 40, 157)
bright_pink = (165, 41, 155)
palette = (purple, mid_purple, light_purple, white, pink, bright_pink)

rgb_new = change_color_skin(rgb_values, palette, -100, 50, 200)
make_image(rgb_new, 'new_color_heart_#2')
#show image
#image.show()

