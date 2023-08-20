import os, sys
sys.path.insert(0, '/home/s/setet9l4/setet9l4.beget.tech/page_for_girl')
sys.path.insert(1, '/home/s/setet9l4/setet9l4.beget.tech/djangoenv/lib/python3.11/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'page_for_girl.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()