import pygame
from env import SCREEN_WIDTH, MONSTER, BLACK

class Monster(pygame.sprite.Sprite):
    """몬스터 클래스: HP, 외형, 위치 등을 관리"""
    def __init__(self):
        super().__init__()
        self.name = MONSTER["name"]
        self.max_hp = MONSTER["hp"]
        self.hp = self.max_hp
        self.xp_reward = MONSTER["xp_reward"]
        
        # 몬스터 외형 설정
        self.image = pygame.Surface([MONSTER["size"], MONSTER["size"]])
        self.image.fill(MONSTER["color"])
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH / 2
        self.rect.y = MONSTER["y_pos"]

        # 폰트 설정 및 이름 표시
        font = pygame.font.SysFont(MONSTER["font"], MONSTER["font_size"], bold=True)
        text_surf = font.render(self.name, True, BLACK)
        text_rect = text_surf.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surf, text_rect)

    def take_damage(self, amount):
        """몬스터가 데미지를 입는 메소드"""
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        """몬스터의 생존 여부를 반환"""
        return self.hp > 0

    def respawn(self, level):
        """새로운 몬스터로 리스폰. 플레이어 레벨에 따라 강해집니다."""
        self.max_hp = int(MONSTER["hp"] * (1.2 ** (level - 1)))
        self.hp = self.max_hp
        self.xp_reward = int(MONSTER["xp_reward"] * (1.1 ** (level - 1)))
        print(f"새로운 몬스터(HP: {self.hp})가 나타났습니다!")