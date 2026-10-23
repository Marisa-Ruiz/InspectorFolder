import tempfile
import unittest
from pathlib import Path


class DuplicatorTest(unittest.TestCase):
    self.temp_dir = tempfile.TemporaryDirectory()
    self.folder_path = Path(self.temp_dir.name)