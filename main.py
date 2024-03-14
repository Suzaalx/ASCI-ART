from PIL import Image
import subprocess
from colorama import Fore, Style

ASCII_CHARS = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
MAX_PIXEL_VALUE = 255

img = Image.open('image.jpeg')
img.thumbnail((200,200))
pixels = list(img.getdata())


# iterating through the pixels in steps of img.width(ex: the width of the image is 5 so we iterare thru the pixels in steps of 5 to get the pixels of the first row of the image, we go from 0 to 5 then 10...etc)
# and then we slice the pixels from i to i+img.width to get the pixels of that row and append them to the pixels matrix then we have 2d array of pixels
pixels_matrix = []
for i in range(0, len(pixels), img.width):
    pixels_matrix.append(pixels[i:i+img.width])


# get the intensity/ brightness of each pixel
intensity_matrix=[]
for row in pixels_matrix:
    intensity_row = []

    for p in row:
        # intensity= (max(p)+min(p)/2.0)
        intensity = 0.21*p[0] + 0.72*p[1] + 0.07*p[2]
        intensity_row.append(intensity)
    intensity_matrix.append(intensity_row)



# get the asci char for each intensity
ascii_matrix =[]
for row in intensity_matrix:
    ascii_row = []
    for p in row:
       
       ascii_row.append(ASCII_CHARS[int(p/MAX_PIXEL_VALUE * len(ASCII_CHARS)) - 1])

    ascii_matrix.append(ascii_row)

# printing the ascii art

for row in ascii_matrix:
    line = [p+p+p for p in row]
    print(Fore.WHITE + "".join(line))




