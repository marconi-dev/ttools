import os
from _components.components import Component


class Screen:
    def __init__(self):
        self.components = {}

    def add_component(self, component: type[Component]):

        if not isinstance(component, Component):
            raise ValueError(f"{component}")

        self.components[component.name] = component

        self.render()
    
    def remove_component(self):
        self.render()

    def replace_component(self):
        self.render()


    def render(self):
        os.system('clear')

        for component in self.components.values():
            print(str(component))

        pass
