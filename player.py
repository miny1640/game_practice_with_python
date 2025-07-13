class Player:
    """플레이어 클래스: 레벨, 경험치 등을 관리"""
    def __init__(self):
        self.level = 1
        self.xp = 0
        self.xp_to_next_level = 100

    def gain_xp(self, amount):
        """경험치를 얻고 레벨업을 확인하는 메소드"""
        self.xp += amount
        print(f"{amount} XP 획득! (현재 XP: {self.xp}/{self.xp_to_next_level})")
        self.check_level_up()

    def check_level_up(self):
        """경험치가 충분하면 레벨업하는 메소드"""
        if self.xp >= self.xp_to_next_level:
            self.level += 1
            self.xp -= self.xp_to_next_level
            self.xp_to_next_level = int(self.xp_to_next_level * 1.5) # 다음 레벨업에 필요한 경험치 증가
            print(f"레벨 업! 현재 레벨: {self.level}")
