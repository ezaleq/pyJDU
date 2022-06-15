import arcade
import pyglet

from src.resolution_tk import Form
from src.views import TitleView


class Game:
    game_window: arcade.Window

    def setup(self, width: int, height: int, fullscreen: bool):
        self.game_window = arcade.Window(width=width,
                                         height=height,
                                         center_window=True,
                                         fullscreen=fullscreen,
                                         title="Jagger Dress Up")
        # image = pyglet.image.load('resources\cursor.png')
        # cursor = pyglet.window.ImageMouseCursor(image, 0, 0)
        # self.game_window.set_mouse_cursor(cursor)
        # self['cursor']='@cursor.cur'

    def run(self):
        arcade.set_background_color((255, 181, 253))
        title_view = TitleView()
        self.game_window.show_view(title_view)
        title_view.setup()
        self.game_window.run()


if __name__ == "__main__":
    form = Form()
    form.mainloop()
    if not form.good_close:
        exit()
    game = Game()
    game.setup(**form.get_data())
    game.run()
