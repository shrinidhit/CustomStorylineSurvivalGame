from Character import Character
from Room import Room
from Base import Base
from Enemy import Enemy
import resources
import rabbyt


class Model():  # sets window and player

    def __init__(self, window):
        self.window = window
        self.player = Character(
            texture=resources.playerImage, x=300, y=400)
        self.collisionThreshold = 4
        self.mapSizeX = 3
        self.mapSizeY = 3
        self.baseCoordinate = (self.mapSizeX / 2, self.mapSizeY / 2)
        self.create_map()
        self.roomCoordinate = self.baseCoordinate
        self.room = self.map[self.roomCoordinate]
        self.spritesOnScreen = self.room.roomItems
        self.actorsOnScreen = self.room.enemies
        self.actorsOnScreen.append(self.player)

    def create_map(self):
        self.map = {}
        for row in xrange(0, self.mapSizeX):
            for column in xrange(0, self.mapSizeY):
                if row == self.baseCoordinate[0] and column == self.baseCoordinate[1]:
                    self.map.update(
                        {(row, column): Base(self.window.height, self.window.width)})
                else:
                    self.map.update(
                        {(row, column): Room(self.window.height, self.window.width)})

    def check_collisions(self):
        for actor in self.actorsOnScreen:
            for collision in rabbyt.collisions.aabb_collide_single(actor, self.spritesOnScreen):
                if collision.right - self.collisionThreshold <= actor.left <= collision.right + self.collisionThreshold:
                    actor.collidingLeft = True
                if collision.left - self.collisionThreshold <= actor.right <= collision.left + self.collisionThreshold:
                    actor.collidingRight = True
                if collision.top - self.collisionThreshold <= actor.bottom <= collision.top + self.collisionThreshold:
                    actor.collidingBottom = True
                if collision.bottom - self.collisionThreshold <= actor.top <= collision.bottom + self.collisionThreshold:
                    actor.collidingTop = True

    def change_room(self):
        if self.player.newRoom == "up":
            if self.roomCoordinate[1] > 0:
                self.roomCoordinate = (
                    self.roomCoordinate[0], self.roomCoordinate[1] - 1)
                self.player.enterNewRoom()
        elif self.player.newRoom == "down":
            if self.roomCoordinate[1] < self.mapSizeY - 1:
                self.roomCoordinate = (
                    self.roomCoordinate[0], self.roomCoordinate[1] + 1)
                self.player.enterNewRoom()
        elif self.player.newRoom == "right":
            if self.roomCoordinate[0] < self.mapSizeX - 1:
                self.roomCoordinate = (
                    self.roomCoordinate[0] + 1, self.roomCoordinate[1])
                self.player.enterNewRoom()
        elif self.player.newRoom == "left":
            if self.roomCoordinate[0] > 0:
                self.roomCoordinate = (
                    self.roomCoordinate[0] - 1, self.roomCoordinate[1])
                self.player.enterNewRoom()

        self.room = self.map[self.roomCoordinate]
        self.spritesOnScreen = self.room.roomItems
        self.spritesOnScreen.append(self.player)
        self.actorsOnScreen = self.room.enemies
        self.actorsOnScreen.append(self.player)

    def update(self, dt):
        self.check_collisions()
        for sprite in self.spritesOnScreen:
            if isinstance(sprite, Enemy):
                sprite.update(dt, self.player.x, self.player.y)
            else:
                sprite.update(dt)

        self.player.update(dt)

        if self.player.enteringRoom:
            self.change_room()
