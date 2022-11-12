#Connect5
import pygame
from bilgiler import *
from with_classes2 import *


game=Connect4(7,6,4)

pygame.init()
ekrbyt=(genislik,uzunluk)
ekr=pygame.display.set_mode(ekrbyt)
pygame.display.set_caption("Connect 4")


font=pygame.font.SysFont("Corbel",40)

CIK_yazi=font.render("Cik",True,siyah)
CIK2_yazi=font.render("Cik",True,siyah)
BASLIK_yazi=font.render("CONNECT 4",True,siyah)
OYNA_yazi=font.render("Oyna",True,siyah)
BILGI_yazi=font.render("i",True,siyah)
HAKKINDA_yazi=font.render("Author=Kerem_Ali",True,(255,255,255))

yer="Menu"

quite=False
while not quite:
    if yer=="Menu":
        platform=game.platform
        sira="A"
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quite=True
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if (BUTON_OYNA_STARTX<=mouse[0] <=BUTON_OYNA_STARTX+BUTON_OYNA_GENISLIK) and(BUTON_OYNA_STARTY<=mouse[1] <=BUTON_OYNA_STARTY+BUTON_OYNA_UZUNLUK):
                    #quite=True
                    print("Oyna Basıldı")
                    yer="Oyna"
                elif (BUTON_CIK_STARTX<=mouse[0] <=BUTON_CIK_STARTX+BUTON_CIK_GENISLIK) and(BUTON_CIK_STARTY<=mouse[1] <=BUTON_CIK_STARTY+BUTON_CIK_UZUNLUK):
                    quite=True
                    print("Cik Basıldı")
                elif (BUTON_BILGI_STARTX<=mouse[0] <=BUTON_BILGI_STARTX+BUTON_CIK_GENISLIK) and(BUTON_BILGI_STARTY<=mouse[1] <=BUTON_BILGI_STARTY+BUTON_BILGI_UZUNLUK):
                    #quite=True
                    print("Bilgi Basıldı")
                    yer="Bilgi"

        mouse=pygame.mouse.get_pos()
        ekr.fill(renk)
        if (BUTON_OYNA_STARTX<=mouse[0] <=BUTON_OYNA_STARTX+BUTON_OYNA_GENISLIK) and(BUTON_OYNA_STARTY<=mouse[1] <=BUTON_OYNA_STARTY+BUTON_OYNA_UZUNLUK):
            pygame.draw.rect(ekr,mavi,[BUTON_OYNA_STARTX,BUTON_OYNA_STARTY,BUTON_OYNA_GENISLIK,BUTON_OYNA_UZUNLUK])
        else:
            pygame.draw.rect(ekr,koyu_mavi,[BUTON_OYNA_STARTX,BUTON_OYNA_STARTY,BUTON_OYNA_GENISLIK,BUTON_OYNA_UZUNLUK])


        if (BUTON_CIK_STARTX<=mouse[0] <=BUTON_CIK_STARTX+BUTON_CIK_GENISLIK) and(BUTON_CIK_STARTY<=mouse[1] <=BUTON_CIK_STARTY+BUTON_CIK_UZUNLUK):
            pygame.draw.rect(ekr,mavi,[BUTON_CIK_STARTX,BUTON_CIK_STARTY,BUTON_CIK_GENISLIK,BUTON_CIK_UZUNLUK])
        else:
            pygame.draw.rect(ekr,koyu_mavi,[BUTON_CIK_STARTX,BUTON_CIK_STARTY,BUTON_CIK_GENISLIK,BUTON_CIK_UZUNLUK])


        if (BUTON_BILGI_STARTX<=mouse[0] <=BUTON_BILGI_STARTX+BUTON_BILGI_GENISLIK) and(BUTON_BILGI_STARTY<=mouse[1] <=BUTON_BILGI_STARTY+BUTON_BILGI_UZUNLUK):
            pygame.draw.rect(ekr,mavi,[BUTON_BILGI_STARTX,BUTON_BILGI_STARTY,BUTON_BILGI_GENISLIK,BUTON_BILGI_UZUNLUK],0,10)
        else:
            pygame.draw.rect(ekr,koyu_mavi,[BUTON_BILGI_STARTX,BUTON_BILGI_STARTY,BUTON_BILGI_GENISLIK,BUTON_BILGI_UZUNLUK],0,10)

        ekr.blit(OYNA_yazi , (BUTON_OYNA_STARTX+45,BUTON_OYNA_STARTY+15))
        ekr.blit(BASLIK_yazi , (LABEL_BASLIK_STARTX,LABEL_BASLIK_STARTY))
        ekr.blit(CIK_yazi , (BUTON_CIK_STARTX+45,BUTON_CIK_STARTY+15))
        ekr.blit(BILGI_yazi , (BUTON_BILGI_STARTX+20,BUTON_BILGI_STARTY+15))
        

        pygame.display.update()
    if yer=="Oyna":
        
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quite=True
            elif event.type==pygame.MOUSEBUTTONDOWN:
                
                mouse=pygame.mouse.get_pos()
                x=mouse[0]
                y=mouse[1]
                print(x,y)
                col=(x-box_kaydirma)//(box_genislik+box_bosluk)
                row=(y-box_kaydirma) // (box_uzunluk +box_bosluk)
                if 0<col<game.col+1 and -1<row<game.col:
                    if not game.check_full(col):
                        game.play(col)
                        #game.platform_goster()
                        game.sira_degistir()
                elif (BUTON_CIK2_STARTX<=mouse[0] <=BUTON_CIK2_STARTX+BUTON_CIK2_GENISLIK) and(BUTON_CIK2_STARTY<=mouse[1] <=BUTON_CIK2_STARTY+BUTON_CIK2_UZUNLUK):
                    print("Cik Basıldı")
                    yer="Menu"


        mouse=pygame.mouse.get_pos()
        ekr.fill(brenk)
        if (BUTON_CIK2_STARTX<=mouse[0] <=BUTON_CIK2_STARTX+BUTON_CIK2_GENISLIK) and(BUTON_CIK2_STARTY<=mouse[1] <=BUTON_CIK2_STARTY+BUTON_CIK2_UZUNLUK):
            pygame.draw.rect(ekr,mavi,[BUTON_CIK2_STARTX,BUTON_CIK2_STARTY,BUTON_CIK2_GENISLIK,BUTON_CIK2_UZUNLUK])
        else:
            pygame.draw.rect(ekr,koyu_mavi,[BUTON_CIK2_STARTX,BUTON_CIK2_STARTY,BUTON_CIK2_GENISLIK,BUTON_CIK2_UZUNLUK])


        for sir in range(game.row):
            for sutun in range(1,game.col+1):
                pygame.draw.rect(ekr,
                                 (60,60,100),
                                 [(box_bosluk + box_genislik) * sutun+ box_bosluk+box_kaydirma,
                                  (box_bosluk + box_uzunluk) * sir + box_bosluk+box_kaydirma,
                                  box_genislik,
                                  box_uzunluk])
                if platform[sutun][sir]==0:
                    color=siyah
                elif platform[sutun][sir]=="A":
                    color=(250,25,15)
                elif platform[sutun][sir]=="B":
                    color=(15,25,250)

                pygame.draw.circle(ekr, color, ((box_bosluk + box_genislik) * sutun+ box_bosluk+box_kaydirma+22.5,
                                                (box_bosluk + box_uzunluk) * sir + box_bosluk+box_kaydirma+22.5),
                                   20, 0)


        ekr.blit(CIK2_yazi , (BUTON_CIK2_STARTX+15,BUTON_CIK2_STARTY+5))

        pygame.display.update()
        
        if game.check_win():
            print("Winner is ",game.check_win())
            print("tebrikler")
            game.reset()
            yer="Menu"
            

    if yer=="Bilgi":
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quite=True
                yer=None
            elif event.type==pygame.MOUSEBUTTONDOWN:
                if (BUTON_CIK2_STARTX<=mouse[0] <=BUTON_CIK2_STARTX+BUTON_CIK2_GENISLIK) and(BUTON_CIK2_STARTY<=mouse[1] <=BUTON_CIK2_STARTY+BUTON_CIK2_UZUNLUK):
                        print("Cik Basıldı")
                        game.reset()
                        yer="Menu"


        ekr.fill((75,100,255))
        mouse=pygame.mouse.get_pos()
        if (BUTON_CIK2_STARTX<=mouse[0] <=BUTON_CIK2_STARTX+BUTON_CIK2_GENISLIK) and(BUTON_CIK2_STARTY<=mouse[1] <=BUTON_CIK2_STARTY+BUTON_CIK2_UZUNLUK):
            pygame.draw.rect(ekr,brenk,[BUTON_CIK2_STARTX,BUTON_CIK2_STARTY,BUTON_CIK2_GENISLIK,BUTON_CIK2_UZUNLUK])
        else:
            pygame.draw.rect(ekr,koyu_mavi,[BUTON_CIK2_STARTX,BUTON_CIK2_STARTY,BUTON_CIK2_GENISLIK,BUTON_CIK2_UZUNLUK])

        ekr.blit(HAKKINDA_yazi,(LABEL_HAKKINDA_STARTX,LABEL_HAKKINDA_STARTY))
        ekr.blit(CIK2_yazi , (BUTON_CIK2_STARTX+15,BUTON_CIK2_STARTY+5))

        pygame.display.update()


pygame.quit()
