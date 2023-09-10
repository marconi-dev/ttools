import sys
import os
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from _screen.screen import Screen
from _components.components import Component


class MyComponent(Component):
    """Multiline component"""

    def get_body(self):
        return "||====||\n||    ||\n||====||"


class MyComponent2(Component):
    """Single line component"""

    def get_body(self): 
        return '<Component/>'


class MyScreen(Screen):
    def get_body(self):
        return 


class TestScreen(TestCase):

    def redirectIO(self):
        sys.stdout = StringIO()

    def test_total_height(self):
        self.redirectIO()
        screen: MyScreen = MyScreen()
        self.assertEqual(screen.components_total_height, 0)

        with patch('os.system', side_effect=lambda x: None):
            screen.add_component(MyComponent2(name='a'))
            self.assertEqual(screen.components_total_height, 1)

    def test_render(self):
        with patch('os.system', side_effect=lambda x: None):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                MyScreen().add_component(MyComponent2(name='a'))
                self.assertEqual(
                    mock_stdout.getvalue(),
                    "<Component/>\n\n"
                )

    def test_render_with_multiple_lines_conponent(self):
        with patch('os.system', side_effect=lambda x: None):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                MyScreen().add_component(MyComponent(name='a'))
                self.assertEqual(
                    mock_stdout.getvalue(),
                    "||====||\n||    ||\n||====||\n\n"
                )
    
    def test_center_with_multiple_lines_component(self):
        width = os.get_terminal_size().columns
        center_str =  "||====||".ljust(width, " ")
        center_str += "||    ||".ljust(width, " ")
        center_str += "||====||".ljust(width, " ") + "\n\n"

        screen: MyScreen = MyScreen(style={'center': True})

        with patch('os.system', side_effect=lambda x: None):
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                screen.add_component(MyComponent(name='a'))
                self.assertEqual(mock_stdout.getvalue(), center_str)
    
    def test_cover(self):
        t_input_heigth = 2
        t_height = os.get_terminal_size().lines
        screen: MyScreen = MyScreen(style={'cover': True})

        self.assertEqual(
            len(screen.vertical_alignment()),
            t_height - t_input_heigth
        )

    def test_cover_with_components(self):
        t_input_heigth = 2
        t_height = os.get_terminal_size().lines
        screen: MyScreen = MyScreen(style={'cover': True})
        component: MyComponent = MyComponent(name='a')
        screen.components['a'] = component

        self.assertEqual(
            len(screen.vertical_alignment()),
            t_height - t_input_heigth - component.height
        )

    def test_cover_with_height(self):
        screen: MyScreen = MyScreen({'cover': True, 'height': 100})
        self.assertEqual(len(screen.vertical_alignment()), 98)
