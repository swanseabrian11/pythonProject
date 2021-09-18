# 导入需要的模块


import sys
import pygame
# 游戏初始化
pygame.init()

window1 = pygame.display.set_mode((400, 600))
caption = pygame.display.set_caption(("打字游戏"))
bg_color = (255, 0, 0)
window1.fill(bg_color)
# 文字
# txtfont = pygame.font.Font('font\corbel.ttf',40)

txtfont = pygame.font.SysFont("microsoftyaheimicrosoftyaheiui", 40)


pleaseinput = txtfont.render("输入下列内容",True , (0, 255, 0))
window1.blit(pleaseinput, (0, 0))

key_list = pygame.key.get_pressed()

pygame.display.flip()
posx = 0
posy = 200
message_box = []
s1 = ''


# bgc = pygame.display

while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        print( pygame.K_RIGHT)

            # print( key_list[303])
            # running = False

        if event.type == pygame.KEYDOWN:
            print(key_list)
            # message_box.append(chr(event.key))
            # text = s1.join(message_box)
            # if len(text) > 400:
            #  posy += 15
            event_text = txtfont.render(chr(event.key),True , (0, 255, 0))
            # event_text = txtfont.render(text, True, (0, 255, 0))


            # print(message_box)



            window1.blit( event_text, (posx, posy))
            # Textlen = len(text)

            posx = posx+20
            if posx > 400:
                posx = 0
                posy = posy + 50
                message_box = []
            pygame.display.update()






