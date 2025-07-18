import pygame
from block import Block
from player import Player
import random
from env import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, BLOCKS_COUNT, RED

# --- 초기 설정 ---
pygame.init()

# 화면 크기
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("몬스터 잡고 레벨업!")

# 폰트 설정
font = pygame.font.Font(None, 40)

# 게임 시간 관련
clock = pygame.time.Clock()

# --- 게임 객체 생성 ---
player = Player() 
blocks = pygame.sprite.Group() # 화면에 그리기 및 업데이트를 위한 그룹
block_list = [] # 순서대로 블록을 참조하기 위한 리스트

attack_keys = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r]

# 몬스터 그룹 생성
def create_blocks():
    global block_list
    blocks.empty()
    block_list = []
    for idx in range(BLOCKS_COUNT): 
        block = Block(random.choice(attack_keys), idx)
        blocks.add(block)
        block_list.append(block)

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
                    if event.key == block_list[idx].key:
                        print("블록 처치!")
                        player.gain_xp(25) # 블록을 잡으면 25 XP 획득
                        block_list[idx].kill() # 블록을 그룹에서 제거 (화면에서 사라짐)
                        idx += 1
                    else:
                        print("헉 아푸다!")
                        player.lose_life()

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

        # UI 텍스트 그리기 (레벨, 경험치, 체력)
        level_text = font.render(f"Level: {player.level}", True, BLACK)
        xp_text = font.render(f"XP: {player.xp} / {player.xp_to_next_level}", True, BLACK)
        health_text = font.render(f"Health: {player.health_remain} / {player.health}", True, BLACK)
        screen.blit(level_text, (10, 10))
        screen.blit(xp_text, (10, 50))
        screen.blit(health_text, (10, 90))

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
