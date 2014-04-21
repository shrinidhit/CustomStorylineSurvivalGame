# View
from Item import Item
from Inventory import Inventory
import resources
import rabbyt
import pyglet


class View():

    def __init__(self, model):
        self.model = model
        self.window = self.model.window
        self.blackout = pyglet.sprite.Sprite(resources.blackout, x=0, y=0)
        self.blackout.opacity = 0

    def fade_to_black(self):
        self.blackout.opacity += .01

    def update(self):
        self.window.clear()
        self.fade_to_black()
        self.model.room.background.render()
        for weapon in self.model.player.weapons:
            for projectile in weapon.projectiles:
                projectile.render()

        for sprite in self.model.spritesOnScreen:
            sprite.render()

        self.blackout.draw()

        if self.model.inventoryGUI.open == True:
            self.model.inventoryGUI.main()
