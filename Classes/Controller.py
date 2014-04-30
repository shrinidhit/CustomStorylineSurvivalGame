from pyglet.window import key
from pyglet.window import mouse
from Items import *
from Menus import *
from Inventory import *
import resources


class Controller():

    def __init__(self, model):
        self.model = model
        self.key_handler = key.KeyStateHandler()
        self.model.window.push_handlers(self.key_handler)
        self.event_handlers = [self, self.key_handler]
        self.mouseX = 0
        self.mouseY = 0

    # checking the key press and tells the player to move right
    def checkKeyPress(self):
        if self.key_handler:
            if self.key_handler[key.LEFT] or self.key_handler[key.A]:
                self.model.player.moveRight()
                # print "Key Pressed!"
            if self.key_handler[key.RIGHT] or self.key_handler[key.D]:
                self.model.player.moveLeft()
                # print "Key Pressed!"
            if self.key_handler[key.UP] or self.key_handler[key.W]:
                self.model.player.moveForward()
                # print "Key Pressed!"
            if self.key_handler[key.DOWN] or self.key_handler[key.S]:
                self.model.player.moveBackward()
                # print "Key Pressed!"
            if self.key_handler[key.SPACE]:
                self.model.player.weapons[0].fire_projectile(
                    self.model.player, self.model.time)
            if self.key_handler[key.LSHIFT]:
                self.model.player.vt = 360
                self.model.player.animRate = .075
            else:
                self.model.player.vt = 160
                self.model.animRate = .15

    def checkMouseMove(self):
        @self.model.window.event
        def on_mouse_motion(x, y, dx, dy):
            self.mouseX = x
            self.mouseY = y

    def checkMouseClick(self):

        @self.model.window.event
        def on_mouse_press(x, y, button, modifiers):

            if button == mouse.LEFT:
                itemClicked = False

                if self.model.contextMenu:
                    # clicking an option in a context menu -> trigger character action
                    for tile in self.model.contextMenu.tiles:
                        tile.on_click(self.model.contextMenu, self.model.player, x, y)
                    # if no item is clicked, close the context menu
                    if not itemClicked:
                       self.model.contextMenu.deconstruct()

                # clicking interactable items -> context menu
                for item in self.model.room.roomItems:
                    if isinstance(item, InteractableItem):
                        item.on_click(model=self.model, x=x, y=y) #if clicked, opens item's context menu of actions
                        if item.clicked:
                           itemClicked = True # keeps track of whether an item is clicked

                # clicking the inventory button -> inventory menu
                self.model.inventoryButton.on_click(model=self.model,x=x, y=y)
                
                if self.model.inventoryMenu:
                    #clicking sprites in the inventory menu
                    if self.model.inventoryButton.clicked:
                        for entry in self.model.inventoryMenu.entries:
                            entry.image.on_click(model=self.model, x=x, y=y)
                    else:
                        self.model.inventoryMenu.deconstruct()

            if button == mouse.RIGHT:
                self.model.player.weapons[1].fire_projectile(
                    self.model.player, self.model.time)

    def update(self):
        self.checkKeyPress()
        self.checkMouseMove()
        self.checkMouseClick()
        self.model.player.set_orientation(self.mouseX, self.mouseY)