import pygame
from block import Block
from player import Player
import random
from env import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, BLOCKS_COUNT, RED, XP_BAR, LEVEL_RECT, HEALTH
from illustrator import create_pixel_art_rects



# --- 초기 설정 ---
pygame.init()

# 화면 크기
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("몬스터 잡고 레벨업!")

# 폰트 설정
font = pygame.font.Font(None, 40)
level_font = pygame.font.Font(None, 25)
xp_font = pygame.font.Font(None, 25)
health_font = pygame.font.Font(None, 25)

# 게임 시간 관련
clock = pygame.time.Clock()

# --- 게임 객체 생성 ---
player = Player() 
blocks = pygame.sprite.Group() # 화면에 그리기 및 업데이트를 위한 그룹
block_list = [] # 순서대로 블록을 참조하기 위한 리스트

attack_keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]

# 몬스터 그룹 생성
def create_blocks():
    global block_list
    blocks.empty()
    block_list = []
    for idx in range(BLOCKS_COUNT): 
        block = Block(random.choice(attack_keys), idx)
        blocks.add(block)
        block_list.append(block)

# UI 텍스트 그리기 (체력)
def create_health(health, color, x, y, pixel_size):
        health_pixels = []
        for _ in range(health // HEALTH["full_heart"]):
            health_pixels.append(HEALTH["shapes"][HEALTH["full_heart"]])
        health_pixels.append(HEALTH["shapes"][health % HEALTH["full_heart"]])

        for health_pixel in health_pixels:
            for health_rect in create_pixel_art_rects(health_pixel, x, y, pixel_size):
                pygame.draw.rect(screen, color, health_rect)
            x += pixel_size * HEALTH["tile_count"]

# --- 메인 게임 루프 ---
def hunt_monsters():
    create_blocks() # 게임 시작 시 첫 블록 웨이브 생성
    running = True
    you_died = False
    idx = 0
    while running:
        # 초당 60프레임으로 게임 속도 조절
        clock.tick(60)

        # 이벤트 처리 (키보드, 마우스 등)
        for event in pygame.event.get():
            # 윈도우를 닫거나 ESC를 누르면 종료
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            if event.type == pygame.KEYDOWN and event.key in attack_keys:
                # 처리해야 할 블록이 남아있는지 확인
                if idx < len(block_list):
                    effect_font = pygame.font.SysFont("malgungothic", 50)
                    if event.key == block_list[idx].key:
                        effect_text = "블록 처치!"
                        player.gain_xp(25) # 블록을 잡으면 25 XP 획득
                        block_list[idx].kill() # 블록을 그룹에서 제거 (화면에서 사라짐)
                        idx += 1
                    else:
                        effect_text = "헉 아푸다!"
                        player.lose_life()
                    screen.blit(effect_font.render(effect_text, True, BLACK), (SCREEN_WIDTH // 2 - 120, 150))
                    pygame.display.flip()
                    pygame.time.wait(50)

        # --- 게임 로직 업데이트 ---
        # 블록이 하나도 없으면 다음 웨이브 생성
        if not blocks:
            create_blocks()
            idx = 0

        # 게임 오버 조건 확인
        if player.health_remain <= 0:
            running = False
            you_died = True

        # --- 화면 그리기 ---
        # 배경색 채우기 (이전 프레임을 지우기 위해 루프 안에 위치)
        screen.fill(WHITE)

        # 몬스터 그룹에 포함된 모든 몬스터 그리기
        blocks.draw(screen)

        # UI 텍스트 그리기 (레벨)
        level_display_area = pygame.Rect(LEVEL_RECT)
        level_text = level_font.render(f"Lvl. {player.level}", True, BLACK)
        level_text_rect = level_text.get_rect(midleft=level_display_area.midleft)
        screen.blit(level_text, level_text_rect)
        
        # 경험치 비율 계산 (0.0 ~ 1.0)
        xp_ratio = player.xp / player.xp_to_next_level
        fill_width = int(XP_BAR["rect"]["width"] * xp_ratio)

        # 경험치 바 그리기 (배경 -> 채우기 -> 테두리 순서로 그려야 제대로 보입니다)
        xp_background_rect = pygame.Rect(XP_BAR["rect"]["x"], XP_BAR["rect"]["y"], XP_BAR["rect"]["width"], XP_BAR["rect"]["height"])
        xp_fill_rect = pygame.Rect(XP_BAR["rect"]["x"], XP_BAR["rect"]["y"], fill_width, XP_BAR["rect"]["height"])
        pygame.draw.rect(screen, XP_BAR["bg"], xp_background_rect)
        pygame.draw.rect(screen, XP_BAR["fill"], xp_fill_rect)

        # 경험치 텍스트를 바 위에 표시
        xp_text = xp_font.render(f"{player.xp} / {player.xp_to_next_level}", True, BLACK)
        screen.blit(xp_text, xp_text.get_rect(center=xp_background_rect.center))

        # UI 텍스트 그리기 (전체 체력)
        create_health(player.health, HEALTH["bg"], HEALTH["x"], HEALTH["y"], HEALTH["pixel_size"])

        # UI 텍스트 그리기 (남은 체력)
        create_health(player.health_remain, HEALTH["fill"], HEALTH["x"], HEALTH["y"], HEALTH["pixel_size"])

        # 화면 업데이트
        pygame.display.flip()

    # 게임 오버 화면 표시
    if you_died:
        screen.fill(BLACK)
        game_over_font = pygame.font.Font(None, 74)
        game_over_text = game_over_font.render("GAME OVER", True, RED)
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(game_over_text, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000) # 3초간 보여주고 종료

hunt_monsters()

# --- 게임 종료 ---
pygame.quit()
