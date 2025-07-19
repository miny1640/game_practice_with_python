import pygame

def create_pixel_art_rects(shape_map, start_x, start_y, pixel_size=10):
    """
    텍스트로 정의된 모양을 기반으로 pygame.Rect 객체 리스트를 생성합니다.
    """
    rects = []
    for y_index, row in enumerate(shape_map):
        for x_index, char in enumerate(row):
            if char == 'x':
                # 'x' 문자를 만나면 해당 위치에 사각형을 추가합니다.
                rect = pygame.Rect(
                    start_x + (x_index * pixel_size),
                    start_y + (y_index * pixel_size),
                    pixel_size,
                    pixel_size
                )
                rects.append(rect)
    return rects
