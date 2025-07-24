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
    " x xx ",
    "x xxxx",
    "x xxxx",
    "xxxxxx",
], [
    "  xx   xx  ",
    " x xx xxxx ",
    "x xxxxxxxxx",
    "x xxxxxxxxx",
    "xxxxxxxxxxx",
], [
    "  xx   xx  ",
    " x xx xxxx ",
    "x xxxxxxxxx",
    "x xxxxxxxxx",
    "xxxxxxxxxxx",
    " xxxxx",
    "  xxxx",
    "   xxx",
    "    xx",
    "     x",
], [
    "  xx   xx  ",
    " x xx xxxx ",
    "x xxxxxxxxx",
    "x xxxxxxxxx",
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
                                "width" : SCREEN_WIDTH - 100, 
                                "height":SCREEN_HEIGHT - 50
                            },
            "size" : 50,
            "font_size" : 30,
            "font" : "malgungothic",
            "font_color" : WHITE,
            "animation_speed" : 1,
            "colors" : [(252, 97, 165), (248, 193, 223), (245, 157, 196), (222, 86, 141), (154, 62, 95), 
                        (136, 24, 65), (79, 10, 39), (244, 216, 189), (201, 152, 120), (140, 86, 56), 
                        (54, 23, 8), (242, 165, 156), (198, 89, 75), (125, 165, 200), (14, 17, 70)
                        ],
}
BLOCKS_COUNT = BLOCK["spawn_screen"]["width"] * (SCREEN_HEIGHT - BLOCK["spawn_screen"]["height"]) // (BLOCK["size"] ** 2)
BLOCKS_X_TILE_COUNT = BLOCK["spawn_screen"]["width"] // BLOCK["size"]
BLOCKS_Y_TILE_COUNT = BLOCK["spawn_screen"]["height"] // BLOCK["size"]

MONSTER = {
            "name": "슬라임",
            "hp": 100,
            "xp_reward": 50, # 몬스터 처치 시 얻는 경험치
            "size": 100,
            "y_pos": 150,
            "color": (0, 200, 0),
            "font": "malgungothic",
            "font_size": 20,
}

MONSTER_HP_BAR = {
            "bg" : (220, 220, 220), 
            "fill" : (255, 0, 0),
            "font_size" : 20,
            "width": 300,
            "height": 25,
            "y": MONSTER["y_pos"] + MONSTER["size"] + 10, # 몬스터 아래에 위치
            "text_color": WHITE,
}
# HP 바를 화면 중앙에 위치시키기 위한 x 좌표 계산
MONSTER_HP_BAR["x"] = (SCREEN_WIDTH - MONSTER_HP_BAR["width"]) / 2
