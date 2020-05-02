
import pygame

import sys

import constants

from game.plane import OurPlane, SmallEnemyPlane

from store.result import PlayRset


class PlaneWar(object):
    """飞机大战"""
    # 游戏状态准备中0， 游戏中1， 游戏结束2
    status = 0

    READY = 0
    PLAYING = 1
    OVER = 2

    our_plane = None

    frame = 0  # 播放帧数

    clock = pygame.time.Clock()

    # 一架飞机可以属于多个精灵组
    small_enemies = pygame.sprite.Group()
    enemies = pygame.sprite.Group()

    # 游戏结果
    rest = PlayRset()


    def __init__(self):
        # 初始化游戏
        pygame.init()

        self.width, self.height = 480, 852
        self.screen = pygame.display.set_mode((self.width, self.height))

        # 设置窗口标题
        pygame.display.set_caption('飞机大战')

        # 加载背景图片
        self.bg = pygame.image.load(constants.BG_IMG)
        self.bg_over = pygame.image.load(constants.BG_IMG_OVER)

        # 标题图片
        self.img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
        self.img_game_title_rect = self.img_game_title.get_rect()
        # t_width, t_height = img_game_title_rect.get_size() # 获取size值
        self.img_game_title_rect.topleft = (int((self.width - self.img_game_title_rect[2]) / 2),  # X值
                                       int(self.height / 2 - self.img_game_title_rect[3]))  # Y值

        # 开始按钮图片
        self.img_game_start_btn = pygame.image.load(constants.IMG_GAME_START_BTN)
        self.img_game_start_btn_rect = self.img_game_start_btn.get_rect()
        self.b_width, self. b_height = self.img_game_start_btn.get_size()  # 获取size值
        self.img_game_start_btn_rect.topleft = (int((self.width - self.b_width) / 2),  # X值
                                           int(self.height / 2 + self.b_height)  # Y值
                                           )

        # 游戏文字对象
        self.score_font = pygame.font.SysFont('华文新魏', 32)


        # 加载背景音乐
        pygame.mixer.music.load(constants.BG_MUSIC)
        pygame.mixer.music.play(-1)  # 循环播放
        pygame.mixer.music.set_volume(0.2)  # 设置音量

        #我方飞机对象
        self.our_plane = our_plane = OurPlane(self.screen, 3)

        self.clock = pygame.time.Clock()

        # 上次按的键盘上的某一个键，用于连续控制飞机
        self.key_nextly = None


    def bind_evnet(self):
        """绑定事件"""
        # 1 监听事件
        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 鼠标点击进入游戏
                # 游戏处于准备中，才能进入游戏
                if self.status == self.READY:
                    self.status = self.PLAYING
                elif self.status == self.OVER: # 结束后点击重新开始
                    self.status = self.READY
                    self.add_small_enemies(6)
            elif event.type == pygame.KEYDOWN:
                # 键盘事件
                # 游戏处于游戏中，才需要键盘控制
                self.key_nextly = event.key
                if self.status == self.PLAYING:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.our_plane.move_up()
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.our_plane.move_left()
                    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.our_plane.move_down()
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.our_plane.move_right()
                    elif event.key == pygame.K_SPACE:
                        self.our_plane.shoot()

    def add_small_enemies(self, num):
        """随机添加几架小型飞机"""
        for i in range(num):
            plane = SmallEnemyPlane(self.screen, 4)
            plane.add(self.small_enemies, self.enemies)

    def run_game(self):
        """游戏主循环部分"""
        while True:
            # 设置帧速率
            self.clock.tick(60)
            self.frame += 1
            if self.frame > 60:
                self.frame = 0

            # 绑定事件
            self.bind_evnet()


            # 状态更新
            if self.status == self.READY:
                # 绘制背景
                self.screen.blit(self.bg, self.bg.get_rect())
                # 绘制标题
                self.screen.blit(self.img_game_title, self.img_game_title_rect)
                # 绘制开始按钮
                self.screen.blit(self.img_game_start_btn, self.img_game_start_btn_rect)
                self.key_nextly = None
            elif self.status == self.PLAYING:
                # 游戏进行中
                # 绘制背景
                self.screen.blit(self.bg, self.bg.get_rect())
                # 绘制飞机
                self.our_plane.update(self)
                # 绘制子弹
                self.our_plane.bullets.update(self)
                # 绘制敌方飞机
                self.small_enemies.update()
                # 游戏分数
                score_text = self.score_font.render('得分{}'.format(self.rest.score), False, constants.TEXT_COLOR)
                self.screen.blit(score_text, score_text.get_rect())
            elif self.status == self.OVER:
                # 结束后背景
                self.screen.blit(self.bg_over, self.bg_over.get_rect())
                score_text = self.score_font.render('{}'.format(self.rest.score), False, constants.TEXT_COLOR)
                score_text_rect = score_text.get_rect()
                text_w, text_h = score_text.get_size()
                # 改变文字的位置
                score_text_rect.topleft = (
                    int((self.width - text_w) / 2),
                    int(self.height / 2)
                )
                self.screen.blit(score_text, score_text_rect)
                # 历史最高分
                score_his = self.score_font.render('{}'.format(self.rest.get_max_core()), False, constants.TEXT_COLOR)
                self.screen.blit(score_his, (150, 40))


            # 更新
            pygame.display.flip()