import unittest

from application import app

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.app = app()
        self.appctx = self.app.app_context()
        self.appctx.push()

    def tearDown(self):
        self.appctx.pop()
        self.app = None
        self.appctx = None

    def test_app(self):
        assert self.app is not None
        assert app == self.app