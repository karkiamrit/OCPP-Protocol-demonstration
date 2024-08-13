from unittest import TestCase
from fastapi.testclient import TestClient
from nea_backend.app.application import create_application


class TestBaseEventHandler(TestCase):
    def test_startup_handler(self):
        app = create_application()
        with self.assertLogs('nea_backend', level='INFO') as cm:

            with TestClient(app):
                pass
            self.assertEqual(cm.output,
                             ['INFO:nea_backend:Starting up ...',
                              'INFO:nea_backend:Shutting down ...'])
