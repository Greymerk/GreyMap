import math

## Color functions for map generation ##

hsl_colors = {
    'oak':                      {'h':35,  's':70,  'l':60 },
    'birch':                    {'h':35,  's':90,  'l':80 },
    'blue_ice':                 {'h':200,  's':20,  'l':40 },
    'brick':                    {'h':15,  's':60,  'l':50 },
    'clay':                     {'h':20,  's':20,  'l':80 },
    'dirt':                     {'h':27,  's':51,  'l':15 },
    'spruce':                   {'h':35,  's':60,  'l':40 },
    'ice':                      {'h':200,  's':40,  'l':60 },
    'jungle':                   {'h':25,  's':80,  'l':60 },
    'dark_oak':                 {'h':35,  's':93,  'l':15 },
    'acacia':                   {'h':20,  's':80,  'l':60 },
    'lava':                     {'h':20,  's':100,  'l':50 },
    'log':                      {'h':35,  's':93,  'l':15 },
    'mushroom':                 {'h':53,  's':22,  'l':58 },
    'mycelium':                 {'h':35,  's':15,  'l':60 },
    'netherbrick':              {'h':5,  's':80,  'l':20 },
    'path':                     {'h':27,  's':51,  'l':30 },
    'packed_ice':               {'h':200,  's':40,  'l':80 },
    'sand':                     {'h':53,  's':22,  'l':58 },
    'snow':                     {'h':240, 's':20,  'l':90 },
    'terracotta':               {'h':20,   's':40,  'l':50 },
    'stone':                    {'h':192,   's':2,   'l':54 },
    'leaves':                   {'h':114, 's':64,  'l':22 },
    'oak_leaves':               {'h':114, 's':64,  'l':22 },  
    'birch_leaves':             {'h':90, 's':64,  'l':40 },  
    'spruce_leaves':            {'h':91, 's':64,  'l':17 },  
    'jungle_leaves':            {'h':100, 's':80,  'l':40 },  
    'acacia_leaves':            {'h':70, 's':70,  'l':25 },
    'dark_oak_leaves':          {'h':115, 's':75,  'l':20 },       
    'grass':                    {'h':94,  's':42,  'l':25 },
    'water':                    {'h':228, 's':50,  'l':23 },
    'wheat':                    {'h':50, 's':80,  'l':60 },
    'red':                      {'h':0,   's':80,   'l':50},
    'orange':                   {'h':35,   's':80,   'l':50},
    'yellow':                   {'h':60,   's':80,   'l':50},
    'lime':                     {'h':80,   's':80,   'l':50},
    'green':                    {'h':120,   's':80,   'l':50},
    'cyan':                     {'h':170,   's':80,   'l':50},
    'light_blue':               {'h':190,   's':80,   'l':50},
    'blue':                     {'h':240,   's':80,   'l':50},
    'magenta':                  {'h':300,   's':80,   'l':50},
    'purple':                   {'h':320,   's':80,   'l':50},
    'brown':                    {'h':30,   's':80,   'l':30},
    'pink':                     {'h':0,   's':80,   'l':80},
    'white':                    {'h':0,   's':0,   'l':100},
    'light_gray':               {'h':0,   's':0,   'l':70},
    'gray':                     {'h':0,   's':0,   'l':50},
    'dim_gray':                 {'h':0,   's':0,   'l':30},
    'black':                    {'h':0,   's':0,   'l':0},
    'red_terracotta':           {'h':0,   's':40,   'l':40},
    'orange_terracotta':        {'h':35,   's':40,   'l':40},
    'yellow_terracotta':        {'h':55,   's':90,   'l':40},
    'lime_terracotta':          {'h':80,   's':40,   'l':40},
    'green_terracotta':         {'h':120,   's':40,   'l':40},
    'cyan_terracotta':          {'h':170,   's':40,   'l':40},
    'light_blue_terracotta':    {'h':190,   's':40,   'l':40},
    'blue_terracotta':          {'h':240,   's':40,   'l':40},
    'magenta_terracotta':       {'h':300,   's':40,   'l':40},
    'purple_terracotta':        {'h':320,   's':40,   'l':40},
    'brown_terracotta':         {'h':30,   's':40,   'l':40},
    'pink_terracotta':          {'h':0,   's':40,   'l':40},
    'white_terracotta':         {'h':20,   's':30,   'l':90},
    'light_gray_terracotta':    {'h':20,   's':20,   'l':70},
    'gray_terracotta':          {'h':10,   's':10,   'l':50},
    'dim_gray_terracotta':      {'h':10,   's':10,   'l':30},
    'black_terracotta':         {'h':10,   's':20,   'l':20},
    'copper':                   {'h':29,   's':57,   'l':46},
    'adobe':                    {'h':30,   's':76,   'l':69},
    'cherry_log':               {'h':300,   's':90,   'l':10},
    'cherry':                   {'h':300,   's':90,   'l':90}
}

# Hue given in degrees,
# saturation and lightness given either in range 0-1 or 0-100 and returned in kind
def hsl_slide(hsl1, hsl2, ratio):
    if (abs(hsl2['h'] - hsl1['h']) > 180):
        if (hsl1['h'] > hsl2['h']):
            hsl1['h'] -= 360
        else:
            hsl1['h'] += 360
    
    # Find location of two colors on the H/S color circle
    p1x = math.cos(math.radians(hsl1['h']))*hsl1['s']
    p1y = math.sin(math.radians(hsl1['h']))*hsl1['s']
    p2x = math.cos(math.radians(hsl2['h']))*hsl2['s']
    p2y = math.sin(math.radians(hsl2['h']))*hsl2['s']
    
    # Slide part of the way from tint to base color
    avg_x = p1x + ratio*(p2x-p1x)
    avg_y = p1y + ratio*(p2y-p1y)
    avg_h = math.atan(avg_y/avg_x)
    avg_s = avg_y/math.sin(avg_h)
    avg_l = hsl1['l'] + ratio*(hsl2['l']-hsl1['l'])
    avg_h = math.degrees(avg_h)
    
    #print('tint: %s base: %s avg: %s %s %s' % (tint,final_color,avg_h,avg_s,avg_l))
    return {'h':avg_h, 's':avg_s, 'l':avg_l}

# From http://www.easyrgb.com/index.php?X=MATH&H=19#text19
def hsl2rgb(H,S,L):
    H = H/360.0
    S = S/100.0 # Turn into a percentage
    L = L/100.0
    if (S == 0):
        return (int(L*255), int(L*255), int(L*255))
    var_2 = L * (1+S) if (L < 0.5) else (L+S) - (S*L)
    var_1 = 2*L - var_2

    def hue2rgb(v1, v2, vH):
        if (vH < 0): vH += 1
        if (vH > 1): vH -= 1
        if ((6*vH)<1): return v1 + (v2-v1)*6*vH
        if ((2*vH)<1): return v2
        if ((3*vH)<2): return v1 + (v2-v1)*(2/3.0-vH)*6
        return v1
        
    R = int(255*hue2rgb(var_1, var_2, H + (1.0/3)))
    G = int(255*hue2rgb(var_1, var_2, H))
    B = int(255*hue2rgb(var_1, var_2, H - (1.0/3)))
    return (R,G,B)
