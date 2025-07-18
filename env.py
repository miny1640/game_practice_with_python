SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

BLOCK = {
            "spawn_screen" : {
                                "width" : SCREEN_WIDTH, 
                                "height":SCREEN_HEIGHT // 2
                            },
            "size" : 50,
            "font_size" : 40,
            "colors" : [(252, 97, 165), (248, 193, 223), (245, 157, 196), (222, 86, 141), (154, 62, 95), 
                        (201, 152, 120), (136, 24, 65), (244, 216, 189), (240, 225, 85), (140, 86, 56), 
                        (79, 10, 39), (220, 232, 244), (125, 165, 200), (54, 23, 8), (242, 165, 156), 
                        (14, 17, 70), (198, 89, 75), (220, 244, 238), (171, 153, 43), (69, 98, 131), 
                        (130, 35, 24), (34, 32, 132), (140, 170, 151), (96, 86, 10), (81, 110, 93), 
                        (6, 19, 10), (238, 210, 3), (101, 109, 185), (109, 143, 114), (9, 91, 111)],
        }
BLOCKS_COUNT = BLOCK["spawn_screen"]["width"] * BLOCK["spawn_screen"]["height"] // (BLOCK["size"] ** 2)
BLOCKS_X_TILE_COUNT = BLOCK["spawn_screen"]["width"] // BLOCK["size"]
BLOCKS_Y_TILE_COUNT = BLOCK["spawn_screen"]["height"] // BLOCK["size"]
