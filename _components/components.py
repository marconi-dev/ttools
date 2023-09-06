from _screen import screen


class Component:
    def __init__(
        self, 
        name="",
        screen=screen.Screen
    ):
        self.screen = screen
        self.name = name

    @property
    def height(self) -> int:
        return str(self).count('\n') + 1
    
    @property
    def width(self) -> int:
        largest_line_length = 0
        lines = str(self).splitlines()

        for line in lines:
            line_length = len(line)
            
            if line_length > largest_line_length:
                largest_line_length = line_length

        return largest_line_length

    def __str__(self) -> str:
        raise NotImplementedError()
