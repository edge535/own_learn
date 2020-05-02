import pygame, sys

pygame.init()

screen = pygame.display.set_mode((500, 500))

# 加载全部字体
fonts = pygame.font.get_fonts()
#print(front)

red = pygame.Color(255, 0, 0)

# 加粗，斜体
# 使用系统默认的字体文件
font = pygame.font.SysFont('华文新魏', 40, True, True)
# 使用项目中字体
# font = gygame.font.Font('')


# 文字对象
text = font.render("得分", False, red)
text2 = font.render("TEST", False, red)


# 音乐
bg_music = pygame.mixer.music.load('/pygame/a_demo\\game_bg_music.mp3')
pygame.mixer.music.play(-1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # 绘制图形
    screen.blit(text, (20, 20))
    screen.blit(text2, (120, 120))
    # 更新
    pygame.display.flip()