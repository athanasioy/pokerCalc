import pygame
import glob2
import poker
State = 'hand'
def pickyourhand():
    mainWindow.fill(green)
    ConfirmButton.draw(mainWindow)
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
                        if deckcards100[i].get_size() == (100,100) and len(myhand)<2:
                            deckcards100[i] = pygame.transform.scale(deckcards100[i],(80,80))
                            myhand.append(deck[i])
                            CardLimit +=1
                        elif deckcards100[i].get_size() == (80,80):
                            deckcards100[i] = pygame.transform.scale(deckcards100[i],(100,100))
                            myhand.remove(deck[i])
                            CardLimit -= 1
            if ConfirmButton.isOver(pos) and pygame.mouse.get_pressed()[0]:
                ConfirmButton.text = "Confirm Flop"
                CardLimit = 0
                deck = poker.removeCardsfromDeck(myhand,deck)
                State = 'flop'
def pickFlop():
    mainWindow.fill(green)
    ConfirmButton.draw(mainWindow)
    #Add cards in mainWindow
    count = 0
    for img in deckcards100:
        mainWindow.blit(img,card_positions[count])
        count += 1
        mainWindow.blit(deckcards75[deck.index(my_hand[0])],(200,490))
        mainWindow.blit(deckcards75[deck.index(my_hand[1])],(310,490))

    for event in pygame.event.get():
        #Quit Event
        if event.type == pygame.QUIT:
                running = False
        #Button Change Color Mechanic
        if event.type == pygame.MOUSEMOTION:
            if ConfirmButton.isOver(pos):
                ConfirmButton.color = lightgray
            else:
                ConfirmButton.color = black
        if event.type == pygame.MOUSEBUTTONDOWN:

            if pygame.mouse.get_pressed()[0]:
                for i in range(len(card_positions)):
                    if isBetween(pos,card_positions[i]):
                        if deckcards100[i].get_size() == (100,100) and CardLimit<3:
                            deckcards100[i] = pygame.transform.scale(deckcards100[i],(80,80))
                            table_cards.append(deck[i])
                            CardLimit +=1
                        elif deckcards100[i].get_size() == (80,80):
                            deckcards100[i] = pygame.transform.scale(deckcards100[i],(100,100))
                            table_cards.remove(deck[i])
                            CardLimit -= 1

def Statemanager():
    if State == 'hand':
        pickyourhand()
    if State == 'flop':
        pickflop()


25,490,150,60
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
CardLimit = 0
#initialize lists
myhand = []
table_cards = []

while running:
    events = pygame.event.get()
    if State == 'hand':
        mainWindow.fill(green)
        ConfirmButton.draw(mainWindow)
        #Add cards in mainWindow
        count = 0
        for img in deckcards100:
            mainWindow.blit(img,card_positions[count])
            count += 1

        for event in events:
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
                            if deckcards100[i].get_size() == (100,100) and len(myhand)<2:
                                deckcards100[i] = pygame.transform.scale(deckcards100[i],(80,80))
                                myhand.append(deck[i])
                                CardLimit +=1
                            elif deckcards100[i].get_size() == (80,80):
                                deckcards100[i] = pygame.transform.scale(deckcards100[i],(100,100))
                                myhand.remove(deck[i])
                                CardLimit -= 1
                if ConfirmButton.isOver(pos) and pygame.mouse.get_pressed()[0]:
                    ConfirmButton.text = "Confirm Flop"
                    CardLimit = 0
                    # deck = poker.removeCardsfromDeck(myhand,deck)
                    State = 'flop'

        if State == 'flop':
            mainWindow.fill(green)
            ConfirmButton.draw(mainWindow)
            #Add cards in mainWindow
            count = 0
            for img in deckcards100:
                mainWindow.blit(img,card_positions[count])
                count += 1
            mainWindow.blit(deckcards100[deck.index(myhand[0])],(200,490))
            mainWindow.blit(deckcards100[deck.index(myhand[1])],(310,490))
            print("GotHere")
            for event in events:
                print("GotHere")
                #Quit Event
                if event.type == pygame.QUIT:
                        running = False
                #Button Change Color Mechanic
                pos = pygame.mouse.get_pos()
                print("GotHere")
                if event.type == pygame.MOUSEMOTION:
                    print("GotHere")
                    if ConfirmButton.isOver(pos):
                        ConfirmButton.color = lightgray
                    else:
                        ConfirmButton.color = black
                    print("GotHere")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pos)
                    if pygame.mouse.get_pressed()[0]:
                        print(pos)
                        for i in range(len(card_positions)):
                            print(i)
                            if isBetween(pos,card_positions[i]):
                                if deckcards100[i].get_size() == (100,100) and CardLimit<3:
                                    print("GotHere isBetween")
                                    deckcards100[i] = pygame.transform.scale(deckcards100[i],(80,80))
                                    table_cards.append(deck[i])
                                    CardLimit +=1
                                elif deckcards100[i].get_size() == (80,80):
                                    deckcards100[i] = pygame.transform.scale(deckcards100[i],(100,100))
                                    table_cards.remove(deck[i])
                                    CardLimit -= 1
    pygame.display.flip()
    print(pygame.event.peek())
    pygame.Clock.tick(10)
