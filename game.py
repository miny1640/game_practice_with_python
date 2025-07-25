import pygame
from block import Block
from player import Player
from monster import Monster
import random
from env import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, BLUE, RED, BLOCKS_COUNT, XP_BAR, HEALTH, MONSTER_HP_BAR
from illustrator import create_pixel_art_rects

# --- 초기 설정 ---
pygame.init()

# 화면 크기
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("몬스터 잡고 레벨업!")

# 폰트 설정
level_font = pygame.font.Font(None, XP_BAR["font_size"])
xp_font = pygame.font.Font(None, XP_BAR["font_size"])
hp_bar_font = pygame.font.Font(None, MONSTER_HP_BAR["font_size"])

# 게임 시간 관련
clock = pygame.time.Clock()

# --- 게임 객체 생성 ---
player = Player() 
monster = Monster()
all_sprites = pygame.sprite.Group(monster) # 몬스터를 그리기 위한 그룹
blocks = pygame.sprite.Group() # 화면에 그리기 및 업데이트를 위한 그룹
block_list = [] # 순서대로 블록을 참조하기 위한 리스트

attack_keys = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]

# 블록 그룹 생성
def create_blocks():
    global block_list
    blocks.empty()
    block_list = []
    for _ in range(BLOCKS_COUNT): 
        add_block_on_tail()

# 꼬리에 블록 추가
def add_block_on_tail():
    block = Block(random.choice(attack_keys), len(block_list))
    blocks.add(block)
    block_list.append(block)

# 꼬리에 블록 추가
def remove_head_block():
    if block_list:
        block_list[0].kill()
        block_list.pop(0)

# UI 텍스트 그리기 (체력)
def create_health(health, color):
    health_pixels = []
    for _ in range(health // HEALTH["full_heart"]):
        health_pixels.append(HEALTH["shapes"][HEALTH["full_heart"]])
    health_pixels.append(HEALTH["shapes"][health % HEALTH["full_heart"]])
        
    x = HEALTH["x"]
    y =  HEALTH["y"]
    pixel_size = HEALTH["pixel_size"]

    for health_pixel in health_pixels:
        for health_rect in create_pixel_art_rects(health_pixel, x, y, pixel_size):
            pygame.draw.rect(screen, color, health_rect)
        x += pixel_size * (HEALTH["tile_count"] + 1)

# 게임 종료 화면
def display_game_over_window(bg_color, text, text_color):
    screen.fill(bg_color)
    game_over_font = pygame.font.Font(None, 74)
    game_over_text = game_over_font.render(text, True, text_color)
    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    screen.blit(game_over_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000) # 3초간 보여주고 종료

# 몬스터 HP 바 그리기
def draw_monster_hp_bar(monster):
    # HP 비율 계산
    ratio = monster.hp / monster.max_hp
    
    # HP 바 배경 및 채우기 Rect 생성
    bg_rect = pygame.Rect(MONSTER_HP_BAR["x"], MONSTER_HP_BAR["y"], MONSTER_HP_BAR["width"], MONSTER_HP_BAR["height"])
    fill_rect = pygame.Rect(MONSTER_HP_BAR["x"], MONSTER_HP_BAR["y"], MONSTER_HP_BAR["width"] * ratio, MONSTER_HP_BAR["height"])

    # HP 바 그리기
    pygame.draw.rect(screen, MONSTER_HP_BAR["bg"], bg_rect)
    pygame.draw.rect(screen, MONSTER_HP_BAR["fill"], fill_rect)

    hp_text = hp_bar_font.render(f"{monster.hp} / {monster.max_hp}", True, MONSTER_HP_BAR["text_color"])
    screen.blit(hp_text, hp_text.get_rect(center=bg_rect.center))

# --- 메인 게임 루프 ---
def hunt_monsters():
    create_blocks() # 게임 시작 시 첫 블록 웨이브 생성
    running = True
    you_died = False
    you_win = False
    while running:
        # 초당 60프레임으로 게임 속도 조절
        clock.tick(60)

        # 이벤트 처리 (키보드, 마우스 등)
        for event in pygame.event.get():
            # 윈도우를 닫거나 ESC를 누르면 종료
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key in attack_keys:
                    effect_font = pygame.font.SysFont("malgungothic", 50)
                    if event.key == block_list[0].key:
                        effect_text = "공격 성공!"
                        monster.take_damage(player.attack_power) # 몬스터 공격

                        # 몬스터가 죽었는지 확인
                        if not monster.is_alive():
                            player.gain_xp(monster.xp_reward) # 경험치 획득
                            monster.respawn(player.level) # 새 몬스터 등장

                        remove_head_block() # 블록 제거
                        for block in blocks:
                            block.move_left() # 블록 위치 재설정
                        add_block_on_tail() # 새로운 블록 추가
                    else:
                        effect_text = "헉, 아푸다!"
                        player.lose_life()
                    screen.blit(effect_font.render(effect_text, True, BLACK), (SCREEN_WIDTH // 2 - 120, 150))
                    pygame.display.flip()
                    pygame.time.wait(50)
                elif event.key == pygame.K_ESCAPE:
                    # ESC 향후 메뉴를 선택할 수 있도록
                    running = False

        # 게임 오버 조건 확인
        if player.health_remain <= 0:
            running = False
            you_died = True
        
        # 게임 승리 조건 확인
        if player.level == 999:
            running = False
            you_win = True

        # --- 화면 그리기 ---
        # 배경색 채우기 (이전 프레임을 지우기 위해 루프 안에 위치)
        screen.fill(WHITE)

        # 몬스터 그리기
        all_sprites.draw(screen)

        # 블록 그룹에 포함된 모든 블록 그리기
        blocks.draw(screen)

        # 경험치 비율 계산 (0.0 ~ 1.0)
        xp_ratio = player.xp / player.xp_to_next_level
        fill_width = int(XP_BAR["rect"]["width"] * xp_ratio)

        # 경험치 바 그리기 (배경 -> 채우기 -> 테두리 순서로 그려야 제대로 보입니다)
        xp_background_rect = pygame.Rect(XP_BAR["rect"]["x"], XP_BAR["rect"]["y"], XP_BAR["rect"]["width"], XP_BAR["rect"]["height"])
        xp_fill_rect = pygame.Rect(XP_BAR["rect"]["x"], XP_BAR["rect"]["y"], fill_width, XP_BAR["rect"]["height"])
        pygame.draw.rect(screen, XP_BAR["bg"], xp_background_rect)
        pygame.draw.rect(screen, XP_BAR["fill"], xp_fill_rect)

        # 레벨과 경험치를 바 위에 표시
        level_text = level_font.render(f"Lv. {player.level}", True, BLACK)
        screen.blit(level_text, level_text.get_rect(midleft=xp_background_rect.midleft))
        xp_text = xp_font.render(f"{(player.xp / player.xp_to_next_level * 100):.2f}%", True, BLACK)
        screen.blit(xp_text, xp_text.get_rect(midright=xp_background_rect.midright))

        # UI 텍스트 그리기 (전체 체력)
        create_health(player.health, HEALTH["bg"])

        # UI 텍스트 그리기 (남은 체력)
        create_health(player.health_remain, HEALTH["fill"])

        # 몬스터 HP 바 그리기
        draw_monster_hp_bar(monster)

        # 화면 업데이트
        pygame.display.flip()

    # 게임 오버 화면 표시
    if you_died:
        display_game_over_window(BLACK, "GAME OVER", RED)
    
    # 게임 승리 화면 표시
    if you_win:
        display_game_over_window(WHITE, "YOU WIN", BLUE)

hunt_monsters()

# --- 게임 종료 ---
pygame.quit()
