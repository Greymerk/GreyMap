import os, sys

from nbt.world import WorldFolder,McRegionWorldFolder
from render.region import RegionRenderer

def generate(world_folder):
    world = WorldFolder(world_folder)
    for region in world.iter_regions():
        r = RegionRenderer(region)
        if not r.is_region_updated():
            try:
                r.render_region_map()
                r.update_poi()
            except KeyboardInterrupt:
                print(" aborted\n")
                exit()
                
        else:
            pass
            print("skipping region: " + str(region.get_location()))
    
    print('completed')
    worldDat = world.get_level_dat()
    worldTime = worldDat['Data']['Time'].value
    writeLastUpdateTime(worldTime)
        
        
def writeLastUpdateTime(time):
    basePath = os.getcwd()
    filename = os.path.join(basePath, 'last_update.txt')
    with open(filename, 'w') as f:
        f.truncate()
        f.write(str(time))
    
    '''
    if len(unknown_blocks) > 0:
        print("warning: unknown color for block ids:")    
        for block_id in unknown_blocks:
            print("%s" % block_id)
    '''

def generate_world_map(world_folder, show=True):
    world = WorldFolder(world_folder)
    bb = world.get_boundingbox()
    world_map = Image.new('RGB', (16*bb.lenx(),16*bb.lenz()))
    t = world.chunk_count()
    try:
        i =0.0
        for chunk in world.iter_chunks():
            if i % 50 ==0:
                sys.stdout.write("Rendering image")
            elif i % 2 == 0:
                sys.stdout.write(".")
                sys.stdout.flush()
            elif i % 50 == 49:
                sys.stdout.write("%5.1f%%\n" % (100*i/t))
            i +=1
            chunkmap = get_map(chunk)
            x,z = chunk.get_coords()
            world_map.paste(chunkmap, (16*(x-bb.minx),16*(z-bb.minz)))
        print(" done\n")
        filename = os.path.basename(world_folder)+".png"
        world_map.save(filename,"PNG")
        print("Saved map as %s" % filename)

    except KeyboardInterrupt:
        print(" aborted\n")
        filename = os.path.basename(world_folder)+".partial.png"
        world_map.save(filename,"PNG")
        print("Saved map as %s" % filename)
        return 75 # EX_TEMPFAIL
    if show:
        world_map.show()