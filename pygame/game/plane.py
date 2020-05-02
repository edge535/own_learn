"""
                飞机的基类
我方飞机    敌方飞机    地方的中型飞机     敌方的大型飞机
"""
import pygame

import constants

from game.bullet import Bullet

import random


class Plane(pygame.sprite.Sprite):
    """飞机基类"""
    # 飞机图片
    plane_image = []
    # 飞机爆炸的图片
    destroy_image = []
    # 飞机坠毁的音乐
    down_sound_src = None
    # 飞机的状态 True活的  False死的
    active = True
    # 该飞机发射子弹的精灵组
    bullets = pygame.sprite.Group()

    def __init__(self, screen, speed=None):
        super().__init__()
        self.screen = screen
        self.img_list = []
        self._destroy_img_list = []
        self.down_sound = None
        self.load_src()
        # 飞机的速度
        self.speed = speed or 10
        # 获取飞机的位置
        self.rect = self.img_list[0].get_rect()
        # 游戏窗口的 宽 高
        self.width, self.height = self.screen.get_size()
        # 飞机的 宽 高
        self.plane_w, self.plane_h = self.img_list[0].get_size()
        # 改变飞机的初始化位置
        self.rect.left = int((self.width-self.plane_w) / 2)
        self.rect.top = int(self.height / 2)

    def load_src(self):
        """加载静态资源"""
        for img in self.plane_image:
            self.img_list.append(pygame.image.load(img))
        for img in self.destroy_image:
            self._destroy_img_list.append(pygame.image.load(img))
        if self.down_sound_src:
            self.down_sound = pygame.mixer.Sound(self.down_sound_src)

    @property
    def image(self):
        return self.img_list[0]

    def blit_me(self):
        self.screen.blit(self.image, self.rect)

    def move_up(self):
        """飞机向上移动"""
        self.rect.top -= self.speed

    def move_down(self):
        """飞机向下移动"""
        self.rect.top += self.speed

    def move_left(self):
        """飞机向左移动"""
        self.rect.left -= self.speed

    def move_right(self):
        """飞机向右移动"""
        self.rect.left += self.speed

    def broken_down(self):
        """飞机坠毁"""
        # 坠毁音乐
        if self.down_sound:
            self.down_sound.play(1)
        # 坠毁动画
        for img in self._destroy_img_list:
            self.screen.blit(img, self.rect)
        # 飞机状态为False
        self.active = False

    def shoot(self):
        """ 飞机发射子弹 """
        bullet = Bullet(self.screen, self, 15)
        self.bullets.add(bullet)



class OurPlane(Plane):
    """我方的飞机"""
    # 飞机图片
    plane_image = [constants.OUR_PLANE_IMG_1, constants.OUR_PLANE_IMG_2]
    # 飞机爆炸的图片
    destroy_image = constants.OUR_DESTROY_IMG_LIST
    # 飞机坠毁的音乐
    down_sound_src = None

    def update(self, war):
        self.move(war.key_nextly)
        if war.frame % 5 :
            self.screen.blit(self.img_list[0], self.rect)
        else:
            self.screen.blit(self.img_list[1], self.rect)
        # 飞机的撞击检测
        result = pygame.sprite.spritecollide(self, war.enemies, False)
        if result :
            # 1.游戏结束
            war.status = war.OVER
            # 2.敌方飞机坠毁
            war.enemies.empty()
            war.small_enemies.empty()
            # 3.我方飞机坠毁
            super().broken_down()
            # 4.记录游戏分数

    def move(self, key):
        """飞机移动的自动控制"""
        if key == pygame.K_w or key == pygame.K_UP:
            self.move_up()
        elif key == pygame.K_a or key == pygame.K_LEFT:
            self.move_left()
        elif key == pygame.K_s or key == pygame.K_DOWN:
            self.move_down()
        elif key == pygame.K_d or key == pygame.K_RIGHT:
            self.move_right()

    def move_up(self):
        """向上移动，不允许超出范围"""
        super().move_up()
        if self.rect.top <= 0 :
            self.rect.top = 0

    def move_down(self):
        """向下移动，不允许超出范围"""
        super().move_down()
        if self.rect.bottom >= self.height :
            self.rect.bottom = self.height

    def move_left(self):
        """向左移动，不允许超出范围"""
        super().move_left()
        if self.rect.left <= 0 :
            self.rect.left = 0

    def move_right(self):
        """向右移动，不允许超出范围"""
        super().move_right()
        if self.rect.right >= self.width :
            self.rect.right = self.width


class SmallEnemyPlane(Plane):
    """敌方的小型飞机"""
    plane_image = constants.SMALL_ENEMY_PLANE_IMG_LIST
    destroy_image = constants.SMALL_ENEMY_PLANE_DESTROY_LIST
    down_sound_src = constants.SMALL_ENEMY_PLANE_DESTROY_SOUND

    def __init__(self, screen, speed=None):
        super().__init__(screen, speed)
        self.screen = screen
        self.init_pos()

    def init_pos(self):
        self.rect.left = random.randint(0, self.width - self.plane_w)
        self.rect.top = random.randint(-6 * self.plane_h, 0)

    def update(self, *args):
        """跟新飞机的移动"""
        super().move_down()
        self.blit_me()
        # 超出范围后如何处理
        if self.rect.top >= self.height:
            # self.kill()
            self.reset()

    def reset(self):
        self.active = True
        self.init_pos()

    def broken_down(self):
        super().broken_down()
        self.reset()