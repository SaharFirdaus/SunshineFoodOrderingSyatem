import os
import sys

path=os.path.expanduser('~/django_projects/Online_Food_Ordering_System/Online_Food_Ordering_System')
if path not in sys.path:
    sys.path.insert(0,path)
os.environ['DJANGO_SETTINGS_MODULE']='Foods_Ordering.settings'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())


















