import os
from _components.components import Component


class ComponentHandler:
    def __init__(self):
        self.components = {}

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
    
    def remove_component(self, component):
        self.component_is_valid(component)
        del self.components[component.name]
        self.render()

    def replace_component(self, component):
        self.component_is_valid(component)
        self.components[component.name] = component
        self.render()

    def render(self):
        raise NotImplementedError()


class Screen(ComponentHandler):
    def __init__(
        self, 
        height=os.get_terminal_size().lines,
        width=os.get_terminal_size().columns,
    ):
        super().__init__()
        self.height = height
        self.width = width

    def render(self):
        os.system('clear')

        for component in self.components.values():
            print(str(component))
