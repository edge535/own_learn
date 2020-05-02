import pygame, sys

pygame.init()

screen = pygame.display.set_mode((500, 500))

# 加载图片
image1 = pygame.image.load('hero1.png')
image2 = pygame.image.load('hero2.png')

# 获取clock对象
clock = pygame.time.Clock()
count = 0


while True:
    count += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 每秒钟执行次数
    clock.tick(60)

    # 屏幕绘制成白色
    screen.fill(pygame.Color(255, 255, 255))

    if count % 5 == 0:
        # 把iamge对象绘制到屏幕上
        screen.blit(image1, (20, 20))
    else:
        screen.blit(image2, (20, 20))


    # 更新
    pygame.display.flip()