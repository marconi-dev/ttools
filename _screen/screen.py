import os


class ComponentHandler:
    def __init__(self):
        self.components = {}
    
    @property
    def components_total_height(self):
        return sum([
            component.height 
            for component in self.components.values()
        ])

    def add_component(self, component):
        self.components[component.name] = component
        self.render()
    
    def remove_component(self, name):
        del self.components[name]
        self.render()

    def replace_component(self, name, component, render=True):
        self.components[name] = component

        if render:
            self.render()

    def render(self):
        raise NotImplementedError()


class Screen(ComponentHandler):
    def __init__(self, style={}):
        super().__init__()
        self.style = self.get_style(style)
    
    def get_style(self, values: dict):
        return {
            'height': values.get('height', os.get_terminal_size().lines),
            'width': values.get('width', os.get_terminal_size().columns),
            'center': values.get('center', False),
            'cover': values.get('cover', False)
        }
        

    def get_centered_component(self, component):
        """
        Left align the component string with the screen width.
        Once component and screen have the same width, center then.
        """
        centered_component = ""
        t_width = os.get_terminal_size().columns

        for line in str(component).splitlines():
            padded_component = line.ljust(self.style['width'])
            centered_component += padded_component.center(t_width)

        return centered_component

    
    def horizontal_alignment(self):
        if self.style['center']:
            return [
                self.get_centered_component(component) 
                for component in self.components.values()
            ]

        return [str(component) for component in self.components.values()]

    def vertical_alignment(self):
        if self.style['cover']:
            cover_height = (
                self.style['height'] -
                self.components_total_height -
                2
            )
            return "\n"*cover_height
        return ""

    def render(self):
        os.system('clear')

        for comp in self.horizontal_alignment():
            print(comp)
        
        print(self.vertical_alignment())
