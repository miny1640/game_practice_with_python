import pygame
from env import BLOCK, BLOCKS_COUNT, BLOCKS_X_TILE_COUNT


class Block(pygame.sprite.Sprite):
    """블록 클래스: 위치, 크기 등을 관리"""
    def __init__(self, key, idx):
        super().__init__()  # 스프라이트 초기화
        self.key = key
        self.size = BLOCK["size"]
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(BLOCK["colors"][idx % len(BLOCK["colors"])])
        self.rect = self.image.get_rect()

        # 폰트 설정 및 키 표시
        font = pygame.font.SysFont(BLOCK["font"], BLOCK["font_size"], bold=True) # 폰트 및 크기 설정
        key_name_map = {
            pygame.K_UP: "↑",
            pygame.K_DOWN: "↓",
            pygame.K_LEFT: "←",
            pygame.K_RIGHT: "→",
        }
        # 맵에 키가 있으면 해당 심볼을, 없으면 키의 이름을 대문자로 사용
        key_name = key_name_map.get(self.key, pygame.key.name(self.key).upper())
        text_surf = font.render(key_name, True, BLOCK["font_color"])  # 텍스트 Surface 생성
        
        # 텍스트를 몬스터 이미지의 중앙에 위치시키기
        text_rect = text_surf.get_rect(center=self.image.get_rect().center)
        self.image.blit(text_surf, text_rect) # 몬스터 이미지에 텍스트 그리기

        self.respawn(idx)  # 초기 위치 설정
        self.is_dying = False
        self.animation_speed = 20

    def start_death_animation(self):
        """블록이 사라지는 애니메이션을 시작합니다."""
        self.is_dying = True

    def update(self):
        """블록의 상태를 업데이트합니다. (애니메이션 등)"""
        if self.is_dying:
            self.rect.x -= self.animation_speed
            # 화면 왼쪽 밖으로 완전히 나가면 스스로를 제거합니다.
            if self.rect.right < 0:
                self.kill()

    def respawn(self, idx):
        """블록을 정해진 위치에 다시 생성하는 메소드"""
        if idx < BLOCKS_COUNT:
            self.rect.x = idx % BLOCKS_X_TILE_COUNT * self.size
            self.rect.y = BLOCK["spawn_screen"]["height"] + idx // BLOCKS_X_TILE_COUNT * self.size
        