# File sets up the django environment, used by other scripts that need to
# execute in Django land
# https://realpython.com/installable-django-app/?utm_source=realpython&utm_medium=rss
import sys
from pathlib import Path
import django
from django.conf import settings

BASE_DIR = Path(__file__).parent / "src"
sys.path.insert(0, str(BASE_DIR))

def boot_django():
    settings.configure(
        # ROOT_URLCONF='ExampleProject.urls',
        # SECRET_KEY="NOT-A-REAL-SECRET-KEY-12345",
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        DATABASES={
            "default":{
                "ENGINE":"django.db.backends.sqlite3",
                "NAME": BASE_DIR / "db.sqlite3",
            }
        },
        INSTALLED_APPS=(
            "vintagestory_masterserver",
        ),
        TIME_ZONE="UTC",
        USE_TZ=True,
    )
    django.setup()