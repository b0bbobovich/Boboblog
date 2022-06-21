import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Boboblog.settings')

application = get_wsgi_application()
