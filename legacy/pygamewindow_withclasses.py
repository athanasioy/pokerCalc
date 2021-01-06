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
            font = pygame.font.SysFont('Garamond', 20)
            text = font.render(self.text, 1, white)
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
        self.mainWindow = pygame.display.set_mode((width,height))
        pygame.display.set_caption("Poker Calculator")

        self.deckcards100 = []
        self.card_positions = []

        self.ConfirmButton = Button(black,25,490,150,60,'Confirm Hand')

        self.CardLimit = 0
        self.running = True

        self.myhand = []
        self.table_cards = []


    def GetCardDirectory(self):
        self.spadejpg = glob2.glob("deck/100Percent/spades/*.jpg")
        self.heartsjpg = glob2.glob("deck/100Percent/hearts/*.jpg")
        self.clubsjpg = glob2.glob("deck/100Percent/clubs/*.jpg")
        self.diamondjpg = glob2.glob("deck/100Percent/diamonds/*.jpg")

        for clubs in clubsjpg:
            self.deckcards100.append(pygame.image.load(clubs))
        for diamond in diamondjpg:
            self.deckcards100.append(pygame.image.load(diamond))
        for spades in spadejpg:
            self.deckcards100.append(pygame.image.load(spades))
        for hearts in heartsjpg:
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

    def getEvents(self):
        self.events = pyame.event.get()
        for event in self.events:
            #Quit Event
            if event.type == pygame.QUIT:
                    self.running = False
            self.pos = pygame.mouse.get_pos()
            #Button Change Color Mechanic
            if event.type == pygame.MOUSEMOTION:
                if self.ConfirmButton.isOver(pos):
                    self.ConfirmButton.color = self.lightgray
                else:
                    self.ConfirmButton.color = self.black
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    for i in range(len(self.card_positions)):
                        if isBetween(self.pos,self.card_positions[i]):
                            if self.deckcards100[i].get_size() == (100,100) and self.CardLimit<2:
                                self.deckcards100[i] = pygame.transform.scale(self.deckcards100[i],(80,80))
                                self.myhand.append(deck[i])
                                self.CardLimit +=1
                            elif self.deckcards100[i].get_size() == (80,80):
                                self.deckcards100[i] = pygame.transform.scale(self.deckcards100[i],(100,100))
                                self.myhand.remove(deck[i])
                                self.CardLimit -= 1
    def mainLoop(self):
        while self.running:
            count = 0
            for img in self.deckcards100:
                self.mainWindow.blit(img,card_positions[count])
                count += 1
            self.ConfirmButton.draw(self.mainWindow)



pygame.init()

deck = poker.createDeck()

#Set Colors
black = (0,0,0)
white = (255,255,255)
green = (0,68,1)
lightgray = (100,100,100)
#Window dimensions
height = 600
width = 1500

# deselected_scale = 1.25
# selected_scale  = 0.8

deckcards100 =[]

mainWindow = pygame.display.set_mode((width,height))
pygame.display.set_caption("Poker Calculator")

#Get directory for deck
spadejpg = glob2.glob("deck/100Percent/spades/*.jpg")
heartsjpg = glob2.glob("deck/100Percent/hearts/*.jpg")
clubsjpg = glob2.glob("deck/100Percent/clubs/*.jpg")
diamondjpg = glob2.glob("deck/100Percent/diamonds/*.jpg")


#get Dire

#Load pygame.image into a deckcard List

for clubs in clubsjpg:
    deckcards100.append(pygame.image.load(clubs))
for diamond in diamondjpg:
    deckcards100.append(pygame.image.load(diamond))
for spades in spadejpg:
    deckcards100.append(pygame.image.load(spades))
for hearts in heartsjpg:
    deckcards100.append(pygame.image.load(hearts))


card_positions = [] # We will save the card positions here

# Generate Card Positions and Save them
x = 15 #initial x
y = 25 # initial y
for count in range(len(deckcards100)):
    if count % 13 == 0 and count != 0: # change row every 13 cards!
        y += 110
        x = 15
    card_positions.append((x,y))
    x += 110

ConfirmButton = Button(black,25,490,150,60,'Confirm Hand')

running = True
counter = 0
#initialize lists
myhand = []
flop = []

while running:
    mainWindow.fill(green)


    #Add cards in mainWindow
    count = 0
    for img in deckcards100:
        mainWindow.blit(img,card_positions[count])
        count += 1

    for event in pygame.event.get():
        #Quit Event
        if event.type == pygame.QUIT:
                running = False
        pos = pygame.mouse.get_pos()


        #Button Change Color Mechanic
        if event.type == pygame.MOUSEMOTION:
            if ConfirmButton.isOver(pos):
                ConfirmButton.color = lightgray
            else:
                ConfirmButton.color = black
        #Click on Card Mechanic

        if event.type == pygame.MOUSEBUTTONDOWN:

            if pygame.mouse.get_pressed()[0]:
                for i in range(len(card_positions)):
                    if isBetween(pos,card_positions[i]):
                        if deckcards100[i].get_size() == (100,100) and counter<2:
                            deckcards100[i] = pygame.transform.scale(deckcards100[i],(80,80))
                            myhand.append(deck[i])
                            counter +=1
                        elif deckcards100[i].get_size() == (80,80):
                            deckcards100[i] = pygame.transform.scale(deckcards100[i],(100,100))
                            myhand.remove(deck[i])
                            counter -= 1
            if ConfirmButton.isOver(pos) and pygame.mouse.get_pressed()[0]:
                poker.removeCardsfromDeck(myhand,deck)

    ConfirmButton.draw(mainWindow)
    pygame.display.flip()
