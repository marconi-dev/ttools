import os
from _components.components import Component


class ComponentHandler:
    def __init__(self):
        self.components = {}
    
    @property
    def components_total_height(self):
        return sum([
            component.height 
            for component in self.components.values()
        ])

    def component_is_valid(self, component) -> bool:
        if not isinstance(component, Component):
            raise ValueError(f"{component}")

        comp_with_same_name = list(filter(
            lambda comp: component.name in comp, self.components
        ))

        if len(comp_with_same_name) > 0:
            raise ValueError(f"{component}")

        return True

    def add_component(self, component):
        self.component_is_valid(component)
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
        center_component = "".join([
            line.ljust(self.style['width']) 
            for line in str(component).splitlines()
        ])
        center_component = center_component.center(
            os.get_terminal_size().columns
        )
        return center_component
    
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
                os.get_terminal_size().lines -
                self.components_total_height -
                2
            )
            return "\n"*cover_height
        return ""

    def render(self):
        comp_str_list = self.horizontal_alignment()
        vertical_alignment = self.vertical_alignment()

        os.system('clear')

        for comp in comp_str_list:
            print(comp)
        
        print(vertical_alignment)
