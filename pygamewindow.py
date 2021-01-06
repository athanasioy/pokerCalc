import pygame
import glob2
import poker

def isBetween(cursor,card_pos):
    """pos and card_pos are both tuples of type (x,y)
    Returns true if pos is between card_pos and card_pos+100"""
    return all([cursorpos>=cardpos and cursorpos<=cardpos+100 for cursorpos,cardpos in zip(cursor,card_pos)])

class Button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)

        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text != '':
            font = pygame.font.SysFont('Tahoma', 20)
            text = font.render(self.text, 1, (255,255,255))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

class Poker():
    def __init__(self):
        pygame.init()
        self.state = 'HandState'

        self.deck = poker.createDeck()
        self.black = (0,0,0)
        self.white = (255,255,255)
        self.green = (0,68,1)
        self.lightgray = (100,100,100)
        self.height = 600
        self.width = 1500
        self.mainWindow = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Poker Calculator")

        self.deckcards100 = []
        self.card_positions = []

        self.ConfirmButton = Button(self.black,25,490,130,40,'Confirm Hand')
        self.ResetButton = Button(self.black, 1335, 490, 100, 40, 'Reset')
        self.CardLimit = 0
        self.CardLimiter = 2
        self.running = True

        self.myhand = []
        self.table_cards = []

        self.Font = pygame.font.SysFont('Arial',25)
        self.Font2 = pygame.font.SysFont('Arial',15)

        self.tableCardText = self.Font.render('Table Cards',True, self.black)
        self.myhandText = self.Font.render('My Hand...',True, self.black)


        #Probabilites text objects
        # self.noPairProb = ''
        # self.noPairText = self.Font2.render('No Pair {}'.format(self.noPairProb) ,True,self.lightgray)
        # self.OnePairProb = ''
        # self.OnePairText = self.Font2.render('One Pair {}'.format(self.OnePairProb) ,True,self.lightgray)
        # self.TwoPairProb = ''
        # self.TwoPairText = self.Font2.render('Two Pair {}'.format(self.TwoPairProb),True,self.lightgray)
        # self.ThreeofaKindProb = ''
        # self.ThreeofaKindText = self.Font2.render('Three of a Kind {}'.format(self.ThreeofaKindProb),True,self.lightgray)
        # self.StraightProb = ''
        # self.StraightText = self.Font2.render('Straight {}'.format(self.StraightProb),True,self.lightgray)
        # self.FlushProb = ''
        # self.FlushText = self.Font2.render('Flush {}'.format(self.FlushProb),True,self.lightgray)
        # self.FullHouseProb = ''
        # self.FullHouseText = self.Font2.render('FullHouse {}'.format(self.FullHouseProb),True,self.lightgray)
        # self.FourofaKindProb = ''
        # self.FourofaKindText = self.Font2.render('Four of a Kind {}'.format(self.FourofaKindProb),True,self.lightgray)
        # self.StraighFlushProb = ''
        # self.StraighFlushText = self.Font2.render('StraighFlush {}'.format(self.StraighFlushProb),True,self.lightgray)


        # self.CombinationProbList = [
        # self.noPairText,
        # self.OnePairText,
        # self.TwoPairText,
        # self.ThreeofaKindText,
        # self.StraightText,
        # self.FlushText,
        # self.FullHouseText,
        # self.FourofaKindText,
        # self.StraighFlushText,
        # ]

    def GetCardDirectory(self):
        self.spadejpg = glob2.glob("deck/100Percent/spades/*.jpg")
        self.heartsjpg = glob2.glob("deck/100Percent/hearts/*.jpg")
        self.clubsjpg = glob2.glob("deck/100Percent/clubs/*.jpg")
        self.diamondjpg = glob2.glob("deck/100Percent/diamonds/*.jpg")

        for clubs in self.clubsjpg:
            self.deckcards100.append(pygame.image.load(clubs))
        for diamond in self.diamondjpg:
            self.deckcards100.append(pygame.image.load(diamond))
        for spades in self.spadejpg:
            self.deckcards100.append(pygame.image.load(spades))
        for hearts in self.heartsjpg:
            self.deckcards100.append(pygame.image.load(hearts))

    def GenerateCardPositions(self):
        x = 15 # initial x
        y = 25 # initial y
        for count in range(len(self.deckcards100)):
            if count % 13 == 0 and count != 0: # change row every 13 cards!
                y += 110
                x = 15
            self.card_positions.append((x,y))
            x += 110


    def drawtext(self):
        self.mainWindow.blit(self.myhandText,(200,460))
        self.mainWindow.blit(self.tableCardText,(500,460))


    def drawButtons(self):
        self.ResetButton.draw(self.mainWindow)
        self.ConfirmButton.draw(self.mainWindow)

    def getEvents(self):
        self.events = pygame.event.get()

    def getandDrawProbabilities(self):
        self.noPairProb = poker.getProbability(self.myhand,self.table_cards,poker.noPair,poker.removeCardsfromDeck(self.myhand + self.table_cards, self.deck))
        self.OnePairProb = poker.getProbability(self.myhand,self.table_cards,poker.isOnePair,poker.removeCardsfromDeck(self.myhand + self.table_cards, self.deck))
        self.TwoPairProb = poker.getProbability(self.myhand,self.table_cards,poker.isTwoPair,poker.removeCardsfromDeck(self.myhand + self.table_cards, self.deck))
        self.ThreeofaKindProb = poker.getProbability(self.myhand,self.table_cards,poker.isThreeOfaKind,poker.removeCardsfromDeck(self.myhand + self.table_cards, self.deck))
        self.StraightProb = poker.getProbability(self.myhand,self.table_cards,poker.isStraight,poker.removeCardsfromDeck(self.myhand + self.table_cards, self.deck))
        self.FlushProb = poker.getProbability(self.myhand,self.table_cards,poker.isFlush,poker.removeCardsfromDeck(self.myhand + self.table_cards, self.deck))
        self.FullHouseProb = poker.getProbability(self.myhand,self.table_cards,poker.isFullHouse,poker.removeCardsfromDeck(self.myhand + self.table_cards, self.deck))
        self.FourofaKindProb = poker.getProbability(self.myhand,self.table_cards,poker.isFourOfaKInd,poker.removeCardsfromDeck(self.myhand + self.table_cards, self.deck))
        self.StraighFlushProb= poker.getProbability(self.myhand,self.table_cards,poker.isStraightFlush,poker.removeCardsfromDeck(self.myhand + self.table_cards, self.deck))

        #Render Font again
        self.noPairText = self.Font2.render('No Pair {}'.format(self.noPairProb) ,True,self.black)
        self.OnePairText = self.Font2.render('One Pair {}'.format(self.OnePairProb) ,True,self.black)
        self.TwoPairText = self.Font2.render('Two Pair {}'.format(self.TwoPairProb),True,self.black)
        self.ThreeofaKindText = self.Font2.render('Three of a Kind {}'.format(self.ThreeofaKindProb),True,self.black)
        self.StraightText = self.Font2.render('Straight {}'.format(self.StraightProb),True,self.black)
        self.FlushText = self.Font2.render('Flush {}'.format(self.FlushProb),True,self.black)
        self.FullHouseText = self.Font2.render('FullHouse {}'.format(self.FullHouseProb),True,self.black)
        self.FourofaKindText = self.Font2.render('Four of a Kind {}'.format(self.FourofaKindProb),True,self.black)
        self.StraighFlushText = self.Font2.render('StraighFlush {}'.format(self.StraighFlushProb),True,self.black)

        self.CombinationProbList = [
        self.noPairText,
        self.OnePairText,
        self.TwoPairText,
        self.ThreeofaKindText,
        self.StraightText,
        self.FlushText,
        self.FullHouseText,
        self.FourofaKindText,
        self.StraighFlushText,
        ]

    def buttonColorFunctionality(self,event):
        if event.type == pygame.MOUSEMOTION:
            if self.ConfirmButton.isOver(self.pos):
                self.ConfirmButton.color = self.lightgray
            else:
                self.ConfirmButton.color = self.black
            if self.ResetButton.isOver(self.pos):
                self.ResetButton.color = self.lightgray
            else:
                self.ResetButton.color = self.black

    def handeventFunctionality(self):
        for event in self.events:
            #Quit Event
            if event.type == pygame.QUIT:
                    self.running = False
            self.pos = pygame.mouse.get_pos()
            #Button Change Color Mechanic
            self.buttonColorFunctionality(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    for i in range(len(self.card_positions)):
                        if isBetween(self.pos,self.card_positions[i]):
                            if self.deckcards100[i].get_size() == (100,100) and self.CardLimit<2:
                                self.deckcards100[i] = pygame.transform.scale(self.deckcards100[i],(80,80))
                                self.myhand.append(self.deck[i])
                                self.CardLimit +=1
                            elif self.deckcards100[i].get_size() == (80,80):
                                self.deckcards100[i] = pygame.transform.scale(self.deckcards100[i],(100,100))
                                self.myhand.remove(self.deck[i])
                                self.CardLimit -= 1
                if self.ConfirmButton.isOver(self.pos) and pygame.mouse.get_pressed()[0] and len(self.myhand) == 2:
                    # self.deck = poker.removeCardsfromDeck(self.myhand,self.deck)
                    self.ConfirmButton.text = 'Confirm Flop'
                    self.state = 'flop'
                    self.CardLimit = 0
                if self.ResetButton.isOver(self.pos):
                    self.myhand = []
                    self.table_cards = []
                    self.state = 'handState'
                    for i in range(len(self.card_positions)):
                        if self.deckcards100[i].get_size() == (80,80):
                            self.deckcards100[i] = pygame.transform.scale(self.deckcards100[i],(100,100))

    def flopEventFunctionality(self):
        for event in self.events:
            #Quit Event
            if event.type == pygame.QUIT:
                    self.running = False
            self.pos = pygame.mouse.get_pos()
            #Button Change Color Mechanic
            self.buttonColorFunctionality(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        for i in range(len(self.card_positions)):
                            if isBetween(self.pos,self.card_positions[i]):
                                if self.deckcards100[i].get_size() == (100,100) and self.CardLimit<5:
                                    self.deckcards100[i] = pygame.transform.scale(self.deckcards100[i],(80,80))
                                    self.table_cards.append(self.deck[i])
                                    self.CardLimit +=1
                                elif self.deckcards100[i].get_size() == (80,80):
                                    self.deckcards100[i] = pygame.transform.scale(self.deckcards100[i],(100,100))
                                    self.table_cards.remove(self.deck[i])
                                    self.CardLimit -= 1
                    if self.ConfirmButton.isOver(self.pos) and len(self.table_cards) >= 3:
                        # self.deck = poker.removeCardsfromDeck(self.myhand,self.deck)
                        self.ConfirmButton.text = 'Confirm Turn'
                        self.state = 'turn'
                        #Get Probabilities!
                        self.getandDrawProbabilities()

                    if self.ResetButton.isOver(self.pos):
                        self.myhand = []
                        self.table_cards = []
                        self.state = 'HandState'
                        self.CardLimit = 0
                        for i in range(len(self.card_positions)):
                            if self.deckcards100[i].get_size() == (80,80):
                                self.deckcards100[i] = pygame.transform.scale(self.deckcards100[i],(100,100))
    def handLoop(self):
        self.getEvents()
        self.mainWindow.fill(self.green)
        #Draw the Text on the screen
        self.drawtext()

        count = 0
        for img in self.deckcards100:
            self.mainWindow.blit(img,self.card_positions[count])
            count += 1
        self.drawButtons()
        self.handeventFunctionality()
        pygame.display.update()


    def flopLoop(self):
        self.getEvents()
        self.mainWindow.fill(self.green)
        #Draw the Text on the screen
        self.drawtext()

        #Draw Cards and my hand Cards
        count = 0
        for img in self.deckcards100:
            self.mainWindow.blit(img,self.card_positions[count])
            count += 1
        x = 200
        for i in range(len(self.myhand)):
            self.mainWindow.blit(self.deckcards100[self.deck.index(self.myhand[i])],(x,490))
            x += 110
        #Buttons!
        self.drawButtons()

        self.flopEventFunctionality()
        pygame.display.update()


    def turnloop(self):
        self.getEvents()
        self.mainWindow.fill(self.green)
        self.drawtext()
        count = 0
        #Draw Cards,my hand Cards and Table Cards!
        for img in self.deckcards100:
            self.mainWindow.blit(img,self.card_positions[count])
            count += 1
        x = 200
        for i in range(len(self.myhand)):
            self.mainWindow.blit(self.deckcards100[self.deck.index(self.myhand[i])],(x,490))
            x += 110
        x = 500
        for i in range(len(self.table_cards)):
            self.mainWindow.blit(self.deckcards100[self.deck.index(self.table_cards[i])],(x,490))
            x += 110

        x = 1200
        y = 460
        for img in self.CombinationProbList:
            self.mainWindow.blit(img,(x,y))
            y += 14

        self.drawButtons()

        self.flopEventFunctionality()
        pygame.display.update()


    def stateManager(self):
        if self.state == 'turn':
            self.turnloop()
        if self.state == 'flop':
            self.flopLoop()
        if self.state == 'HandState':
            self.handLoop()



g = Poker()
g.GetCardDirectory()
g.GenerateCardPositions()
print(g.card_positions)
while g.running:
    g.stateManager()
