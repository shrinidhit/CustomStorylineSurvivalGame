from pyglet.window import key


class Controller():

    def __init__(self, model):
        self.model = model
        self.key_handler = key.KeyStateHandler()
        self.model.window.push_handlers(self.key_handler)
        self.event_handlers = [self, self.key_handler]

    # checking the key press and tells the player to move right
    def checkKeyPress(self):
        if self.key_handler:
            if self.key_handler[key.LEFT]:
                self.model.player.moveLeft()
                # print "Key Pressed!"
            if self.key_handler[key.RIGHT]:
                self.model.player.moveRight()
                # print "Key Pressed!"
            if self.key_handler[key.UP]:
                self.model.player.moveForward()
                # print "Key Pressed!"
            if self.key_handler[key.DOWN]:
                self.model.player.moveBackward()
                # print "Key Pressed!"

    def checkMouseMove(self):
        pass
