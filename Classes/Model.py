from Character import Character
from Room import Room
from Base import Base
import resources


class Model():  # sets window and player

    def __init__(self, window):
        self.window = window
        self.player = Character(
            texture=resources.playerImage, x=300, y=400)
        self.mapSizeX = 3
        self.mapSizeY = 3
        self.baseCoordinate = (self.mapSizeX / 2, self.mapSizeY / 2)
        self.createMap()
        self.roomCoordinate = self.baseCoordinate
        self.room = self.map[self.roomCoordinate]
        self.spritesOnScreen = self.room.roomItems
        self.spritesOnScreen.append(self.player)

    def createMap(self):
        self.map = {}
        for row in xrange(0, self.mapSizeX):
            for column in xrange(0, self.mapSizeY):
                if row == self.baseCoordinate[0] and column == self.baseCoordinate[1]:
                    self.map.update(
                        {(row, column): Base(self.window.height, self.window.width)})
                else:
                    self.map.update(
                        {(row, column): Room(self.window.height, self.window.width)})

    def update(self, dt):

        for sprite in self.spritesOnScreen:
            sprite.update(dt)

        if self.player.enteringRoom:
            # print "Old Room Coordinate: " + str(self.roomCoordinate)
            if self.player.newRoom == "up":
                # print "Trying to Move Up"
                if self.roomCoordinate[1] > 0:
                    self.roomCoordinate = (
                        self.roomCoordinate[0], self.roomCoordinate[1] - 1)
                    self.player.enterNewRoom()
            elif self.player.newRoom == "down":
                # print "Trying to Move down"
                if self.roomCoordinate[1] < self.mapSizeY - 1:
                    self.roomCoordinate = (
                        self.roomCoordinate[0], self.roomCoordinate[1] + 1)
                    self.player.enterNewRoom()
            elif self.player.newRoom == "right":
                # print "Trying to Move Right"
                if self.roomCoordinate[0] < self.mapSizeX - 1:
                    self.roomCoordinate = (
                        self.roomCoordinate[0] + 1, self.roomCoordinate[1])
                    self.player.enterNewRoom()
            elif self.player.newRoom == "left":
                # print "Trying to Move Left"
                if self.roomCoordinate[0] > 0:
                    self.roomCoordinate = (
                        self.roomCoordinate[0] - 1, self.roomCoordinate[1])
                    self.player.enterNewRoom()

            # print "New Room Coordinate: " + str(self.roomCoordinate)
            self.room = self.map[self.roomCoordinate]
            # print self.room
            self.spritesOnScreen = self.room.roomItems
            self.spritesOnScreen.append(self.player)
            # print self.spritesOnScreen
