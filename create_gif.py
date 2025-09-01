from PIL import Image
import imageio.v3 as iio
import os
import webbrowser

# Input images
filenames = ['team-pic1.png', 'team-pic2.png']
images = [iio.imread(f) for f in filenames]

# Save as GIF
gif_path = 'team.gif'
iio.imwrite(gif_path, images, duration=500, loop=0)

# Automatically open it in default viewer
abs_path = os.path.abspath(gif_path)
webbrowser.open(f'file://{abs_path}')
