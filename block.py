import random
import pygame
from env import WHITE, BLOCK, BLOCKS_COUNT, BLOCKS_X_TILE_COUNT



class Block(pygame.sprite.Sprite):
    attack_keys = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f]
    """몬스터 클래스: 위치, 크기 등을 관리"""
    def __init__(self, key, idx):
        super().__init__()  # 스프라이트 초기화
        self.key = key
        self.size = BLOCK["size"]
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(random.choice(BLOCK["colors"]))
        self.rect = self.image.get_rect()

        # 폰트 설정 및 키 표시
        font = pygame.font.Font(None, BLOCK["font_size"]) # 폰트 및 크기 설정
        key_name = pygame.key.name(self.key).upper() # 키 이름을 대문자로 변환 (e.g., 'a')
        text_surf = font.render(key_name, True, WHITE) # 텍스트 Surface 생성
        
        # 텍스트를 몬스터 이미지의 중앙에 위치시키기
        text_rect = text_surf.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surf, text_rect) # 몬스터 이미지에 텍스트 그리기

        self.respawn(idx)  # 초기 위치 설정

    def respawn(self, idx):
        """몬스터를 정해진 위치에 다시 생성하는 메소드"""
        if idx < BLOCKS_COUNT:
            self.rect.x = idx % BLOCKS_X_TILE_COUNT * self.size
            self.rect.y = BLOCK["spawn_screen"]["height"] + idx // BLOCKS_X_TILE_COUNT * self.size
        