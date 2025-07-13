import random
import pygame
from env import SCREEN_WIDTH, SCREEN_HEIGHT, RED


class Monster(pygame.sprite.Sprite):
    """몬스터 클래스: 위치, 크기 등을 관리"""
    def __init__(self):
        super().__init__()  # 스프라이트 초기화
        self.size = 50
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.respawn()  # 초기 위치 설정

    def respawn(self):
        """몬스터를 새로운 랜덤 위치에 다시 생성하는 메소드"""
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.size)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.size)
