class Component:
    def __init__(self, name=""):
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

    @property
    def name(self) -> str:
        return self._name
    
    def __str__(self) -> str:
        raise NotImplementedError()

    @name.setter
    def name(self, name):
        if name is None:
            raise ValueError('Component.name must not be None')
        
        elif name == "":
            raise ValueError('Component.name must not be empty')
        
        self._name = name

