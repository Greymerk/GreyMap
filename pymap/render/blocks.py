from render.color import hsl_colors

# List of blocks to ignore
# Uncomment all the lines to show underground structures

block_ignore = [
    'minecraft:air',  # At least this one
    'minecraft:cave_air'
#    'cave_air', 'water', 'lava', 'snow', 'ice',
#    'grass', 'tall_grass', 'dead_bush',
#    'seagrass', 'tall_seagrass', 'kelp', 'kelp_plant',
#    'dandelion', 'poppy', 'oxeye_daisy', 'white_tulip',
#    'azure_bluet', 'lilac', 'rose_bush', 'peony', 'blue_orchid',
#    'lily_pad', 'sugar_cane', 'vine', 'pumpkin', 'cactus',
#    'wheat', 'potatoes', 'beetroots', 'carrots',
#    'oak_leaves', 'dark_oak_leaves', 'birch_leaves',
#    'acacia_leaves', 'spruce_leaves',
#    'oak_log', 'dark_oak_log', 'birch_log',
#    'acacia_log', 'spruce_log',
#    'brown_mushroom', 'red_mushroom',
#    'brown_mushroom_block', 'red_mushroom_block', 'mushroom_stem',
#    'grass_block', 'grass_path', 'farmland', 'dirt',
#    'stone', 'sand', 'gravel', 'clay',
#    'sandstone', 'diorite', 'andesite', 'granite', 'obsidian',
#    'coal_ore', 'iron_ore', 'gold_ore', 'diamond_ore',
#    'redstone_ore', 'lapis_ore', 'emerald_ore',
#    'cobweb',
    ]


# Map of block colors from names
# Legacy block numeric identifiers are now hidden by Block class
# and mapped to alpha identifiers in best effort

block_colors = {
    'minecraft:acacia_slab':            hsl_colors['acacia'],
    'minecraft:acacia_trapdoor':        hsl_colors['acacia'],
    'minecraft:acacia_stairs':          hsl_colors['acacia'],
    'minecraft:acacia_wall_sign':       hsl_colors['acacia'],
    'minecraft:acacia_fence':           hsl_colors['acacia'],
    'minecraft:acacia_leaves':          hsl_colors['acacia_leaves'],
    'minecraft:acacia_log':             hsl_colors['log'],
    'minecraft:acacia_planks':          hsl_colors['acacia'],
    'minecraft:acacia_button':          hsl_colors['acacia'],
    'minecraft:air':                    hsl_colors['black'],
    'minecraft:allium':                 hsl_colors['magenta'],
    'minecraft:amethyst_block':         hsl_colors['purple'],
    'minecraft:andesite':               hsl_colors['gray'],
    'minecraft:attached_melon_stem':    hsl_colors['green'],
    'minecraft:attached_pumpkin_stem':  hsl_colors['green'],
    'minecraft:azalea':                 hsl_colors['leaves'],
    'minecraft:azalea_leaves':          hsl_colors['leaves'],
    'minecraft:azure_bluet':            hsl_colors['light_blue'],
    'minecraft:bamboo':                 hsl_colors['lime'],
    'minecraft:barrel':                 hsl_colors['spruce'],
    'minecraft:bedrock':                hsl_colors['dim_gray'],
    'minecraft:beehive':                hsl_colors['oak'],
    'minecraft:beetroots':              hsl_colors['green'],
    'minecraft:bell':                   hsl_colors['yellow'],
    'minecraft:big_dripleaf':           hsl_colors['green'],
    'minecraft:birch_fence':            hsl_colors['birch'],
    'minecraft:birch_fence_gate':       hsl_colors['birch'],
    'minecraft:birch_leaves':           hsl_colors['birch_leaves'],
    'minecraft:birch_log':              hsl_colors['white'],
    'minecraft:birch_planks':           hsl_colors['birch'],
    'minecraft:birch_sign':             hsl_colors['birch'],
    'minecraft:birch_sapling':          hsl_colors['birch_leaves'],
    'minecraft:birch_slab':             hsl_colors['birch'],
    'minecraft:birch_stairs':           hsl_colors['birch'],
    'minecraft:birch_trapdoor':         hsl_colors['birch'],
    'minecraft:birch_wall_sign':        hsl_colors['birch'],
    'minecraft:birch_pressure_plate':   hsl_colors['birch'],
    'minecraft:birch_pressure_plate':   hsl_colors['birch'],
    'minecraft:black_bed':              hsl_colors['black'],
    'minecraft:black_wool':             hsl_colors['black'],
    'minecraft:blue_ice':               hsl_colors['blue_ice'],
    'minecraft:blue_orchid':            hsl_colors['light_blue'],
    'minecraft:blue_terracotta':        hsl_colors['blue_terracotta'],
    'minecraft:bone_block':             hsl_colors['white'],
    'minecraft:bookshelf':              hsl_colors['oak'],
    'minecraft:brick_slab':             hsl_colors['brick'],
    'minecraft:brick_stairs':           hsl_colors['brick'],
    'minecraft:bricks':                 hsl_colors['brick'],
    'minecraft:brown_mushroom':         hsl_colors['mushroom'],
    'minecraft:brown_mushroom_block':   hsl_colors['mushroom'],
    'minecraft:brown_bed':              hsl_colors['brown'],
    'minecraft:bubble_column':          hsl_colors['water'],
    'minecraft:budding_amethyst':       hsl_colors['purple'],
    'minecraft:cactus':                 hsl_colors['green'],
    'minecraft:campfire':               hsl_colors['orange'],
    'minecraft:carrots':                hsl_colors['lime'],
    'minecraft:cave_air':               hsl_colors['black'],
    'minecraft:carved_pumpkin':         hsl_colors['orange'],
    'minecraft:chest':                  hsl_colors['oak'],
    'minecraft:chorus_flower':          hsl_colors['pink'],
    'minecraft:chorus_plant':           hsl_colors['pink'],
    'minecraft:chipped_anvil':          hsl_colors['dim_gray'],
    'minecraft:chiseled_sandstone':     hsl_colors['sand'],
    'minecraft:chiseled_stone_bricks':  hsl_colors['stone'],
    'minecraft:chiseled_quartz_block':  hsl_colors['white'],
    'minecraft:clay':                   hsl_colors['clay'],
    'minecraft:coal_ore':               hsl_colors['dim_gray'],
    'minecraft:coal_block':             hsl_colors['dirt'],
    'minecraft:coarse_dirt':            hsl_colors['dirt'],
    'minecraft:cobblestone':            hsl_colors['stone'],
    'minecraft:cobbled_deepslate_wall': hsl_colors['dim_gray'],
    'minecraft:cobbled_deepslate':      hsl_colors['dim_gray'],
    'minecraft:cobblestone_slab':       hsl_colors['stone'],
    'minecraft:cobblestone_stairs':     hsl_colors['stone'],
    'minecraft:cobblestone_wall':       hsl_colors['stone'],
    'minecraft:cobweb':                 hsl_colors['white'],
    'minecraft:cocoa':                  hsl_colors['brown'],
    'minecraft:comparator':             hsl_colors['light_gray'],
    'minecraft:composter':              hsl_colors['spruce'],
    'minecraft:copper_ore':             hsl_colors['dim_gray'],
    'minecraft:cornflower':             hsl_colors['light_blue'],
    'minecraft:crafting_table':         hsl_colors['oak'],
    'minecraft:cracked_stone_bricks':   hsl_colors['stone'],
    'minecraft:crimson_hyphae':         hsl_colors['red'],
    'minecraft:crimson_nylium':         hsl_colors['red'],
    'minecraft:crying_obsidian':        hsl_colors['black'],
    'minecraft:cut_red_sandstone':      hsl_colors['orange'],
    'minecraft:cut_sandstone_slab':     hsl_colors['orange'],
    'minecraft:cut_sandstone':          hsl_colors['sand'],
    'minecraft:cyan_carpet':            hsl_colors['cyan'],
    'minecraft:dandelion':              hsl_colors['yellow'],
    'minecraft:dark_oak_fence':         hsl_colors['dark_oak'],
    'minecraft:dark_oak_fence_gate':    hsl_colors['dark_oak'],
    'minecraft:dark_oak_leaves':        hsl_colors['dark_oak_leaves'],
    'minecraft:dark_oak_log':           hsl_colors['dark_oak'],
    'minecraft:dark_oak_planks':        hsl_colors['dark_oak'],
    'minecraft:dark_oak_wall_sign':     hsl_colors['dark_oak'],
    'minecraft:dark_oak_sapling':       hsl_colors['dark_oak_leaves'],
    'minecraft:dark_oak_stairs':        hsl_colors['dark_oak'],
    'minecraft:dark_oak_slab':          hsl_colors['dark_oak'],
    'minecraft:dark_oak_trapdoor':      hsl_colors['dark_oak'],
    'minecraft:dark_oak_door':          hsl_colors['dark_oak'],
    'minecraft:daylight_detector':      hsl_colors['light_gray'],
    'minecraft:dead_brain_coral_block': hsl_colors['light_gray'],
    'minecraft:dead_bush':              hsl_colors['brown'],
    'minecraft:deepslate':              hsl_colors['dim_gray'],
    'minecraft:deepslate_tiles':        hsl_colors['dim_gray'],
    'minecraft:dispenser':              hsl_colors['gray'],
    'minecraft:polished_deepslate_stairs': hsl_colors['dim_gray'],
    'minecraft:cobbled_deepslate_stairs': hsl_colors['dim_gray'],
    'minecraft:deepslate_tile_stairs':  hsl_colors['dim_gray'],
    'minecraft:deepslate_tile_wall':    hsl_colors['dim_gray'],
    'minecraft:diorite':                hsl_colors['white'],
    "minecraft:diorite_stairs":         hsl_colors['white'],
    'minecraft:diorite_wall':           hsl_colors['white'],
    'minecraft:dirt':                   hsl_colors['dirt'],
    'minecraft:dirt_path':              hsl_colors['path'],
    'minecraft:dripstone_block':        hsl_colors['stone'],
    'minecraft:emerald_block':          hsl_colors['lime'],
    'minecraft:emerald_ore':            hsl_colors['gray'],
    'minecraft:enchanting_table':       hsl_colors['red'],
    'minecraft:end_portal_frame':       hsl_colors['gray'],
    'minecraft:end_rod':                hsl_colors['white'],
    'minecraft:end_stone':              hsl_colors['sand'],
    'minecraft:ender_chest':            hsl_colors['black'],
    'minecraft:farmland':               hsl_colors['dirt'],
    'minecraft:fern':                   hsl_colors['grass'],
    'minecraft:fire':                   hsl_colors['orange'],
    'minecraft:flower_pot':             hsl_colors['brown'],
    'minecraft:flowering_azalea':       hsl_colors['leaves'],
    'minecraft:flowering_azalea_leaves': hsl_colors['leaves'],
    'minecraft:flowing_lava':           hsl_colors['lava'],
    'minecraft:flowing_water':          hsl_colors['water'],
    'minecraft:furnace':                hsl_colors['dim_gray'],
    'minecraft:glass_pane':             hsl_colors['light_gray'],
    'minecraft:glass':                  hsl_colors['light_gray'],
    'minecraft:glow_lichen':            hsl_colors['dim_gray'],
    'minecraft:glowstone':              hsl_colors['yellow'],
    'minecraft:gold_block':             hsl_colors['yellow'],
    'minecraft:gold_ore':               hsl_colors['light_gray'],
    'minecraft:granite':                hsl_colors['orange'],
    'minecraft:granite_wall':           hsl_colors['orange'],
    'minecraft:grass':                  hsl_colors['grass'],
    'minecraft:grass_block':            hsl_colors['grass'],
    'minecraft:short_grass':            hsl_colors['grass'],
    'minecraft:tall_grass':             hsl_colors['grass'],
    'minecraft:grass_path':             hsl_colors['brown'],
    'minecraft:gravel':                 hsl_colors['light_gray'],
    'minecraft:green_carpet':           hsl_colors['green'],
    'minecraft:green_terracotta':       hsl_colors['green'],
    'minecraft:green_wall_banner':      hsl_colors['green'],
    'minecraft:grindstone':             hsl_colors['dim_gray'],
    'minecraft:hay_block':              hsl_colors['wheat'],
    'minecraft:heavy_weighted_pressure_plate': hsl_colors['light_gray'],
    'minecraft:hopper':                 hsl_colors['dim_gray'],
    'minecraft:ice':                    hsl_colors['ice'],
    'minecraft:infested_stone':         hsl_colors['stone'],
    'minecraft:iron_ore':               hsl_colors['dim_gray'],
    'minecraft:iron_bars':              hsl_colors['light_gray'],
    'minecraft:iron_trapdoor':          hsl_colors['light_gray'],
    'minecraft:jack_o_lantern':         hsl_colors['orange'],
    'minecraft:jungle_button':          hsl_colors['jungle'],
    'minecraft:jungle_trapdoor':        hsl_colors['jungle'],
    'minecraft:jungle_fence':           hsl_colors['jungle'],
    'minecraft:jungle_fence_gate':      hsl_colors['jungle'],
    'minecraft:jungle_leaves':          hsl_colors['jungle_leaves'],
    'minecraft:jungle_log':             hsl_colors['log'],
    'minecraft:jungle_planks':          hsl_colors['jungle'],
    'minecraft:jungle_slab':            hsl_colors['jungle'],
    'minecraft:jungle_stairs':          hsl_colors['jungle'],
    'minecraft:kelp':                   hsl_colors['green'],
    'minecraft:ladder':                 hsl_colors['oak'],
    'minecraft:lantern':                hsl_colors['dim_gray'],
    'minecraft:lapis_block':            hsl_colors['blue'],
    'minecraft:lapis_ore':              hsl_colors['gray'],
    'minecraft:large_fern':             hsl_colors['green'],
    'minecraft:lava':                   hsl_colors['lava'],
    'minecraft:lectern':                hsl_colors['oak'],
    'minecraft:lever':                  hsl_colors['stone'],
    'minecraft:lilac':                  hsl_colors['pink'],
    'minecraft:lily_pad':               hsl_colors['green'],
    'minecraft:lily_of_the_valley':     hsl_colors['white'],
    'minecraft:light_gray_bed':         hsl_colors['light_gray'],
    'minecraft:light_blue_stained_glass': hsl_colors['light_blue'],
    'minecraft:light_gray_carpet':      hsl_colors['light_gray'],
    'minecraft:light_gray_terracotta':  hsl_colors['light_gray_terracotta'],
    'minecraft:lit_pumpkin':            hsl_colors['orange'],
    'minecraft:magma_block':            hsl_colors['lava'],
    'minecraft:mangrove_leaves':        hsl_colors['leaves'],
    'minecraft:mangrove_roots':         hsl_colors['brown'],
    'minecraft:melon':                  hsl_colors['lime'],
    'minecraft:melon_stem':             hsl_colors['green'],
    'minecraft:moss_block':             hsl_colors['green'],
    'minecraft:moss_carpet':            hsl_colors['green'],
    'minecraft:mossy_cobblestone':      hsl_colors['stone'],
    'minecraft:mossy_cobblestone_wall': hsl_colors['stone'],
    'minecraft:mossy_stone_bricks':     hsl_colors['stone'],
    'minecraft:mossy_stone_brick_slab': hsl_colors['stone'],
    'minecraft:mossy_stone_brick_stairs': hsl_colors['stone'],
    'minecraft:mossy_stone_brick_wall': hsl_colors['stone'],
    'minecraft:mushroom_stem':          hsl_colors['mushroom'],
    'minecraft:mud':                    hsl_colors['brown'],
    'minecraft:packed_mud':             hsl_colors['adobe'],
    'minecraft:mud_bricks':             hsl_colors['adobe'],
    'minecraft:mud_brick_stairs':       hsl_colors['adobe'],
    'minecraft:muddy_mangrove_roots':   hsl_colors['brown'],
    'minecraft:mycelium':               hsl_colors['mycelium'],
    'minecraft:nether_bricks':          hsl_colors['netherbrick'],
    'minecraft:nether_brick_slab':      hsl_colors['netherbrick'],
    'minecraft:nether_brick_stairs':    hsl_colors['netherbrick'],
    'minecraft:nether_brick_wall':      hsl_colors['netherbrick'],
    'minecraft:netherrack':             hsl_colors['red'],
    'minecraft:nether_wart_block':      hsl_colors['red'],
    'minecraft:oak_button':             hsl_colors['oak'],
    'minecraft:oak_door':               hsl_colors['oak'],
    'minecraft:oak_fence':              hsl_colors['oak'],
    'minecraft:oak_fence_gate':         hsl_colors['oak'],
    'minecraft:oak_leaves':             hsl_colors['oak_leaves'],
    'minecraft:oak_log':                hsl_colors['log'],
    'minecraft:oak_planks':             hsl_colors['oak'],
    'minecraft:oak_pressure_plate':     hsl_colors['oak'],
    'minecraft:oak_sapling':            hsl_colors['oak_leaves'],
    'minecraft:oak_sign':               hsl_colors['oak'],
    'minecraft:oak_slab':               hsl_colors['oak'],
    'minecraft:oak_stairs':             hsl_colors['oak'],
    'minecraft:oak_trapdoor':           hsl_colors['oak'],
    'minecraft:oak_wall_sign':          hsl_colors['oak'],
    'minecraft:obsidian':               hsl_colors['black'],
    'minecraft:observer':               hsl_colors['dim_gray'],
    'minecraft:orange_terracotta':      hsl_colors['orange_terracotta'],
    'minecraft:orange_tulip':           hsl_colors['orange'],
    'minecraft:oxeye_daisy':            hsl_colors['white'],
    'minecraft:packed_ice':             hsl_colors['packed_ice'],
    'minecraft:peony':                  hsl_colors['pink'],
    'minecraft:pink_tulip':             hsl_colors['pink'],
    'minecraft:pink_wall_banner':       hsl_colors['pink'],
    'minecraft:pointed_dripstone':      hsl_colors['stone'],
    'minecraft:poppy':                  hsl_colors['red'],
    'minecraft:podzol':                 hsl_colors['dirt'],
    'minecraft:polished_andesite':      hsl_colors['gray'],
    'minecraft:polished_diorite':       hsl_colors['white'],
    'minecraft:polished_granite':       hsl_colors['pink'],
    'minecraft:potatoes':               hsl_colors['green'],
    'minecraft:potted_allium':          hsl_colors['pink'],
    'minecraft:potted_azure_bluet':     hsl_colors['light_blue'],
    'minecraft:potted_dead_bush':       hsl_colors['brown'],
    'minecraft:potted_cactus':          hsl_colors['green'],
    'minecraft:potted_red_tulip':       hsl_colors['red'],
    'minecraft:prismarine':             hsl_colors['cyan'],
    'minecraft:prismarine_slab':        hsl_colors['cyan'],
    'minecraft:prismarine_stairs':      hsl_colors['cyan'],
    'minecraft:pumpkin':                hsl_colors['orange'],
    'minecraft:pumpkin_stem':           hsl_colors['green'],
    'minecraft:purple_wall_banner':     hsl_colors['purple'],
    'minecraft:purpur_block':           hsl_colors['pink'],
    'minecraft:purpur_slab':            hsl_colors['pink'],
    'minecraft:rail':                   hsl_colors['stone'],
    'minecraft:red_mushroom':           hsl_colors['red'],
    'minecraft:red_mushroom_block':     hsl_colors['red'],
    'minecraft:red_sand':               hsl_colors['orange'],
    'minecraft:red_wall_banner':        hsl_colors['red'],
    'minecraft:redstone_lamp':          hsl_colors['orange'],
    'minecraft:redstone_wall_torch':    hsl_colors['red'],
    'minecraft:redstone_wire':          hsl_colors['red'],
    'minecraft:redstone_block':         hsl_colors['red'],
    'minecraft:redstone_torch':         hsl_colors['red'],
    'minecraft:red_terracotta':         hsl_colors['red_terracotta'],
    'minecraft:red_tulip':              hsl_colors['red'],
    'minecraft:repeater':               hsl_colors['stone'],
    'minecraft:red_bed':                hsl_colors['red'],
    'minecraft:rooted_dirt':            hsl_colors['dirt'],
    'minecraft:rose_bush':              hsl_colors['red'],
    'minecraft:sugar_cane':             hsl_colors['lime'],
    'minecraft:sand':                   hsl_colors['sand'],
    'minecraft:sandstone':              hsl_colors['sand'],
    'minecraft:sandstone_slab':         hsl_colors['sand'],
    'minecraft:sandstone_stairs':       hsl_colors['sand'],
    'minecraft:sandstone_wall':         hsl_colors['sand'],
    'minecraft:shulker_box':            hsl_colors['pink'],
    'minecraft:red_shulker_box':        hsl_colors['red'],
    'minecraft:orange_shulker_box':     hsl_colors['orange'],
    'minecraft:yellow_shulker_box':     hsl_colors['yellow'],
    'minecraft:green_shulker_box':      hsl_colors['green'],
    'minecraft:lime_shulker_box':       hsl_colors['lime'],
    'minecraft:blue_shulker_box':       hsl_colors['blue'],
    'minecraft:cyan_shulker_box':       hsl_colors['cyan'],
    'minecraft:brown_shulker_box':      hsl_colors['brown'],
    'minecraft:gray_shulker_box':       hsl_colors['gray'],
    'minecraft:black_shulker_box':      hsl_colors['black'],
    'minecraft:white_shulker_box':      hsl_colors['white'],
    'minecraft:scaffolding':            hsl_colors['wheat'],
    'minecraft:seagrass':               hsl_colors['grass'],
    'minecraft:sea_lantern':            hsl_colors['cyan'],
    'minecraft:sea_pickle':             hsl_colors['grass'],
    'minecraft:shroomlight':            hsl_colors['yellow'],
    'minecraft:sign':                   hsl_colors['oak'],
    'minecraft:slime_block':            hsl_colors['lime'],
    'minecraft:skeleton_skull':         hsl_colors['light_gray'],
    'minecraft:small_dripleaf':         hsl_colors['lime'],
    'minecraft:smoker':                 hsl_colors['spruce'],
    'minecraft:smooth_basalt':          hsl_colors['white'],
    'minecraft:smooth_sandstone':       hsl_colors['sand'],
    'minecraft:smooth_sandstone_stairs': hsl_colors['sand'],
    'minecraft:smooth_sandstone_slab':  hsl_colors['sand'],
    'minecraft:smooth_stone_slab':      hsl_colors['light_gray'],
    'minecraft:smooth_stone':           hsl_colors['stone'],
    'minecraft:snow':                   hsl_colors['snow'],
    'minecraft:snow_block':             hsl_colors['snow'],
    'minecraft:soul_sand':              hsl_colors['brown'],
    'minecraft:spawner':                hsl_colors['dim_gray'],
    'minecraft:spruce_button':          hsl_colors['spruce'],
    'minecraft:spruce_fence':           hsl_colors['spruce'],
    'minecraft:spruce_fence_gate':      hsl_colors['spruce'],
    'minecraft:spruce_leaves':          hsl_colors['spruce_leaves'],
    'minecraft:spruce_log':             hsl_colors['log'],
    'minecraft:spruce_sapling':         hsl_colors['spruce_leaves'],
    'minecraft:spruce_stairs':          hsl_colors['spruce'],
    'minecraft:spruce_planks':          hsl_colors['spruce'],
    'minecraft:spruce_sign':            hsl_colors['spruce'],
    'minecraft:spruce_slab':            hsl_colors['spruce'],
    'minecraft:spruce_trapdoor':        hsl_colors['spruce'],
    'minecraft:spruce_wall_sign':       hsl_colors['spruce'],
    'minecraft:spruce_wood':            hsl_colors['log'],
    'minecraft:sticky_piston':          hsl_colors['stone'],
    'minecraft:stone':                  hsl_colors['stone'],
    'minecraft:stone_pressure_plate':   hsl_colors['stone'],
    'minecraft:stone_bricks':           hsl_colors['stone'],
    'minecraft:stone_brick_stairs':     hsl_colors['stone'],
    'minecraft:stone_brick_slab':       hsl_colors['stone'],
    'minecraft:stone_brick_wall':       hsl_colors['stone'],
    'minecraft:stone_button':           hsl_colors['stone'],
    'minecraft:stone_slab':             hsl_colors['stone'],
    'minecraft:stone_stairs':           hsl_colors['stone'],
    'minecraft:stripped_oak_log':       hsl_colors['log'],
    'minecraft:stripped_oak_wood':      hsl_colors['log'],
    'minecraft:stripped_spruce_wood':   hsl_colors['log'],
    'minecraft:sunflower':              hsl_colors['yellow'],
    'minecraft:sweet_berry_bush':       hsl_colors['green'],
    'minecraft:tall_grass':             hsl_colors['grass'],
    'minecraft:tall_seagrass':          hsl_colors['grass'],
    'minecraft:terracotta':             hsl_colors['terracotta'],
    'minecraft:torch':                  hsl_colors['yellow'],
    'minecraft:trapped_chest':          hsl_colors['oak'],
    'minecraft:tripwire':               hsl_colors['white'],
    'minecraft:tripwire_hook':          hsl_colors['gray'],
    'minecraft:tuff':                   hsl_colors['gray'],
    'minecraft:twisting_vines':         hsl_colors['cyan'],
    'minecraft:vine':                   hsl_colors['grass'],
    'minecraft:wall_torch':             hsl_colors['yellow'],
    'minecraft:water':                  hsl_colors['water'],
    'minecraft:water_cauldron':         hsl_colors['water'],
    'minecraft:warped_stem':            hsl_colors['cyan'],
    'minecraft:warped_roots':           hsl_colors['cyan'],
    'minecraft:warped_nylium':          hsl_colors['cyan'],
    'minecraft:warped_wart_block':      hsl_colors['cyan'],
    'minecraft:white_glazed_terracotta': hsl_colors['white_terracotta'],
    'minecraft:wheat':                  hsl_colors['wheat'],
    'minecraft:white_bed':              hsl_colors['white'],
    'minecraft:white_wool':             hsl_colors['white'],
    'minecraft:white_carpet':           hsl_colors['white'],
    'minecraft:white_terracotta':       hsl_colors['white_terracotta'],
    'minecraft:white_tulip':            hsl_colors['white'],
    'minecraft:white_wall_banner':      hsl_colors['white'],
    'minecraft:yellow_carpet':          hsl_colors['yellow'],
    'minecraft:yellow_terracotta':      hsl_colors['yellow_terracotta'],
    'minecraft:yellow_wool':            hsl_colors['yellow'],
    'minecraft:magenta_concrete':       hsl_colors['magenta'],
    'minecraft:pink_concrete':          hsl_colors['pink'],
    'minecraft:purple_concrete':        hsl_colors['purple'],
    'minecraft:white_concrete':         hsl_colors['white'],
    'minecraft:lightning_rod':          hsl_colors['copper'],
    'minecraft:blue_bed':               hsl_colors['blue'],
    'minecraft:anvil':                  hsl_colors['dim_gray'],
    'minecraft:polished_deepslate_slab': hsl_colors['dim_gray'],
    'minecraft:orange_wool':            hsl_colors['orange'],
    'minecraft:gray_wool':              hsl_colors['gray'],
    'minecraft:powered_rail':           hsl_colors['orange'],
    'minecraft:purple_wool':            hsl_colors['purple'],
    'minecraft:cobbled_deepslate_slab': hsl_colors['dim_gray'],
    'minecraft:mangrove_propagule':     hsl_colors['lime'],
    'minecraft:dragon_wall_head':       hsl_colors['dim_gray'],
    'minecraft:turtle_egg':             hsl_colors['white'],
    'minecraft:brown_wall_banner':      hsl_colors['brown'],
    'minecraft:acacia_fence_gate':      hsl_colors['acacia'],
    'minecraft:acacia_wood':            hsl_colors['acacia'],
    'minecraft:acacia_sapling':         hsl_colors['acacia_leaves'],
    'minecraft:cauldron':               hsl_colors['dim_gray'],
    'minecraft:powder_snow_cauldron':   hsl_colors['dim_gray'],
    'minecraft:black_wall_banner':      hsl_colors['black'],
    'minecraft:blue_stained_glass_pane':hsl_colors['blue'],
    'minecraft:blackstone_slab':        hsl_colors['black'],
    'minecraft:note_block':             hsl_colors['log'],
    'minecraft:blue_stained_glass':     hsl_colors['blue'],
    'minecraft:amethyst_cluster':       hsl_colors['magenta'],
    'minecraft:iron_door':              hsl_colors['light_gray'],
    'minecraft:polished_diorite_slab':  hsl_colors['white'],
    'minecraft:deepslate_iron_ore':     hsl_colors['dim_gray'],
    'minecraft:mangrove_stairs':        hsl_colors['jungle'],
    'minecraft:mangrove_slab':          hsl_colors['jungle'],
    'minecraft:end_stone_bricks':       hsl_colors['sand'],
    'minecraft:dark_oak_button':        hsl_colors['dark_oak'],
    'minecraft:yellow_bed':             hsl_colors['yellow'],
    'minecraft:light_gray_wool':        hsl_colors['light_gray'],
    'minecraft:deepslate_copper_ore':   hsl_colors['dim_gray'],
    'minecraft:note_block':             hsl_colors['log'],
    'minecraft:target':                 hsl_colors['white'],
    'minecraft:quartz_block':           hsl_colors['white'],
    'minecraft:stripped_birch_log':     hsl_colors['light_gray'],
    'minecraft:mangrove_planks':        hsl_colors['log'],
    'minecraft:andesite_slab':          hsl_colors['stone'],
    'minecraft:basalt':                 hsl_colors['stone'],
    'minecraft:pink_petals':            hsl_colors['cherry'],
    'minecraft:cherry_leaves':          hsl_colors['cherry'],
    'minecraft:cherry_sign':            hsl_colors['cherry'],
    'minecraft:cherry_slab':            hsl_colors['cherry'],
    'minecraft:cherry_planks':          hsl_colors['cherry'],
    'minecraft:cherry_fence':           hsl_colors['cherry'],
    'minecraft:cherry_fence_gate':      hsl_colors['cherry'],
    'minecraft:cherry_door':            hsl_colors['cherry'],
    'minecraft:cherry_button':          hsl_colors['cherry'],
    'minecraft:cherry_trap_door':       hsl_colors['cherry'],
    'minecraft:cherry_pressure_plate':  hsl_colors['cherry'],
    'minecraft:cherry_button':          hsl_colors['cherry'],
    
    }

















