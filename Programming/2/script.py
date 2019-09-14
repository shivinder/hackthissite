#!/usr/bin/env python3

from PIL import Image
import translator

# TODO: fetch the png with code instead of saving it manually
# for now, we will have to save it on the disk manually
url = 'https://www.hackthissite.org/missions/prog/2/PNG.png'
png_filename = url.split('/')[-1]

# initialise the morse decoder here
decoder = translator.Decoder()

# start working with the image
png_image_bytes = Image.open(png_filename,'r').tobytes()

# declare the counter
counter, offset = 0, 0
morse_code = ''

# begin traversal through the bytes
for byte in png_image_bytes:
    # this is the ascii code
    if byte == 1:
        morse_code += chr((counter-offset))
        offset = counter

    counter += 1

# print the morse code
print('Morse Code: {}'.format(morse_code))

# decode the morse code
print('Plain Text: {}'.format(decoder.decode(morse_code).plaintext))