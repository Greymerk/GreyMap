from render.color import *
from struct import pack

from render.blocks import block_ignore,block_colors

# PIL module (not build-in)
try:
    from PIL import Image
except ImportError:
    # PIL not in search path. Let's see if it can be found in the parent folder
    sys.stderr.write("Module PIL/Image not found. Pillow (a PIL fork) can be found at http://python-imaging.github.io/\n")
    # Note: it may also be possible that PIL is installed, but JPEG support is disabled or broken
    sys.exit(70) # EX_SOFTWARE

def get_ground(chunk, x, z):

    if x < 0:
        x = 0
    if x > 15:
        x = 15
    if z < 0:
        z = 0
    if z > 15:
        z = 15

    max_height = chunk.get_max_height()
    ground = max_height    

    for y in range(max_height,-1,-1):
        block_id = chunk.get_block(x, y, z)
        if block_id != None:
            if (block_id not in block_ignore or y == 0):
                return y    
    return 0

def get_map(chunk):
    # Show an image of the chunk from above
    pixels = b""
    
    for z in range(16):
        for x in range(16):
            # Find the highest block in this column           
            ground_height = get_ground(chunk, x, z)
            block_id = chunk.get_block(x, ground_height, z)
          
            if block_id != None:
                if block_id in block_colors:
                    color = block_colors[block_id]
                else:
                    color = {'h':0, 's':0, 'l':100}
            else:
                #color = {'h':0, 's':0, 'l':0}
                return None

            #height_shift = (ground_height-64)*0.5
            height_shift = (ground_height - get_ground(chunk, x-1, z-1)) * 5

            final_color = {'h':color['h'], 's':color['s'], 'l':color['l'] + height_shift}
            if final_color['l'] > 100: final_color['l'] = 100
            if final_color['l'] < 0: final_color['l'] = 0

            rgb = hsl2rgb(final_color['h'], final_color['s'], final_color['l'])

            pixels += pack("BBB", rgb[0], rgb[1], rgb[2])

    im = Image.frombytes('RGB', (16,16), pixels)
    return im
    
def get_heightmap_image(chunk, buffer=False, gmin=False, gmax=False):
    points = chunk.blocks.generate_heightmap(buffer, True)
    # Normalize the points
    hmin = min(points) if (gmin == False) else gmin # Allow setting the min/max explicitly, in case this is part of a bigger map
    hmax = max(points) if (gmax == False) else gmax
    hdelta = hmax-hmin+0.0
    pixels = ""
    for y in range(16):
        for x in range(16):
            # pix X => mc -Z
            # pix Y => mc X
            offset = (15-x)*16+y
            height = int((points[offset]-hmin)/hdelta*255)
            if (height < 0): height = 0
            if (height > 255): height = 255
            pixels += pack(">B", height)
    im = Image.fromstring('L', (16,16), pixels)
    return im