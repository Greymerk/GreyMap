
import json

class BlockEntity(object):

    def __init__(self, nbt):
        self.nbt = nbt
        self.x = self.nbt.get('x').value
        self.y = self.nbt.get('y').value
        self.z = self.nbt.get('z').value
    
    def getBlockName(self):
        blockType = self.nbt.get('id').value
        return blockType
        
    def getNBT(self):
        return self.nbt
        
    def getLocation(self):
        return self.x, self.y, self.z
    
class SignSide(object):
    
    def __init__(self, nbt):
        self.messages = []
        self.color = 'black'
        self.glow = False
        
        if(nbt is None):
            self.messages = ['','','','']
            return
            
        msgs = nbt.get('messages')
        for tag in msgs:
            j = json.loads(str(tag))
            self.messages.append(j['text'])
        
    def isEmpty(self):
        for line in self.messages:
            if len(line) > 0:
                return False
        return True
        
    def asObj(self):
        obj = {}
        obj['messages'] = self.messages
        obj['color'] = self.color
        obj['has_glowing_text'] = self.glow
        return obj
    
class Sign(BlockEntity):

    def __init__(self, nbt):
        BlockEntity.__init__(self, nbt)
        self.front = SignSide(nbt.get('front_text'))
        self.back = SignSide(nbt.get('back_text'))
            
    def __str__(self):
        return str(self.front.messages)
        
    def isEmpty(self):
        return self.front.isEmpty() and self.back.isEmpty()
    
    def is_marker(self):
        line = self.front.messages[0]
        if len(line) < 3:
            return False
        
        if not ((line[0] == '~') and (line[-1] == '~')):
            return False
        
        return True
        
    def asObj(self):
        obj = {}
        obj['front_text'] = self.front.asObj()
        obj['back_text'] = self.back.asObj()
        obj['x'] = self.x
        obj['y'] = self.y
        obj['z'] = self.z
        
        return obj