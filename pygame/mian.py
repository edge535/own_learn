import pygame, sys

import constants

from game.plane import OurPlane, SmallEnemyPlane

from game.war import PlaneWar


def main():
    """游戏入口"""
    # # 初始化
    # pygame.init()
    #
    # # 屏幕对象
    # width, height = 480, 852
    # screen = pygame.display.set_mode((width, height))
    #
    # # 设置窗口标题
    # pygame.display.set_caption('飞机大战')
    #
    # # 加载背景图片
    # bg = pygame.image.load(constants.BG_IMG)
    #
    # # 标题图片
    # img_game_title = pygame.image.load(constants.IMG_GAME_TITLE)
    # img_game_title_rect = img_game_title.get_rect()
    # # t_width, t_height = img_game_title_rect.get_size() # 获取size值
    # img_game_title_rect.topleft = (int((width - img_game_title_rect[2])/2), # X值
    #                                int(height/2 - img_game_title_rect[3]))  # Y值
    #
    # # 开始按钮图片
    # img_game_start_btn = pygame.image.load(constants.IMG_GAME_START_BTN)
    # img_game_start_btn_rect = img_game_start_btn.get_rect()
    # b_width, b_height = img_game_start_btn.get_size() # 获取size值
    # img_game_start_btn_rect.topleft = (int((width - b_width)/2),   # X值
    #                                    int(height / 2 + b_height)  # Y值
    #                                    )
    #
    # # 加载背景音乐
    # pygame.mixer.music.load(constants.BG_MUSIC)
    # pygame.mixer.music.play(-1) # 循环播放
    # pygame.mixer.music.set_volume(0.2) # 设置音量
    #
    # # 游戏状态准备中0， 游戏中1， 游戏结束2
    # status = 0
    #
    # our_plane = OurPlane(screen)
    #
    # frame = 0 # 播放帧数
    #
    # clock = pygame.time.Clock()
    #
    # # 一架飞机可以属于多个精灵组
    # small_enemies = pygame.sprite.Group()
    # enemies = pygame.sprite.Group()
    # # 随机添加几架小型飞机
    # for i in range(6):
    #     plane = SmallEnemyPlane(screen, 5)
    #     plane.add(small_enemies)
    #     plane.add(enemies)
    #
    # while True:
    #     # 设置帧速率
    #     clock.tick(60)
    #     frame += 1
    #     if frame > 60:
    #         frame = 0
    #
    #     # 1 监听事件
    #     for event in pygame.event.get():
    #         # 退出游戏
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         elif event.type == pygame.MOUSEBUTTONDOWN:
    #             # 鼠标点击进入游戏
    #             # 游戏处于准备中，才能进入游戏
    #             if status == 0 :
    #                 status = 1
    #         elif event.type == pygame.KEYDOWN:
    #             # 键盘事件
    #             # 游戏处于游戏中，才需要键盘控制
    #             if status == 1:
    #                 if event.key == pygame.K_w or event.key == pygame.K_UP:
    #                     our_plane.move_up()
    #                 elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
    #                     our_plane.move_left()
    #                 elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
    #                     our_plane.move_down()
    #                 elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
    #                     our_plane.move_right()
    #                 elif event.key == pygame.K_SPACE:
    #                     our_plane.shoot()
    #
    #     if status == 0:
    #         # 绘制背景
    #         screen.blit(bg, bg.get_rect())
    #         # 绘制标题
    #         screen.blit(img_game_title, img_game_title_rect)
    #         # 绘制开始按钮
    #         screen.blit(img_game_start_btn, img_game_start_btn_rect)
    #     elif status == 1:
    #         # 游戏进行中
    #         # 绘制背景
    #         screen.blit(bg, bg.get_rect())
    #         # 绘制飞机
    #         our_plane.update(frame)
    #         # 绘制子弹
    #         our_plane.bullets.update()
    #         # 绘制敌方飞机
    #         small_enemies.update()
    #
    #
    #     # 更新
    #     pygame.display.flip()

    war = PlaneWar()
    war.add_small_enemies(6)
    war.run_game()


if __name__ == '__main__':
    main()