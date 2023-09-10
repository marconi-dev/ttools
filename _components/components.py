class ComponentStyling:
    def __init__(self, screen_style={}, style={}):
        self.screen_style = screen_style
        self.string = self.get_body()
        self.style = self.get_style(style)
        self.apply_margin()
        self.apply_center()
    
    def get_style(self, style):
        margin_dict = {'left': 0, 'right': 0, 'top': 0, 'bottom': 0}

        if style.get('margin'):
            margin_dict = {**margin_dict, **style.get('margin')}
            
        return {
            "center": style.get("center", False),
            "margin": margin_dict
        }

    def apply_margin(self):
        """
        apply margin to every line to the given string representation
        """
        margin_top = self.style['margin']['top']
        margin_left = self.style['margin']['left']
        margin_right = self.style['margin']['right']
        margin_bottom = self.style['margin']['bottom']
        
        new_string = ""
        for line in self.string.splitlines():
            new_string += f"{' '*margin_left}{line}{' '*margin_right}\n"

        self.string = "\n"*margin_top + new_string[:-1] + "\n"*margin_bottom
        

    def apply_center(self):
        if not self.style['center']:
            return
        
        new_string = ""
        for line in self.string.splitlines():
            new_string += line.center(self.screen_style['width']) + '\n'

        self.string = new_string[:-1]

    def get_body(self):
        return ""

    def __str__(self):
        return self.string



class Component(ComponentStyling):
    def __init__(
        self, 
        name="",
        screen_style={},
        style={}
    ):
        self.name = name
        super().__init__(screen_style, style)

    @property
    def height(self) -> int:
        return self.string.count('\n') + 1
    
    @property
    def width(self) -> int:
        largest_line_length = 0
        lines = str(self).splitlines()

        for line in lines:
            line_length = len(line)
            
            if line_length > largest_line_length:
                largest_line_length = line_length

        return largest_line_length
