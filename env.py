SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

HEALTH_SHAPES = [[
    "",
], [
    "  xx  ",
    " xxxx ",
    "xxxxxx",
    "xxxxxx",
    "xxxxxx",
], [
    "  xx   xx  ",
    " xxxx xxxx ",
    "xxxxxxxxxxx",
    "xxxxxxxxxxx",
    "xxxxxxxxxxx",
], [
    "  xx   xx  ",
    " xxxx xxxx ",
    "xxxxxxxxxxx",
    "xxxxxxxxxxx",
    "xxxxxxxxxxx",
    " xxxxx",
    "  xxxx",
    "   xxx",
    "    xx",
    "     x",
], [
    "  xx   xx  ",
    " xxxx xxxx ",
    "xxxxxxxxxxx",
    "xxxxxxxxxxx",
    "xxxxxxxxxxx",
    " xxxxxxxxx ",
    "  xxxxxxx  ",
    "   xxxxx   ",
    "    xxx    ",
    "     x     ",
]]

XP_BAR = {
            "bg" : (220, 220, 220), 
            "fill" : (124, 252, 0),
            "font_size" : 15,
            "rect" : {
                "x" : 0,
                "y" : 0,
                "width" : SCREEN_WIDTH,
                "height" : 10
            }
}

HEALTH = {
            "bg" : (220, 220, 220), 
            "fill" : RED,
            "pixel_size" : 2,
            "x" : 0,
            "y" : XP_BAR["rect"]["height"] + 2,
            "tile_count" : len(HEALTH_SHAPES[len(HEALTH_SHAPES) - 1][0]),
            "full_heart" : len(HEALTH_SHAPES) - 1,
            "shapes" : HEALTH_SHAPES,
}

BLOCK = {
            "spawn_screen" : {
                                "width" : SCREEN_WIDTH, 
                                "height":SCREEN_HEIGHT - 100
                            },
            "size" : 100,
            "font_size" : 30,
            "font" : "malgungothic",
            "font_color" : WHITE,
            "colors" : [(252, 97, 165), (248, 193, 223), (245, 157, 196), (222, 86, 141), (154, 62, 95), 
                        (136, 24, 65), (79, 10, 39), (244, 216, 189), (201, 152, 120), (140, 86, 56), 
                        (54, 23, 8), (242, 165, 156), (198, 89, 75), (125, 165, 200), (14, 17, 70)
                        ],
}
BLOCKS_COUNT = BLOCK["spawn_screen"]["width"] * (SCREEN_HEIGHT - BLOCK["spawn_screen"]["height"]) // (BLOCK["size"] ** 2)
BLOCKS_X_TILE_COUNT = BLOCK["spawn_screen"]["width"] // BLOCK["size"]
BLOCKS_Y_TILE_COUNT = BLOCK["spawn_screen"]["height"] // BLOCK["size"]
