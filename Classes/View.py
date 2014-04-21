# View
from Item import Item
from Inventory import Inventory
from Actor import Actor
from ButtonTile import ButtonTile
import resources
import rabbyt
import pyglet


class View():

    def __init__(self, model):
        self.model = model
        self.window = self.model.window
        self.blackout = pyglet.sprite.Sprite(resources.blackout, x=800, y=450)
        self.blackout.opacity = 0
	

    def fade_to_black(self):
        self.blackout.opacity += .01

    def update(self):
        self.window.clear()
        self.fade_to_black()
        # self.model.room.background.render()
        self.model.inventoryButton.render()
        self.model.inventoryButton.label.draw()

        for projectile in self.model.projectiles:
            projectile.render()

        for sprite in self.model.spritesOnScreen:
            sprite.render()
	
	    self.display_context_menu(self.model.spritesOnScreen)
        self.blackout.draw()

    def display_context_menu(self, sprites):
        self.model.contextMenu.button_tiles = []
        for sprite in sprites:
            if isinstance(sprite, Item) and not isinstance(sprite,Actor):
                if sprite.open:
                    self.model.contextMenu.item = sprite
                    start_x = sprite.x + 2*sprite.bounding_radius
                    start_y = sprite.y + 2*sprite.bounding_radius
                    for i in range(len(sprite.actions)):
                        next_x = start_x
                        next_y = start_y + i * resources.silverBox.height 
                        self.model.contextMenu.button_tiles.append(ButtonTile(sprite.actions[i],x=next_x, y=next_y))
        
        for i in range(len(self.model.contextMenu.button_tiles)):
            self.model.contextMenu.button_tiles[i].render()
            self.model.contextMenu.button_tiles[i].label.draw()
