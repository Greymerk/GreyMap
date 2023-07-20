import os
import subprocess
import json
import pathlib


if __name__ == '__main__':
    basePath = pathlib.Path(__file__).parent.resolve()
    os.chdir(basePath)
    configName = "settings.json"
    configFile = os.path.join(basePath, configName)
    #print(configFile)

    with open(configFile) as f:
        config = json.load(f)
        #print(data)

    pymapDir =  os.path.join(basePath, 'pymap')
    regionDir = os.path.join(basePath, 'regions')
    worldDir = config["world"]
    #print(pymapDir)
    #os.chdir(regionDir)
    
    subprocess.run(["python3", os.path.join(pymapDir, 'map.py'), worldDir])
