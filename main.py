from PIL import Image
import subprocess
from colorama import Fore, Style

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_PIXEL_VALUE = 255

image= 'image.jpeg'
img = Image.open(image)
img.thumbnail((200,200))
pixels = list(img.getdata())
    


# iterating through the pixels in steps of img.width(ex: the width of the image is 5 so we iterare thru the pixels in steps of 5 to get the pixels of the first row of the image, we go from 0 to 5 then 10...etc)
# and then we slice the pixels from i to i+img.width to get the pixels of that row and append them to the pixels matrix then we have 2d array of pixels
def get_pixels_matrix(pixels, img):
    pixels_matrix = []
    for i in range(0, len(pixels), img.width):
        pixels_matrix.append(pixels[i:i+img.width])
    return pixels_matrix



# get the intensity/ brightness of each pixel
def get_intensity_brightness(pixels_matrix):
    intensity_matrix=[]
    for row in pixels_matrix:
        intensity_row = []
        for result in row:
            p = list(result)
            # p = [abs(value- MAX_PIXEL_VALUE) for value in p]
            

            lightness= ((max(p)+min(p))/2)
            average= (p[0]+p[1]+p[2])/3
            intensity = 0.21*p[0] + 0.72*p[1] + 0.07*p[2]
            value = (lightness + average+ intensity) / 3
            intensity_row.append(value)
        intensity_matrix.append(intensity_row)
    return intensity_matrix




# get the asci char for each intensity
def get_asci_char(intensity):
    ascii_matrix =[]
    for row in intensity:
        ascii_row = []
        for p in row:
        
            ascii_row.append(ASCII_CHARS[int(p/MAX_PIXEL_VALUE * len(ASCII_CHARS)) - 1])

        ascii_matrix.append(ascii_row)
    return ascii_matrix

# printing the ascii art
def print_ascii_art(ascii_matrix):
    for row in ascii_matrix:
        line = [p+p+p for p in row]
        print(Fore.WHITE + "".join(line))
        print(Style.RESET_ALL)

pixels_matrix = get_pixels_matrix(pixels, img)
intensity_matrix = get_intensity_brightness(pixels_matrix)
asci_matrix = get_asci_char(intensity_matrix)
print_ascii_art(asci_matrix)






