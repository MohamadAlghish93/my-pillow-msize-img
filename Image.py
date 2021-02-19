from PIL import Image

image = Image.open('wide-header.png')

# The file format of the source file.
print(image.format) # Output: JPEG

# The pixel format used by the image. Typical values are “1”, “L”, “RGB”, or “CMYK.”
print(image.mode) # Output: RGB

# Image size, in pixels. The size is given as a 2-tuple (width, height).
print(image.size) # Output: (1200, 776)

# Colour palette table, if any.
print(image.palette) # Output: None


new_image = image.resize((620, 115))
new_image.save('wide-header_620.png')

print('>>>>>>>')
print(image.size) # Output: (1200, 776)
print(new_image.size) # Output: (400, 400)
