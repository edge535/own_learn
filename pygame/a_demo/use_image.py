import sys, pygame

# 初始化
pygame.init()

# 屏幕对象
screen = pygame.display.set_mode((500, 500))

# 加载图片
ball = pygame.image.load('intro_ball.gif')

# 红色
red = pygame.Color(255, 0, 0)



# 游戏主循环
while True:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #退出
            pygame.quit()
            sys.exit()

    # 画线
    pygame.draw.line(screen, red, (1, 1), (50, 50), 6)

    # 画矩形
    pygame.draw.rect(screen, red, (20, 20, 200, 200), 10)

    # 画圆形
    pygame.draw.circle(screen, red, (50, 50), 100, 2)


    # 绘制图形
    screen.blit(ball, (100, 100))

    pygame.display.flip()