import sys

import pygame.time
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from buttons import *
import time

import re
from pprint import pprint
from nltk.tokenize import regexp_tokenize


pygame.init()

class GUI_Interface:
    def __init__(self):

        self.Totaltime = 0
        self.screen = pygame.display.set_mode((1820, 980))
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = 'main menu'
        self.algorithm_state = ''
        self.load()
        self.Digits = set("0 1 2 3 4 5 6 7 8 9 ".split())
        self.FirstSymbolID = set("A B C D F G H J K L M N O P Q R S U V W X Y Z a b c d f g h j k l m n o p q r s u v w x y z".split())
        self.SecondSymbolPlusID = set ("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9".split())
        self.SecondSymbolPlusID2 = set("A B C D E F G H I J K M O P Q R S T U V W X Y Z a b c d e f g h i j k m o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9".split()) ## without N n L l
        self.SecondSymbolPlusIdDigitless = set("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z = : - ;".split())
        self.SecondSymbolPlusIDNOTIF = set("A B C D E G H I J K L M N O P Q R S T U V W X Y Z a b c d e g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9".split())
        self.SecondSymbolPlusIDNOTTHEN = set("A B C D F G I J K L M O P Q R S U V W X Y Z a b c d f g i j k l m o p q r s u v w x y z 0 1 2 3 4 5 6 7 8 9".split())
        self.SecondSymbolPlusIDAllCharacters = set ("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9 = : - ; .".split())

        self.FirstSymbolIF = set("I i".split())
        self.SecondSymbolIF = set("F f".split())

        self.FirstSymbolTHEN = set("T t".split())
        self.SecondSymbolTHEN = set("H h".split())
        self.ThirdSymbolTHEN = set("E e".split())
        self.FourthSymbolTHEN = set("N n".split())

        self.FirstSymbolElse_End = set("E e".split())

        self.SecondSymbolELSE = set("L l".split())
        self.ThirdSymbolELSE = set("S s".split())
        self.FourthSymbolELSE = set("E e".split())

        self.SecondSymbolEND = set("N n".split())
        self.ThirdSymbolEND = set("D d".split())

        self.CharactersPostID = set (". = : - ;".split())

        self.FirstSymbolDotEqual = set (":".split())
        self.SecondSymbolDotEqual = set("=".split())

        self.Semicolon = set(";".split())

        self.Dot = set(".".split())

        self.Sentence = ""
        self.list = ""






 # Define Main-Menu buttons
        self.UploadTextFile_button = Buttons(self, TURQUOISE, 100, 750, 400, MAIN_BUTTON_HEIGHT, 'Upload A Text File')
        self.Tockenize_button = Buttons(self, TURQUOISE, 100, 850, 400, MAIN_BUTTON_HEIGHT, 'Scan & Tockenize Text')
        self.Visualize_button = Buttons(self, TURQUOISE, 100, 650, 400, MAIN_BUTTON_HEIGHT, 'Visualize')

    def run(self):
        while self.running:
            if self.state == 'main menu':
                self.main_menu_events()
            if self.state == 'start visualizing':
                self.execute_algorithm()
            if self.state == 'start uploading':
                self.execute_algorithm()
            if self.state == 'start Tockenizing':
                self.execute_algorithm()




        pygame.quit()
        sys.exit()

##### Loading Images
    def load(self):
        self.main_menu_background = pygame.image.load('main_background2.png')
        self.grid_background = pygame.image.load('grid_logo.png')

##### Draw Text
    def draw_text(self, words, screen, pos, size, colour, font_name, centered=False):
        font = pygame.font.SysFont(font_name, size)
        text = font.render(words, False, colour)
        text_size = text.get_size()
        if centered:
            pos[0] = pos[0] - text_size[0] // 2
            pos[1] = pos[1] - text_size[1] // 2
        screen.blit(text, pos)

##### Setup for Main Menu
    def sketch_main_menu(self):
        self.screen.blit(self.main_menu_background, (0, 0))

        pygame.draw.circle(self.screen, BLACK, (880,605), 45, 7)          ## is Assign
        pygame.draw.circle(self.screen, BLACK, (920, 450), 45, 7)         ## Start
        pygame.draw.circle(self.screen, BLACK, (610, 512), 45, 7)         ## Dead Left
        pygame.draw.circle(self.screen, BLACK, (690, 385), 45, 7)         ## is IF
        pygame.draw.circle(self.screen, BLACK, (880, 747), 45, 7)         ## ASSIGN
        pygame.draw.circle(self.screen, BLACK, (537, 384), 45, 7)         ## IF
        pygame.draw.circle(self.screen, BLACK, (1012, 605), 45, 7)        ## Dead center
        pygame.draw.circle(self.screen, BLACK, (1085, 835), 45, 7)        ## is float
        pygame.draw.circle(self.screen, BLACK, (387, 583), 45, 7)         ## is Then 1
        pygame.draw.circle(self.screen, BLACK, (290, 257), 45, 7)         ## Then
        pygame.draw.circle(self.screen, BLACK, (288, 495), 45, 7)         ## is then 2
        pygame.draw.circle(self.screen, BLACK, (251, 370), 45, 7)         ## is then 3
        pygame.draw.circle(self.screen, BLACK, (1248, 373), 45, 7)        ## is else 1
        pygame.draw.circle(self.screen, BLACK, (1375, 373), 45, 7)        ## is else 2
        pygame.draw.circle(self.screen, BLACK, (1503, 372), 45, 7)        ## else
        pygame.draw.circle(self.screen, BLACK, (1500, 499), 45, 7)        ## Dead Right
        pygame.draw.circle(self.screen, BLACK, (1599, 585), 45, 7)        ## is end
        pygame.draw.circle(self.screen, BLACK, (1727, 585), 45, 7)        ## end
        pygame.draw.circle(self.screen, BLACK, (1320, 726), 45, 7)        ## semicolon
        pygame.draw.circle(self.screen, BLACK, (1190, 726), 45, 7)        ## NUM
        pygame.draw.circle(self.screen, BLACK, (1155, 452), 45, 7)        ## is else or end
        pygame.draw.circle(self.screen, BLACK, (920, 165), 80, 7)         ## ID


        # Draw Buttons
        self.UploadTextFile_button.draw_button(TURQUOISE)
        self.Tockenize_button.draw_button(TURQUOISE)
        self.Visualize_button.draw_button(TURQUOISE)







    #def StateTransition(self):


##### MAIN MENU FUNCTIONS

    def main_menu_events(self):
        # Draw Background
        pygame.display.update()
        self.sketch_main_menu()


        # Check if game is running
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            pos = pygame.mouse.get_pos()
            # Get mouse position and check if it is clicking button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.UploadTextFile_button.isOver(pos):
                    self.algorithm_state = 'Upload'
                    self.state = 'start uploading'
                if self.Tockenize_button.isOver(pos):
                    self.algorithm_state = 'Tockenize'
                    self.state = 'start Tockenizing'
                if self.Visualize_button.isOver(pos):
                    self.algorithm_state = 'Visualize'
                    self.state = 'start visualizing'




            # Get mouse position and check if it is hovering over button
            if event.type == pygame.MOUSEMOTION:
                if self.UploadTextFile_button.isOver(pos):
                    self.UploadTextFile_button.colour = TURQUOISE
                elif self.Tockenize_button.isOver(pos):
                    self.Tockenize_button.colour = TURQUOISE
                elif self.Visualize_button.isOver(pos):
                    self.Visualize_button.colour = TURQUOISE
                else:
                    self.UploadTextFile_button.colour, self.Tockenize_button.colour, self.Visualize_button.colour = WHITE, WHITE, WHITE






    def execute_algorithm(self):

        self.Totaltime = 0

        for event in pygame.event.get():

            self.clock.tick()
            if event.type == pygame.QUIT:
                self.running = False




        if self.algorithm_state == 'Visualize':



         for Incrementor in range(0, len(self.list)):

            Token1 = self.list[Incrementor]

            flag = 1
            pygame.draw.circle(self.screen, SPRINGGREEN, (920, 450), 45, 7)  ## Start
            pygame.display.update()
            pygame.event.pump()
            pygame.time.delay(2000)

            if any(char1 in self.FirstSymbolID for char1 in Token1[0]) and flag ==1:


                pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                pygame.display.update()
                pygame.event.pump()
                pygame.time.delay(2000)
                for counter1 in range(0, len(Token1)-1):

                    i = counter1 + 1



                    if any(char1 in self.SecondSymbolPlusID for char1 in Token1[i]) and flag ==1:
                        if i < len(Token1) - 1:
                            i += 1
                        else:
                            flag = 0

                        pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        print('ID route 1')

                    elif any(char1 in self.CharactersPostID for char1 in Token1[i]) and flag == 1:

                        if i < len(Token1) - 1:
                            i += 1
                        else:
                            flag = 0

                        pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        pygame.draw.circle(self.screen, TAN, (920, 165), 80, 7)  ## ID
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        print('Dead State 1')






            if any(char2 in self.FirstSymbolIF for char2 in Token1[0]) and flag == 1:





                    pygame.draw.circle(self.screen, SPRINGGREEN, (690, 385), 45, 7)  ## is IF
                    pygame.display.update()
                    pygame.event.pump()
                    pygame.time.delay(2000)

                    if any(char2 in self.SecondSymbolIF for char2 in Token1[1]) and flag ==1:





                        pygame.draw.circle(self.screen, SPRINGGREEN, (537, 384), 45, 7)  ## IF
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        print('IF')

                        for counter2 in range(1, len(Token1)-1):

                            j = counter2 + 1

                            if any(char2 in self.SecondSymbolPlusID for char2 in Token1[j]) and flag ==1:

                                if j < len(Token1) -1 :
                                    j += 1
                                else:
                                    flag = 0




                                pygame.draw.circle(self.screen, TAN, (537, 384), 45, 7)  ## IF
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)


                                pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)


                                print('ID route 3')


                            elif any(char2 in self.CharactersPostID for char2 in Token1[j]) and flag == 1:

                                if j < len(Token1) -1 :
                                   j += 1
                                else:
                                     flag = 0

                                pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('Dead State 1')

                    elif any(char2 in self.SecondSymbolPlusID for char2 in Token1[1]) and flag ==1:


                        pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        print('ID route 2')

                        for counter2 in range(1, len(Token1)-1):

                            j = counter2 + 1

                            if any(char2 in self.SecondSymbolPlusID for char2 in Token1[j]) and flag == 1:

                                if j < len(Token1)-1:
                                    j += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (537, 384), 45, 7)  ## IF
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('ID route 3')


                            elif any(char2 in self.CharactersPostID for char2 in Token1[j]) and flag == 1:

                                if j < len(Token1)-1:
                                    j += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('Dead State 1')


                    elif any(char2 in self.CharactersPostID for char2 in Token1[1]) and flag == 1:





                        pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)

                        print('Dead State 1')

                        for counter2 in range(1, len(Token1)-1):
                            j = counter2 + 1

                            if any(char2 in self.CharactersPostID for char2 in Token1[j]) and flag == 1:

                                if j < len(Token1)-1:
                                  j += 1
                                else:
                                     flag = 0

                                pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('Dead State 1')













            if any(char3 in self.FirstSymbolTHEN for char3 in Token1[0]) and flag ==1:


                    pygame.draw.circle(self.screen, SPRINGGREEN, (387, 583), 45, 7)     ## is Then 1
                    pygame.display.update()
                    pygame.event.pump()
                    pygame.time.delay(2000)



                    if any(char3 in self.SecondSymbolTHEN for char3 in Token1[1]) and flag ==1:


                        pygame.draw.circle(self.screen, SPRINGGREEN, (288, 495), 45, 7)  ## is then 2
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)

                        if any(char3 in self.ThirdSymbolTHEN for char3 in Token1[2]) and flag ==1:


                            pygame.draw.circle(self.screen, SPRINGGREEN, (251, 370), 45, 7)  ## is then 3
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)

                            if any(char3 in self.FourthSymbolTHEN for char3 in Token1[3]) and flag ==1:


                                pygame.draw.circle(self.screen, SPRINGGREEN, (290, 257), 45, 7)       ## Then
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)

                                for counter3 in range(3, len(Token1) - 1):

                                    k = counter3 + 1

                                    if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                        if k < len(Token1) - 1:
                                            k += 1
                                        else:
                                            flag = 0

                                        pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                        pygame.display.update()
                                        pygame.event.pump()
                                        pygame.time.delay(2000)
                                        print('ID route then')


                                    elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                        if k < len(Token1) - 1:
                                            k += 1
                                        else:
                                            flag = 0

                                        pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                                        pygame.display.update()
                                        pygame.event.pump()
                                        pygame.time.delay(2000)
                                        print('Dead State 1')



                            elif any(char3 in self.CharactersPostID for char3 in Token1[3]) and flag == 1:

                                pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('Dead State 1')

                                for counter3 in range(3, len(Token1) - 1):

                                    k = counter3 + 1

                                    if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                        if k < len(Token1) - 1:
                                            k += 1
                                        else:
                                            flag = 0

                                        pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID

                                        print('ID route then')


                                    elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                        if k < len(Token1) - 1:
                                            k += 1
                                        else:
                                            flag = 0

                                        pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                                        pygame.display.update()
                                        pygame.event.pump()
                                        pygame.time.delay(2000)
                                        print('Dead State 1')
                            elif any(char3 in self.SecondSymbolPlusID for char3 in Token1[3]) and flag == 1:

                                pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('ID route 4')

                                for counter3 in range(3, len(Token1) - 1):

                                    k = counter3 + 1

                                    if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                        if k < len(Token1) - 1:
                                            k += 1
                                        else:
                                            flag = 0

                                        pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                        pygame.display.update()
                                        pygame.event.pump()
                                        pygame.time.delay(2000)
                                        print('ID route then')


                                    elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                        if k < len(Token1) - 1:
                                            k += 1
                                        else:
                                            flag = 0

                                        pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                                        pygame.display.update()
                                        pygame.event.pump()
                                        pygame.time.delay(2000)
                                        print('Dead State 1')

                            elif any(char3 in self.CharactersPostID for char3 in Token1[3]) and flag == 1:

                                pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('Dead State 1')

                                for counter3 in range(3, len(Token1) - 1):

                                    k = counter3 + 1

                                    if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                        if k < len(Token1) - 1:
                                            k += 1
                                        else:
                                            flag = 0

                                        pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                        pygame.display.update()
                                        pygame.event.pump()
                                        pygame.time.delay(2000)
                                        print('ID route then')


                                    elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                        if k < len(Token1) - 1:
                                            k += 1
                                        else:
                                            flag = 0

                                        pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                                        pygame.display.update()
                                        pygame.event.pump()
                                        pygame.time.delay(2000)
                                        print('Dead State 1')

                        elif any(char3 in self.SecondSymbolPlusID for char3 in Token1[2]) and flag == 1:

                            pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('ID route 4')

                            for counter3 in range(2, len(Token1) - 1):

                                k = counter3 + 1

                                if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                    if k < len(Token1) - 1:
                                        k += 1
                                    else:
                                        flag = 0

                                    pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                    pygame.display.update()
                                    pygame.event.pump()
                                    pygame.time.delay(2000)
                                    print('ID route then')


                                elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                    if k < len(Token1) - 1:
                                        k += 1
                                    else:
                                        flag = 0

                                    pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                                    pygame.display.update()
                                    pygame.event.pump()
                                    pygame.time.delay(2000)
                                    print('Dead State 1')

                        elif any(char3 in self.CharactersPostID for char3 in Token1[2]) and flag == 1:

                            pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('Dead State 1')

                            for counter3 in range(2, len(Token1) - 1):

                                k = counter3 + 1

                                if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                    if k < len(Token1) - 1:
                                        k += 1
                                    else:
                                        flag = 0

                                    pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                    pygame.display.update()
                                    pygame.event.pump()
                                    pygame.time.delay(2000)
                                    print('ID route then')


                                elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                    if k < len(Token1) - 1:
                                        k += 1
                                    else:
                                        flag = 0

                                    pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                                    pygame.display.update()
                                    pygame.event.pump()
                                    pygame.time.delay(2000)
                                    print('Dead State 1')




                    elif any(char3 in self.SecondSymbolPlusID for char3 in Token1[1]) and flag == 1:


                        pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        print('ID route 4')

                        for counter3 in range(1, len(Token1) - 1):

                            k = counter3 + 1

                            if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('ID route then')


                            elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('Dead State 1')

                    elif any(char3 in self.CharactersPostID for char3 in Token1[1]) and flag == 1:


                        pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        print('Dead State 1')

                        for counter3 in range(1, len(Token1) - 1):

                            k = counter3 + 1

                            if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('ID route then')


                            elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (610, 512), 45, 7)  ## Dead left
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('Dead State 1')









            if any(char3 in self.FirstSymbolElse_End for char3 in Token1[0]) and flag == 1:

                pygame.draw.circle(self.screen, SPRINGGREEN, (1155, 452), 45, 7)  ## is else or end
                pygame.display.update()
                pygame.event.pump()
                pygame.time.delay(2000)
                if any(char3 in self.SecondSymbolELSE for char3 in Token1[1]) and flag == 1:

                    pygame.draw.circle(self.screen, SPRINGGREEN, (1248, 373), 45, 7)  ## is else 1
                    pygame.display.update()
                    pygame.event.pump()
                    pygame.time.delay(2000)
                    if any(char3 in self.ThirdSymbolELSE for char3 in Token1[2]) and flag == 1:

                        pygame.draw.circle(self.screen, SPRINGGREEN, (1375, 373), 45, 7)  ## is else 2
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        if any(char3 in self.FourthSymbolELSE for char3 in Token1[3]) and flag == 1:

                            pygame.draw.circle(self.screen, SPRINGGREEN, (1503, 372), 45, 7)  ## else
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            for counter3 in range(3, len(Token1) - 1):

                                k = counter3 + 1

                                if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                    if k < len(Token1) - 1:
                                      k += 1
                                    else:
                                      flag = 0

                                    pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                    pygame.display.update()
                                    pygame.event.pump()
                                    pygame.time.delay(2000)
                                    print('ID route then test 1')


                                elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                    if k < len(Token1) - 1:
                                         k += 1
                                    else:
                                        flag = 0

                                    pygame.draw.circle(self.screen, TAN, (1500, 499), 45, 7)  ## Dead Right
                                    pygame.display.update()
                                    pygame.event.pump()
                                    pygame.time.delay(2000)
                                    print('Dead State 1')

                        elif any(char3 in self.CharactersPostID for char3 in Token1[3]) and flag == 1:

                            pygame.draw.circle(self.screen, TAN, (1500, 499), 45, 7)  ## Dead Right
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('Dead State 1')

                            for counter3 in range(3, len(Token1) - 1):

                                k = counter3 + 1

                                if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                    if k < len(Token1) - 1:
                                        k += 1
                                    else:
                                        flag = 0

                                    pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                    pygame.display.update()
                                    pygame.event.pump()
                                    pygame.time.delay(2000)
                                    print('ID route then')


                                elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                    if k < len(Token1) - 1:
                                        k += 1
                                    else:
                                        flag = 0

                                    pygame.draw.circle(self.screen, TAN, (1500, 499), 45, 7)  ## Dead Right
                                    pygame.display.update()
                                    pygame.event.pump()
                                    pygame.time.delay(2000)
                                    print('Dead State 1')
                        elif any(char3 in self.SecondSymbolPlusID for char3 in Token1[3]) and flag == 1:

                            pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('ID route 4')

                            for counter3 in range(3, len(Token1) - 1):

                                k = counter3 + 1

                                if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                    if k < len(Token1) - 1:
                                        k += 1
                                    else:
                                        flag = 0

                                    pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                    pygame.display.update()
                                    pygame.event.pump()
                                    pygame.time.delay(2000)
                                    print('ID route then')


                                elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                    if k < len(Token1) - 1:
                                        k += 1
                                    else:
                                        flag = 0

                                    pygame.draw.circle(self.screen, TAN, (1500, 499), 45, 7)  ## Dead Right
                                    pygame.display.update()
                                    pygame.event.pump()
                                    pygame.time.delay(2000)
                                    print('Dead State 1')

                        elif any(char3 in self.CharactersPostID for char3 in Token1[3]) and flag == 1:

                            pygame.draw.circle(self.screen, TAN, (1500, 499), 45, 7)  ## Dead Right
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('Dead State 1')

                            for counter3 in range(3, len(Token1) - 1):

                                k = counter3 + 1

                                if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                    if k < len(Token1) - 1:
                                        k += 1
                                    else:
                                        flag = 0

                                    pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                    pygame.display.update()
                                    pygame.event.pump()
                                    pygame.time.delay(2000)
                                    print('ID route then')


                                elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                    if k < len(Token1) - 1:
                                        k += 1
                                    else:
                                        flag = 0

                                    pygame.draw.circle(self.screen, TAN, (1500, 499), 45, 7)  ## Dead Right
                                    pygame.display.update()
                                    pygame.event.pump()
                                    pygame.time.delay(2000)
                                    print('Dead State 1')

                    elif any(char3 in self.SecondSymbolPlusID for char3 in Token1[2]) and flag == 1:

                        pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        print('ID route 4')

                        for counter3 in range(2, len(Token1) - 1):

                            k = counter3 + 1

                            if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('ID route then')


                            elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (1500, 499), 45, 7)  ## Dead Right
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('Dead State 1')

                    elif any(char3 in self.CharactersPostID for char3 in Token1[2]) and flag == 1:

                        pygame.draw.circle(self.screen, TAN, (1500, 499), 45, 7)  ## Dead Right
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        print('Dead State 1')

                        for counter3 in range(2, len(Token1) - 1):

                            k = counter3 + 1

                            if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('ID route then')


                            elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (1500, 499), 45, 7)  ## Dead Right
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('Dead State 1')



                elif any(char3 in self.SecondSymbolEND for char3 in Token1[1]) and flag == 1:

                    pygame.draw.circle(self.screen, SPRINGGREEN, (1599, 585), 45, 7)  ## is end
                    pygame.display.update()
                    pygame.event.pump()
                    pygame.time.delay(2000)

                    if any(char3 in self.ThirdSymbolEND for char3 in Token1[2]) and flag == 1:

                        pygame.draw.circle(self.screen, SPRINGGREEN, (1727, 585), 45, 7)  ## end
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        for counter3 in range(2, len(Token1) - 1):

                            k = counter3 + 1

                            if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('ID route then test 2')


                            elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (1500, 499), 45, 7)  ## Dead Right
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('Dead State 1')

                    for counter3 in range(2, len(Token1) - 1):

                        k = counter3 + 1

                        if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                            if k < len(Token1) - 1:
                                k += 1
                            else:
                                flag = 0

                            pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('ID route then test 3')


                        elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                            if k < len(Token1) - 1:
                                k += 1
                            else:
                                flag = 0

                            pygame.draw.circle(self.screen, TAN, (1500, 499), 45, 7)  ## Dead Right
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('Dead State 1')

                elif any(char3 in self.SecondSymbolPlusID2 for char3 in Token1[1]) and flag == 1:

                    pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                    pygame.display.update()
                    pygame.event.pump()
                    pygame.time.delay(2000)
                    print('ID route 4')

                    for counter3 in range(1, len(Token1) - 1):

                        k = counter3 + 1

                        if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                            if k < len(Token1) - 1:
                                k += 1
                            else:
                                flag = 0

                            pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('ID route then')


                        elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                            if k < len(Token1) - 1:
                                k += 1
                            else:
                                flag = 0

                            pygame.draw.circle(self.screen, TAN, (1500, 499), 45, 7)  ## Dead Right
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('Dead State 1')

                elif any(char3 in self.CharactersPostID for char3 in Token1[1]) and flag == 1:

                    pygame.draw.circle(self.screen, TAN, (1500, 499), 45, 7)  ## Dead Right
                    pygame.display.update()
                    pygame.event.pump()
                    pygame.time.delay(2000)
                    print('Dead State 1')

                    for counter3 in range(1, len(Token1) - 1):

                        k = counter3 + 1

                        if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                            if k < len(Token1) - 1:
                                k += 1
                            else:
                                flag = 0

                            pygame.draw.circle(self.screen, SPRINGGREEN, (920, 165), 80, 7)  ## ID
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('ID route then')


                        elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                            if k < len(Token1) - 1:
                                k += 1
                            else:
                                flag = 0

                            pygame.draw.circle(self.screen, TAN, (1500, 499), 45, 7)  ## Dead Right
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('Dead State 1')








           #################################################### ///////////////////////////// := #


            if any(char2 in self.FirstSymbolDotEqual for char2 in Token1[0]) and flag == 1:


                    pygame.draw.circle(self.screen, SPRINGGREEN, (880, 605), 45, 7)  ## is Assign
                    pygame.display.update()
                    pygame.event.pump()
                    pygame.time.delay(2000)

                    if any(char2 in self.SecondSymbolDotEqual for char2 in Token1[1]) and flag ==1:


                        pygame.draw.circle(self.screen, SPRINGGREEN, (880, 747), 45, 7)  ## ASSIGN
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)


                        for counter2 in range(1, len(Token1)-1):

                            j = counter2 + 1

                            if any(char2 in self.SecondSymbolPlusID for char2 in Token1[j]) and flag ==1:

                                if j < len(Token1) -1 :
                                    j += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)


                            elif any(char2 in self.CharactersPostID for char2 in Token1[j]) and flag == 1:

                                if j < len(Token1) -1 :
                                   j += 1
                                else:
                                     flag = 0

                                pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)

                    elif any(char2 in self.SecondSymbolPlusID for char2 in Token1[1]) and flag ==1:


                        pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)        ## Dead center
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)


                        for counter2 in range(1, len(Token1)-1):

                            j = counter2 + 1

                            if any(char2 in self.SecondSymbolPlusID for char2 in Token1[j]) and flag == 1:

                                if j < len(Token1)-1:
                                    j += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('ID route 3')


                            elif any(char2 in self.CharactersPostID for char2 in Token1[j]) and flag == 1:

                                if j < len(Token1)-1:
                                    j += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)        ## Dead center
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('Dead State 1')


                    elif any(char2 in self.CharactersPostID for char2 in Token1[1]) and flag == 1:





                        pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)        ## Dead center
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)


                        for counter2 in range(1, len(Token1)-1):
                            j = counter2 + 1

                            if any(char2 in self.CharactersPostID for char2 in Token1[j]) and flag == 1:

                                if j < len(Token1)-1:
                                  j += 1
                                else:
                                     flag = 0

                                pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)        ## Dead center
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)














            if any(char3 in self.Digits for char3 in Token1[0]) and flag == 1:

                pygame.draw.circle(self.screen, SPRINGGREEN, (1190, 726), 45, 7)  ## NUM
                pygame.display.update()
                pygame.event.pump()
                pygame.time.delay(2000)
                if len(Token1) < 2:
                    flag =0

                if  flag == 1 and any(char3 in self.Dot for char3 in Token1[1]):

                    pygame.draw.circle(self.screen, SPRINGGREEN, (1085, 835), 45, 7)  ## is float
                    pygame.display.update()
                    pygame.event.pump()
                    pygame.time.delay(2000)
                    if len(Token1) < 3:
                        flag = 0

                    if any(char3 in self.Digits for char3 in Token1[2]) and flag == 1:

                        pygame.draw.circle(self.screen, SPRINGGREEN, (1190, 726), 45, 7)  ## NUM
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        if len(Token1) < 4:
                            flag = 0

                        for counter3 in range(2, len(Token1) - 1):

                            k = counter3 + 1

                            if any(char3 in self.SecondSymbolPlusIdDigitless for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('ID route then test 52')


                            elif any(char3 in self.Dot for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('Dead State test 67')

                            elif any(char3 in self.Digits for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, SPRINGGREEN, (1190, 726), 45, 7)  ## NUM
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)


                    elif any(char3 in self.SecondSymbolPlusIdDigitless for char3 in Token1[2]) and flag == 1:

                        pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        print('Dead State test 123')

                        for counter3 in range(2, len(Token1) - 1):

                            k = counter3 + 1

                            if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('ID route then')


                            elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)
                                print('Dead State 154')
                    elif any(char3 in self.Dot for char3 in Token1[2]) and flag == 1:

                        pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)
                        print('ID route 4')

                        for counter3 in range(2, len(Token1) - 1):

                            k = counter3 + 1

                            if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)



                            elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                                if k < len(Token1) - 1:
                                    k += 1
                                else:
                                    flag = 0

                                pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                                pygame.display.update()
                                pygame.event.pump()
                                pygame.time.delay(2000)


                elif flag == 1 and any(char3 in self.SecondSymbolPlusIdDigitless for char3 in Token1[1]):

                    pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                    pygame.display.update()
                    pygame.event.pump()
                    pygame.time.delay(2000)
                    print('Dead State 35')

                    for counter3 in range(1, len(Token1) - 1):

                        k = counter3 + 1

                        if any(char3 in self.SecondSymbolPlusID for char3 in Token1[k]) and flag == 1:

                            if k < len(Token1) - 1:
                                k += 1
                            else:
                                flag = 0

                            pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('Dead State 369')


                        elif any(char3 in self.CharactersPostID for char3 in Token1[k]) and flag == 1:

                            if k < len(Token1) - 1:
                                k += 1
                            else:
                                flag = 0

                            pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('Dead State test 58')

                elif  flag == 1 and any(char3 in self.Digits for char3 in Token1[1]):

                    pygame.draw.circle(self.screen, SPRINGGREEN, (1190, 726), 45, 7)  ## NUM
                    pygame.display.update()
                    pygame.event.pump()
                    pygame.time.delay(2000)
                    for counter3 in range(1, len(Token1) - 1):

                        k = counter3 + 1

                        if any(char3 in self.SecondSymbolPlusIdDigitless for char3 in Token1[k]) and flag == 1:

                            if k < len(Token1) - 1:
                                k += 1
                            else:
                                flag = 0

                            pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('ID route then test 52')


                        elif any(char3 in self.Dot for char3 in Token1[k]) and flag == 1:

                            if k < len(Token1) - 1:
                                k += 1
                            else:
                                flag = 0

                            pygame.draw.circle(self.screen, SPRINGGREEN, (1085, 835), 45, 7)  ## is float
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)
                            print('Dead State test 67')

                        elif any(char3 in self.Digits for char3 in Token1[k]) and flag == 1:

                            if k < len(Token1) - 1:
                                k += 1
                            else:
                                flag = 0

                            pygame.draw.circle(self.screen, SPRINGGREEN, (1190, 726), 45, 7)  ## NUM
                            pygame.display.update()
                            pygame.event.pump()
                            pygame.time.delay(2000)








            if any(char1 in self.Semicolon for char1 in Token1[0]) and flag ==1:


                pygame.draw.circle(self.screen, SPRINGGREEN, (1320, 726), 45, 7)        ## semicolon
                pygame.display.update()
                pygame.event.pump()
                pygame.time.delay(2000)
                for counter1 in range(0, len(Token1)-1):



                    i = counter1 + 1


                    if any(char1 in self.SecondSymbolPlusIDAllCharacters for char1 in Token1[i]) and flag ==1:
                        if i < len(Token1) - 1:
                            i += 1
                        else:
                            flag = 0

                        pygame.draw.circle(self.screen, TAN, (1012, 605), 45, 7)  ## Dead center
                        pygame.display.update()
                        pygame.event.pump()
                        pygame.time.delay(2000)





























        elif self.algorithm_state == 'Upload':



            file = filedialog.askopenfilename()
            fob = open(file, 'r')
            self.Sentence = fob.read()
            print(fob.read())

            #with open('User_Input.txt') as f:
             #   self.Sentence = f.read()
              #  print(self.Sentence)



        elif self.algorithm_state == 'Tockenize':

            self.Sentence = self.Sentence.replace(";", " ; ")
            self.list = self.Sentence.split()
            self.list = [s.strip() for s in self.list]
            for x in range(0, len(self.list)):
                print(self.list[x])


            my_string = ' '.join(self.Sentence.split())  # join lines with spaces
            my_string = my_string.replace(";", " ; ")  # any semicolon will have space before and after
            my_string = my_string.replace(":=", " := ")  # any semicolon will have space before and after



            my_pattern = re.compile(r"\S+")  # matching any sequence of non-whitespaces
            matches = my_pattern.findall(my_string)
            # for match in matches:
            #    print(match)

            # my_pattern = r"([a-zA-Z]+[a-zA-Z0-9_-]*|:=|;|[0-9.0-9]+|[0-9]+)"
            # my_pattern = (r"\S+")
            # lis = regexp_tokenize(my_string, my_pattern)
            # print("INPUT STRING: ")
            # print(lis)

            token_type_list = []
            for attr in matches:
                    # match each attribute to its token type and output the token in angled brackets
                    if attr.lower() == "if":
                        print("<" + attr + ", " + "IF>")
                        token_type_list.append("IF")
                        continue
                    elif attr.lower() == "then":
                        print("<" + attr + ", " + "THEN>")
                        token_type_list.append("THEN")
                        continue
                    elif attr.lower() == "end":
                        print("<" + attr + ", " + "END>")
                        token_type_list.append("END")
                        continue
                    elif attr.lower() == "else":
                        print("<" + attr + ", " + "ELSE>")
                        token_type_list.append("ELSE")
                        continue
                    elif attr == ":=":
                        print("<" + attr + ", " + "ASSIGN>")
                        token_type_list.append("ASSIGN")
                        continue
                    elif attr == ";":
                        print("<" + attr + ", " + "SEMICOLON>")
                        token_type_list.append("SEMICOLON")
                        continue
                    elif re.fullmatch(r"[0-9]+|[0-9]+.[0-9]+", attr):
                        print("<" + attr + ", " + "NUM>")
                        token_type_list.append("NUM")
                        continue
                    elif re.fullmatch(r"[a-zA-Z][a-zA-Z0-9]*", attr):
                        print("<" + attr + ", " + "ID>")
                        token_type_list.append("ID")
                    else:  # unidentifiable token
                        print("<" + attr + ", " + "UNIDENTIFIABLE>")
                        token_type_list.append("UNIDENTIFIABLE")
            # print("\n--done tokenization--")
            # print("\nTOKEN_LIST: ")
            print(token_type_list)







        pygame.display.update()
        pygame.event.pump()
        self.state = 'main menu'

