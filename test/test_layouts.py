import importlib
import importlib.util
from pathlib import Path
from unittest import TestCase

from test.util import *

LAYOUTS_DIR_PATH = 'layouts'


class Layout:
    path: str
    layout: List[int]
    transparent: List[int]

    def __init__(self, path: str, layout: List[int], transparent: List[int]) -> None:
        self.layout = layout
        self.transparent = transparent
        self.path = path


class LayoutTest(TestCase):

    def test_layouts(self) -> None:
        for layout in self.get_layouts():
            with self.subTest(layout.path):
                self.assert_layout(layout)

    def get_layouts(self) -> List[Layout]:
        files = self.get_layout_files()
        return list(map(self.load_layout, files))

    def load_layout(self, path: str):
        spec: Any = importlib.util.spec_from_file_location('layout', path)
        layout = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(layout)
        return Layout(
            path,
            layout.layout if hasattr(layout, 'layout') else None,
            layout.transparent if hasattr(layout, 'transparent') else None
        )

    def assert_layout(self, layout: Layout) -> None:
        self.assertIsNotNone(layout.layout)
        self.assertIsNotNone(layout.transparent)
        self.assertEqual(len(layout.layout), len(layout.transparent))

    def get_layout_files(self) -> List[str]:
        return list(map(str, Path(LAYOUTS_DIR_PATH).glob('**/*.py')))
