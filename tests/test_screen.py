import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from _screen.screen import Screen
from _components.components import Component


class MyComponent(Component):
    def __str__(self): 
        return '<Component />'


class TestComponent(TestCase):
    def redirectIO(self):
        sys.stdout = StringIO()

    def test_component_is_valid_fail(self):
        self.redirectIO()
        screen: Screen = Screen()

        with self.assertRaises(ValueError):
            """Must be an instance of Component"""
            screen.component_is_valid('hello')
        
        with self.assertRaises(ValueError):
            """Must be an instance of Component"""
            screen.component_is_valid(None)

        with patch('os.system', side_effect=lambda x: None):
            with self.assertRaises(ValueError):
                """Cannot add 2 components with the same name"""
                screen.add_component(MyComponent(name='comp'))
                screen.add_component(MyComponent(name='comp'))
    
    def test_component_is_valid(self):
        screen: Screen = Screen()
        my_component: MyComponent = MyComponent(name='MyComponent')
        self.assertTrue(screen.component_is_valid(my_component))

    def test_render(self):
        screen: Screen = Screen()
        component: MyComponent = MyComponent(name='a')
        
        with patch('os.system', side_effect=lambda x: None):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                screen.add_component(component)
                self.assertEqual(
                    mock_stdout.getvalue(),
                    "<Component />\n"
                )
