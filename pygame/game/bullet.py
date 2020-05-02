import pygame

import constants




class Bullet(pygame.sprite.Sprite):
    """子弹类"""

    # 子弹状态
    active = True

    def __init__(self, screen, plane, speed=None):
        super().__init__()
        self.screen = screen
        # 速度
        self.speed = speed or 10
        self.plane = plane
        self.image = pygame.image.load(constants.BULLET_IMG)
        # 改变子弹的位置
        self.rect = self.image.get_rect()
        self.rect.centerx = plane.rect.centerx
        self.rect.top = plane.rect.top
        # 发射的音乐
        self.shoot_sound = pygame.mixer.Sound(constants.BULLET_SOUND)
        self.shoot_sound.set_volume(0.3)
        self.shoot_sound.play()

    def update(self, war):
        """跟新子弹的位置"""
        self.rect.top -= self.speed
        if self.rect.top < 0:
            self.remove(self.plane.bullets)
        self.screen.blit(self.image, self.rect)
        # 碰撞检测，检测子弹是否已经碰撞到了敌机
        result = pygame.sprite.spritecollide(self, war.enemies, False)
        print('result:', result)
        for r in result:
            # 1.子弹消失
            self.kill()
            # 2.飞机消失
            r.broken_down()
            # 3.统计游戏成绩
            war.rest.score += 10
            # 保存历史记录
            war.rest.set_history()