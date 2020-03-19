import pygame as pg
import string


class TextBox(object):
    def __init__(self, rect, **kwargs):
        '''
        Optional kwargs and their defaults:
            "id" : None,
            "command" : None,
                function to execute upon enter key
                Callback for command takes 2 args, id and final (the string in the textbox)
            "active" : True,
                textbox active on opening of window
            "color" : pg.Color("white"),
                background color
            "font_color" : pg.Color("black"),
            "outline_color" : pg.Color("black"),
            "outline_width" : 2,
            "active_color" : pg.Color("blue"),
            "font" : pg.font.Font(None, self.rect.height+4),
            "clear_on_enter" : False,
                remove text upon enter
            "inactive_on_enter" : True
            "blink_speed": 500
                prompt blink time in milliseconds
            "delete_speed": 500
                backspace held clear speed in milliseconds

        Values:
            self.rect = pg.Rect(rect)
            self.buffer = []
            self.final = None
            self.rendered = None
            self.render_rect = None
            self.render_area = None
            self.blink = True
            self.blink_timer = 0.0
            self.delete_timer = 0.0
            self.accepted = string.ascii_letters+string.digits+string.punctuation+" "
        '''
        self.rect = pg.Rect(rect)
        self.buffer = []
        self.final = None
        self.rendered = None
        self.render_rect = None
        self.render_area = None
        self.blink = True
        self.blink_timer = 0.0
        self.delete_timer = 0.0
        self.accepted = string.ascii_letters + string.digits + string.punctuation + " "
        self.process_kwargs(kwargs)

    def process_kwargs(self, kwargs):
        defaults = {"id": None,
                    "command": None,
                    "active": True,
                    "color": pg.Color("white"),
                    "font_color": pg.Color("black"),
                    "outline_color": pg.Color("black"),
                    "outline_width": 2,
                    "active_color": pg.Color("blue"),
                    "font": pg.font.Font(None, self.rect.height + 4),
                    "clear_on_enter": False,
                    "inactive_on_enter": True,
                    "blink_speed": 500,
                    "delete_speed": 75}
        for kwarg in kwargs:
            if kwarg in defaults:
                defaults[kwarg] = kwargs[kwarg]
            else:
                raise KeyError("TextBox accepts no keyword {}.".format(kwarg))
        self.__dict__.update(defaults)

    def get_event(self, event, mouse_pos=None):
        ''' Call this on your event loop

            for event in pg.event.get():
                TextBox.get_event(event)
        '''
        if event.type == pg.KEYDOWN and self.active:
            if event.key in (pg.K_RETURN, pg.K_KP_ENTER):
                self.execute()
            elif event.key == pg.K_BACKSPACE:
                if self.buffer:
                    self.buffer.pop()
            elif event.unicode in self.accepted:
                self.buffer.append(event.unicode)
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if not mouse_pos:
                mouse_pos = pg.mouse.get_pos()
            self.active = self.rect.collidepoint(mouse_pos)

    def execute(self):
        if self.command:
            self.command(self.id, self.final)
        self.active = not self.inactive_on_enter
        if self.clear_on_enter:
            self.buffer = []

    def switch_blink(self):
        if pg.time.get_ticks() - self.blink_timer > self.blink_speed:
            self.blink = not self.blink
            self.blink_timer = pg.time.get_ticks()

    def update(self):
        '''
        Call once on your main game loop
        '''
        new = "".join(self.buffer)
        if new != self.final:
            self.final = new
            self.rendered = self.font.render(self.final, True, self.font_color)
            self.render_rect = self.rendered.get_rect(x=self.rect.x + 2,
                                                      centery=self.rect.centery)
            if self.render_rect.width > self.rect.width - 6:
                offset = self.render_rect.width - (self.rect.width - 6)
                self.render_area = pg.Rect(offset, 0, self.rect.width - 6,
                                           self.render_rect.height)
            else:
                self.render_area = self.rendered.get_rect(topleft=(0, 0))
        self.switch_blink()
        self.handle_held_backspace()

    def handle_held_backspace(self):
        if pg.time.get_ticks() - self.delete_timer > self.delete_speed:
            self.delete_timer = pg.time.get_ticks()
            keys = pg.key.get_pressed()
            if keys[pg.K_BACKSPACE]:
                if self.buffer:
                    self.buffer.pop()

    def draw(self, surface):
        '''
        Call once on your main game loop
        '''
        outline_color = self.active_color if self.active else self.outline_color
        outline = self.rect.inflate(self.outline_width * 2, self.outline_width * 2)
        surface.fill(outline_color, outline)
        surface.fill(self.color, self.rect)
        if self.rendered:
            surface.blit(self.rendered, self.render_rect, self.render_area)
        if self.blink and self.active:
            curse = self.render_area.copy()
            curse.topleft = self.render_rect.topleft
            surface.fill(self.font_color, (curse.right + 1, curse.y, 2, curse.h))


class Button(object):
    def __init__(self, rect, command, **kwargs):
        self.rect = pg.Rect(rect)
        self.command = command
        self.clicked = False
        self.hovered = False
        self.hover_text = None
        self.clicked_text = None
        self.process_kwargs(kwargs)
        self.render_text()

    def process_kwargs(self, kwargs):
        settings = {
            "color": pg.Color('red'),
            "text": None,
            "font": None,  # pg.font.Font(None,16),
            "call_on_release": True,
            "hover_color": None,
            "clicked_color": None,
            "font_color": pg.Color("white"),
            "hover_font_color": None,
            "clicked_font_color": None,
            "click_sound": None,
            "hover_sound": None,
            'border_color': pg.Color('black'),
            'border_hover_color': pg.Color('yellow'),
            'disabled': False,
            'disabled_color': pg.Color('grey'),
            'radius': 3,
        }
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("{} has no keyword: {}".format(self.__class__.__name__, kwarg))
        self.__dict__.update(settings)

    def render_text(self):
        if self.text:
            if self.hover_font_color:
                color = self.hover_font_color
                self.hover_text = self.font.render(self.text, True, color)
            if self.clicked_font_color:
                color = self.clicked_font_color
                self.clicked_text = self.font.render(self.text, True, color)
            self.text = self.font.render(self.text, True, self.font_color)

    def get_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.on_release(event)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True
            if not self.call_on_release:
                self.function()

    def on_release(self, event):
        if self.clicked and self.call_on_release:
            # if user is still within button rect upon mouse release
            if self.rect.collidepoint(pg.mouse.get_pos()):
                self.command()
        self.clicked = False

    def check_hover(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
                if self.hover_sound:
                    self.hover_sound.play()
        else:
            self.hovered = False

    def draw(self, surface):
        color = self.color
        text = self.text
        border = self.border_color
        self.check_hover()
        if not self.disabled:
            if self.clicked and self.clicked_color:
                color = self.clicked_color
                if self.clicked_font_color:
                    text = self.clicked_text
            elif self.hovered and self.hover_color:
                color = self.hover_color
                if self.hover_font_color:
                    text = self.hover_text
            if self.hovered and not self.clicked:
                border = self.border_hover_color
        else:
            color = self.disabled_color

        # if not self.rounded:
        #    surface.fill(border,self.rect)
        #    surface.fill(color,self.rect.inflate(-4,-4))
        # else:
        if self.radius:
            rad = self.radius
        else:
            rad = 0
        self.round_rect(surface, self.rect, border, rad, 1, color)
        if self.text:
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text, text_rect)

    def round_rect(self, surface, rect, color, rad=20, border=0, inside=(0, 0, 0, 0)):
        rect = pg.Rect(rect)
        zeroed_rect = rect.copy()
        zeroed_rect.topleft = 0, 0
        image = pg.Surface(rect.size).convert_alpha()
        image.fill((0, 0, 0, 0))
        self._render_region(image, zeroed_rect, color, rad)
        if border:
            zeroed_rect.inflate_ip(-2 * border, -2 * border)
            self._render_region(image, zeroed_rect, inside, rad)
        surface.blit(image, rect)

    def _render_region(self, image, rect, color, rad):
        corners = rect.inflate(-2 * rad, -2 * rad)
        for attribute in ("topleft", "topright", "bottomleft", "bottomright"):
            pg.draw.circle(image, color, getattr(corners, attribute), rad)
        image.fill(color, rect.inflate(-2 * rad, 0))
        image.fill(color, rect.inflate(0, -2 * rad))

    def update(self):
        # for completeness
        pass


pg.init()
screen = pg.display.set_mode((600, 400))
done = False


def name_on_enter(id, final):
    print('enter pressed, username is "{}"'.format(final))


def pass_on_enter(id, final):
    print('enter pressed, password is "{}"'.format(final))


username_settings = {
    "command": name_on_enter,
    "inactive_on_enter": False,
}
password_settings = {
    "command": pass_on_enter,
    "inactive_on_enter": False,
}
btn_settings = {
    "clicked_font_color": (0, 0, 0),
    "hover_font_color": (205, 195, 100),
    'font': pg.font.Font(None, 16),
    'font_color': (255, 255, 255),
    'border_color': (0, 0, 0),
}

name_entry = TextBox(rect=(70, 100, 150, 30), **username_settings)
pass_entry = TextBox(rect=(70, 200, 150, 30), **password_settings)
tbs = [name_entry, pass_entry]


def get_textboxes(username, password):
    print('button pressed, username is "{}"'.format(username))
    print('button pressed, password is "{}"'.format(password))


btn = Button(rect=(70, 300, 105, 25), command=lambda: get_textboxes(name_entry.final, pass_entry.final), text='OK',
             **btn_settings)

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        for tb in tbs:
            tb.get_event(event)
        btn.get_event(event)
    for tb in tbs:
        tb.update()
        tb.draw(screen)
    btn.draw(screen)
    pg.display.update()