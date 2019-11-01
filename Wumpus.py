import random, os,msvcrt

MONSTER = 'M'
HERO = 'H'
HOLE = 'O'
EMPTY = ' '
DEAD = 'X'

HOR_LINE = '\xc4'
VERT_LINE = '\xb3'
TL_CORNER = '\xda'
TR_CORNER = '\xbf'
TOP_INT = '\xc2'
LEFT_INT = '\xc3'
RIGHT_INT = '\xb4'
MID_INT = '\xc5'
BL_CORNER = '\xc0'
BR_CORNER = '\xd9'
BOT_INT = '\xc1'

class world:

    def __init__(self, size):
        
        random.seed(None)
        self.size = size  # The size of the world, a size of 4 means a 4x4 grid
        self.world = self.generateWorld()  # Randomly populates the world
        
        visited = []  # Keeps track of the visited squares for the recursive function
        
        # Uses the recursive function self.searchGrid to decide
        # if the hero can reach the monster
        self.valid = self.searchGrid(self.world.index(HERO), visited)

        while(self.valid == False):
            self.world = self.generateWorld()
            visited = []
            self.valid = self.searchGrid(self.world.index(HERO), visited)

    def __str__(self):
        
        tempstr = ''  # Creates an empty string
        tempstr += self.drawLine(1)  # Draws the top line of the grid into the empty string

        # Draws the rest of the grid into the string
        for count in range(self.size * self.size):
            
            # Draws each data line with spaces and a vertical line
            # separating each element of the row
            tempstr += VERT_LINE + " " + str(self.world[count]) + " "

            # Draws the lines between data rows
            if(count % self.size == self.size - 1):
                tempstr += VERT_LINE + "\n"
                if(count/self.size != self.size-1):
                    # Draws lines in between rows
                    tempstr += self.drawLine(2)
                else:
                    # Draws the bottom line
                    tempstr += self.drawLine(3)
                    
        # Adds a line that lets us know if the grid is solvable
        tempstr += '\n\n' + str(self.valid)
        
        return tempstr

    def drawLine(self,location):
        
        tempstr = ''
        
        # Draws the top line
        if(location == 1):
            tempstr += TL_CORNER + HOR_LINE*3
            for x in range(1,self.size):
                tempstr += TOP_INT + HOR_LINE*3
            tempstr += TR_CORNER + "\n"

        # Draws the lines in between rows
        elif(location == 2):
            tempstr += LEFT_INT + HOR_LINE*3
            for x in range(1,self.size):
                tempstr += MID_INT + HOR_LINE*3
            tempstr += RIGHT_INT + "\n"

        # Draws the bottom line
        elif(location == 3):
            tempstr += BL_CORNER + HOR_LINE*3
            for x in range(1,self.size):
                tempstr += BOT_INT + HOR_LINE*3
            tempstr += BR_CORNER + "\n"
            
        return tempstr


    def generateWorld(self):
        
        tempWorld = []
        
        #Fill the world with blank tiles
        for x in range(self.size * self.size):
            tempWorld += [EMPTY]
            
        #Fill 1/4 of the world with holes
        for x in range(self.size * self.size / 4):
            self.placeChar(HOLE,tempWorld)
            
        #Place a Monster in the world
        self.placeChar(MONSTER,tempWorld)
        
        #Place a Hero in the world
        self.placeChar(HERO,tempWorld)
        
        return tempWorld


    def searchGrid(self, x, visited):
        
        visited += [x]
        
        #Look at square above
        if(x/self.size != 0 and visited.count(x-self.size) == 0):
            if(self.world[x-self.size] == MONSTER):
                return True
            elif(self.world[x-self.size] != HOLE):
                if(self.searchGrid(x-self.size, visited)):
                    return True
                
        #Look at square below
        if(x/self.size != self.size-1 and visited.count(x+self.size) == 0):
            if(self.world[x+self.size] == MONSTER):
                return True
            elif(self.world[x+self.size] != HOLE):
                if(self.searchGrid(x+self.size, visited)):
                    return True
                
        #Look at square to the left
        if(x%self.size != 0 and visited.count(x-1) == 0):
            if(self.world[x-1] == MONSTER):
                return True
            elif(self.world[x-1] != HOLE):
                if(self.searchGrid(x-1, visited)):
                   return True
                
        #Look at square to the right
        if(x%self.size != self.size-1 and visited.count(x+1) == 0):
            if(self.world[x+1] == MONSTER):
                return True
            elif(self.world[x+1] != HOLE):
                if(self.searchGrid(x+1, visited)):
                    return True
                
        return False
    

    def placeChar(self, char, World):
        
        # Generates random numbers until one is found such that world[rand]
        # is an empty space, then places the character in world[rand]
        while True:
            rand = random.randrange(self.size*self.size)
            if (World[rand] == EMPTY):
                World[rand] = char
                break


    def moveHeroUp(self):
        
        # Finds the location of the hero
        x = self.world.index(HERO)

        # Moves if the hero isn't in the top row
        if(x/self.size != 0):
            
            # Finds the contents of the square above the hero
            contents = self.world[x-self.size]

            # Moves the hero up if the space is empty and a 0 is returned
            if (contents == EMPTY):
                self.world[x-self.size] = HERO
                self.world[x] = EMPTY
                y=0
                return 0

            # If there is a hole, the hero falls in and a 1 is returned
            elif (contents == HOLE):
                self.world[x-self.size] = DEAD
                self.world[x] = EMPTY
                return 1
            
        # Otherwise nothing happens and a 0 is returned
        return 0


    def moveHeroDown(self):
        x = self.world.index(HERO)
        if(x/self.size != self.size-1):
            contents = self.world[x+self.size]
            if (contents == EMPTY):
                self.world[x+self.size] = HERO
                self.world[x] = EMPTY
                return 0
            elif (contents == HOLE):
                self.world[x+self.size] = DEAD
                self.world[x] = EMPTY
                return 1
        return 0

    def moveHeroLeft(self):
        x = self.world.index(HERO)
        if(x%self.size != 0):
            contents = self.world[x-1]
            if (contents == EMPTY):
                self.world[x-1] = HERO
                self.world[x] = EMPTY
                return 0
            elif (contents == HOLE):
                self.world[x-1] = DEAD
                self.world[x] = EMPTY
                return 1
        return 0


    def moveHeroRight(self):
        x = self.world.index(HERO)
        if(x%self.size != self.size-1):
            contents = self.world[x+1]
            if(contents == EMPTY):
                self.world[x+1] = HERO
                self.world[x] = EMPTY
                return 0
            elif (contents == HOLE):
                self.world[x+1] = DEAD
                self.world[x] = EMPTY
                return 1
        return 0