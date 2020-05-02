import pygame, sys

pygame.init()


screen = pygame.display.set_mode((500, 500))


# 加载字体
# ['arial', 'arialblack', 'bahnschrift', 'calibri',
# 'cambriacambriamath', 'cambria', 'candara',
# 'comicsansms', 'consolas', 'constantia', 'corbel',
# 'couriernew', 'ebrima', 'franklingothicmedium',
#  'gabriola', 'gadugi', 'georgia', 'impact',
# 'inkfree', 'javanesetext', 'leelawadeeui',
# 'leelawadeeuisemilight', 'lucidaconsole',
# 'lucidasans', 'malgungothic', 'malgungothicsemilight',
# 'microsofthimalaya', 'microsoftjhengheimicrosoftjhengheiui',
# 'microsoftjhengheimicrosoftjhengheiuibold',
# 'microsoftjhengheimicrosoftjhengheiuilight',
# 'microsoftnewtailue', 'microsoftphagspa',
# 'microsoftsansserif', 'microsofttaile',
# 'microsoftyaheimicrosoftyaheiui',
# 'microsoftyaheimicrosoftyaheiuibold',
# 'microsoftyaheimicrosoftyaheiuilight', 'microsoftyibaiti', 'mingliuextbpmingliuextbmingliuhkscsextb', 'mongolianbaiti', 'msgothicmsuigothicmspgothic', 'mvboli', 'myanmartext', 'nirmalaui', 'nirmalauisemilight', 'palatinolinotype', 'segoemdl2assets', 'segoeprint', 'segoescript', 'segoeui', 'segoeuiblack', 'segoeuiemoji', 'segoeuihistoric', 'segoeuisemibold', 'segoeuisemilight', 'segoeuisymbol', 'simsunnsimsun', 'simsunextb', 'sitkasmallsitkatextsitkasubheadingsitkaheadingsitkadisplaysitkabanner', 'sitkasmallsitkatextboldsitkasubheadingboldsitkaheadingboldsitkadisplayboldsitkabannerbold', 'sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic', 'sitkasmallsitkatextitalicsitkasubheadingitalicsitkaheadingitalicsitkadisplayitalicsitkabanneritalic', 'sylfaen', 'symbol', 'tahoma', 'timesnewroman', 'trebuchetms', 'verdana', 'webdings', 'wingdings', 'yugothicyugothicuisemiboldyugothicuibold', 'yugothicyugothicuilight', 'yugothicmediumyugothicuiregular', 'yugothicregularyugothicuisemilight', 'dengxian', 'fangsong', 'kaiti', 'simhei', 'holomdl2assets', 'meiryomeiryomeiryouimeiryouiitalic', 'meiryomeiryoboldmeiryouiboldmeiryouibolditalic', 'msminchomspmincho', 'uddigikyokashonbuddigikyokashonpbuddigikyokashonkb', 'uddigikyokashonruddigikyokashonpruddigikyokashonkr', 'yumincho', 'bookantiqua', 'bookmanoldstyle', 'bradleyhanditc', 'bookshelfsymbol7', 'century', 'freestylescript', 'frenchscript', 'garamond', 'centurygothic', 'kristenitc', 'juiceitc', 'lucidahandwriting', 'mistral', 'monotypecorsiva', 'papyrus', 'pristina', 'msreferencesansserif', 'msreferencespecialty', 'tempussansitc', 'wingdings2', 'wingdings3', '方正舒体', '方正姚体', '隶书', '幼圆', '华文彩云', '华文仿宋', '华文琥珀', '华文楷体', '华文隶书', '华文宋体', '华文细黑', '华文行楷', '华文新魏', '华文中宋', 'extra', 'teamviewer13', 'ocraextended', 'dejavusansmonooblique', 'dejavusansmono', 'momoxinjian', '草檀斋毛泽东字体', 'axurehandwritingbold', 'axurehandwritingbolditalic', 'axurehandwritingitalic', 'axurehandwriting', 'icomoon']
fonts = pygame.font.get_fonts()
print(fonts)

red = pygame.Color(255, 0, 0)

# 加粗 斜体
# font = pygame.font.SysFont('华文新魏', 40, False, False)
font = pygame.font.Font('./simhei.ttf', 40)
# 文字对象
text = font.render('得分', True, red)


# 加载音乐
bg_music = pygame.mixer.music.load('./static/bg_music.mp3')
# 设置音量大小（0-1），值越小，音量越小
pygame.mixer.music.set_volume(0.2)
# 循环播放背景音乐
pygame.mixer.music.play(-1)

while True:
    print(111)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(text, (20, 20))
    pygame.display.flip()