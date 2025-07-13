import pygame
from monster import Monster
from player import Player
from env import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK

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
monsters = pygame.sprite.Group()

# 몬스터 그룹 생성
def create_monsters():
    for _ in range(10): # 10마리의 몬스터 생성
        monster = Monster()
        monsters.add(monster)

# --- 메인 게임 루프 ---
def hunt_monsters():
    running = True
    while running:
        # 초당 60프레임으로 게임 속도 조절
        clock.tick(60)

        if len(monsters) == 0:
            create_monsters()

        # 이벤트 처리 (키보드, 마우스 등)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # ESC 키를 누르면 게임 종료
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            # 마우스 클릭 이벤트 처리
            if event.type == pygame.MOUSEBUTTONDOWN:
                # 클릭된 몬스터를 찾아 처리
                for monster in monsters:
                    if monster.rect.collidepoint(event.pos):
                        print("몬스터 처치!")
                        player.gain_xp(25) # 몬스터를 잡으면 25 XP 획득
                        monster.kill() # 몬스터를 모든 그룹에서 제거
                        break # 한 번의 클릭으로 여러 몬스터가 죽지 않도록

        # --- 화면 그리기 ---
        # 배경색 채우기
        screen.fill(WHITE)

        # 몬스터 그룹에 포함된 모든 몬스터 그리기
        monsters.draw(screen)

        # UI 텍스트 그리기 (레벨, 경험치)
        level_text = font.render(f"Level: {player.level}", True, BLACK)
        xp_text = font.render(f"XP: {player.xp} / {player.xp_to_next_level}", True, BLACK)
        screen.blit(level_text, (10, 10))
        screen.blit(xp_text, (10, 50))

        # 화면 업데이트
        pygame.display.flip()

hunt_monsters()

# --- 게임 종료 ---
pygame.quit()
