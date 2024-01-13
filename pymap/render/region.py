from nbt.chunk import AnvilChunk

from render.chunk import get_map
import os, sys
import pathlib
import time

import json

# PIL module (not build-in)
try:
    from PIL import Image
except ImportError:
    # PIL not in search path. Let's see if it can be found in the parent folder
    sys.stderr.write("Module PIL/Image not found. Pillow (a PIL fork) can be found at http://python-imaging.github.io/\n")
    # Note: it may also be possible that PIL is installed, but JPEG support is disabled or broken
    sys.exit(70) # EX_SOFTWARE

class RegionRenderer(object):

    def __init__(self, region):
        self.region = region

    def is_region_updated(self):
        
        rx,rz = self.region.get_location()
        
        basePath = os.getcwd()
        regionDir = os.path.join(basePath, 'regions')
        #filename = os.path.basename(str(rx) + '.' + str(rz))+".png")
        filename = os.path.join(regionDir, str(rx) + '.' + str(rz)+".png")
        
        #imgfilename = os.path.basename(str(rx) + '.' + str(rz))+".png"
        if not os.path.exists(filename):
            return False

        imgtime = os.path.getmtime(filename)
        return self.region.timestamp < imgtime
    
    def render_region_map(self):
        
        lastUpdate = self.readLastUpdateTime()
        rx,rz = self.region.get_location()
        basePath = os.getcwd()
        regionDir = os.path.join(basePath, 'regions')
        filename = os.path.join(regionDir, str(rx) + '.' + str(rz)+".png")
        
        if(os.path.isfile(filename)):
            region_map = Image.open(filename, mode='r')
            region_map.load()
        else:
            region_map = Image.new('RGB', (16*32,16*32))
            
        t = 32 * 32
        
        for i, nbtfile in enumerate(self.region.iter_chunks()):
            chunk = AnvilChunk(nbtfile)
            if i % 128 ==0:
                sys.stdout.write("Rendering image")
            elif i % 4 == 0:
                sys.stdout.write(".")
                sys.stdout.flush()
            elif i % 128 == 127:
                sys.stdout.write("%5.1f%%\n" % (100*float(i)/t))
            if(chunk.get_last_update() < lastUpdate):
                continue
            chunkmap = get_map(chunk)
            if(chunkmap is None):
                continue
            x,z = chunk.get_coords()
            region_map.paste(chunkmap, (16*(x%32),16*(z%32)))
            
        print(" done\n")
        region_map.save(filename,"PNG")
        print("Saved map as %s" % filename)
            
        
    def update_poi(self):
        print('updating poi: ' + str(self.region.get_location()))
        signList = []
        
        for i, nbtfile in enumerate(self.region.iter_chunks()):
            
            chunk = AnvilChunk(nbtfile)
            signs = chunk.get_signs()
            for s in signs:
                if not s.isEmpty():
                    signList.append(s.asObj())

        rx,rz = self.region.get_location()    
        
        basePath = os.getcwd()
        sDir = os.path.join(basePath, 'signs')
        filename = os.path.join(sDir, str(rx) + '.' + str(rz)+".json")
        with open(filename, 'w') as f:
            len(signList)
            f.write(json.dumps(signList, ensure_ascii=False))
        print("Saved signs as %s" % filename)
        
    def readLastUpdateTime(self):
        basePath = os.getcwd()
        filename = os.path.join(basePath, 'last_update.txt')
        with open(filename, 'r') as f:
            lastUpdate = f.read()
            #print('last update', lastUpdate)
        return int(lastUpdate)
        
