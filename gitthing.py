# Author: Johnofsicily
# Description: Simple script to generate a computer art image using Python
# Tags: photography, computer art, generative

from PIL import Image, ImageDraw
import random

WIDTH, HEIGHT = 800, 600
img = Image.new('RGB', (WIDTH, HEIGHT), 'white')
draw = ImageDraw.Draw(img)

# Draw random colored circles for a generative art effect
for _ in range(100):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    r = random.randint(20, 100)
    color = tuple(random.randint(0, 255) for _ in range(3))
    draw.ellipse((x - r, y - r, x + r, y + r), fill=color, outline=None)

img.save('johnofsicily_art.png')
print("Art generated and saved as johnofsicily_art.png!")
