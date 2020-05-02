import os



import pygame


# 项目的根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# print(BASE_DIR)

# 静态文件的目录
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
# print(ASSETS_DIR)

# 背景图片
BG_IMG = os.path.join(ASSETS_DIR, 'images/background.png')
BG_IMG_READY = os.path.join(ASSETS_DIR, 'images/background.png')
BG_IMG_OVER = os.path.join(ASSETS_DIR, 'images/game_over.png')

# 标题图片
IMG_GAME_TITLE = os.path.join(ASSETS_DIR, 'images/game_title.png')

# 开始游戏的按钮
IMG_GAME_START_BTN = os.path.join(ASSETS_DIR, 'images/game_start.png')

# 背景音乐
BG_MUSIC = os.path.join(ASSETS_DIR, 'sound/game_bg_music.mp3')

# 游戏分数颜色
TEXT_COLOR = pygame.Color(249, 149, 125)

# 我方飞机静态资源
OUR_PLANE_IMG_1 = os.path.join(ASSETS_DIR, 'images/hero1.png')
OUR_PLANE_IMG_2 = os.path.join(ASSETS_DIR, 'images/hero2.png')
OUR_DESTROY_IMG_LIST = [
    os.path.join(ASSETS_DIR, 'images/hero_broken_n1.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n2.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n3.png'),
    os.path.join(ASSETS_DIR, 'images/hero_broken_n4.png')
]
# OUR_DESTROY_IMG_1 = os.path.join(ASSETS_DIR, 'images/hero_broken_n1.png')
# OUR_DESTROY_IMG_2 = os.path.join(ASSETS_DIR, 'images/hero_broken_n2.png')
# OUR_DESTROY_IMG_3 = os.path.join(ASSETS_DIR, 'images/hero_broken_n3.png')
# OUR_DESTROY_IMG_4 = os.path.join(ASSETS_DIR, 'images/hero_broken_n4.png')


# 子弹的图片
BULLET_IMG = os.path.join(ASSETS_DIR, 'images/bullet1.png')

# 子弹的音乐
BULLET_SOUND = os.path.join(ASSETS_DIR, 'sound/bullet.wav')


# 敌方小型飞机资源
SMALL_ENEMY_PLANE_IMG_LIST = [os.path.join(ASSETS_DIR, 'images/enemy1.png')]
SMALL_ENEMY_PLANE_DESTROY_LIST = [
    os.path.join(ASSETS_DIR, 'images/enemy1_down1.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down2.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down3.png'),
    os.path.join(ASSETS_DIR, 'images/enemy1_down4.png')
]
SMALL_ENEMY_PLANE_DESTROY_SOUND = os.path.join(ASSETS_DIR, 'sound/enemy1_down.wav')

# 游戏结果存储的文件地址
PLAY_RESULT_FILE = os.path.join(BASE_DIR, 'store/rest.txt')