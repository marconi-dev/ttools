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

    def test_render(self):
        screen: Screen = Screen()
        component: MyComponent = MyComponent(name='a')
        
        with patch('os.system', side_effect=lambda x: None):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                screen.add_component(component)
                self.assertEqual(
                    mock_stdout.getvalue(),
                    "<Component />\n\n"
                )
