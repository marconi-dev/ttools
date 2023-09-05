from unittest import TestCase
from _components.components import Component


class TestComponent(TestCase):
    def test_component_without_name(self):
        with self.assertRaises(ValueError): 
            Component()

    def test_component_with_None_as_name(self):
        with self.assertRaises(ValueError):
            Component(name=None)

    def test_component_name(self):
        name = 'Component'
        component: Component = Component(name=name)
        self.assertEqual(component.name, name)
    
    def test_string_representation_not_implemented(self):
        component: Component = Component(name='Component')
        with self.assertRaises(NotImplementedError):
            print(component)
    
    def test_component_height(self):
        class MyComponent(Component):
            def __str__(self) -> str:
                return 'Hello,\n World!'

        my_component: MyComponent = MyComponent(name='MyComponent')

        self.assertEqual(my_component.height, 2)

    def test_component_width(self):
        class MyComponent(Component):
            def __str__(self) -> str:
                return 'small Line\nLargest Line\n123\nloveU'

        largest_line_len = len('Largest Line')
        my_component: MyComponent = MyComponent(name='MyComponent')
        self.assertEqual(my_component.width, largest_line_len)
    
    def test_component_with_with_f_strings(self):
        class MyComponent(Component):
            def __str__(self) -> str:
                return f'olá\n{" "*100}\nlinha\nline'

        my_component: MyComponent = MyComponent(name='MyComponent')
        self.assertEqual(my_component.width, 100)
