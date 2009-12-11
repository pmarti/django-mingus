import sys
import os

os.environ['PYTHON_EGG_CACHE'] = '/home/pablo/django/eggs'

# activate virtualenv
activate_this = "/home/pablo/django/virtualenvs/minimoesfuerzo/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

# tell django where our settings module is
sys.path.insert(0, "/home/pablo/django/virtualenvs/minimoesfuerzo/django-mingus")
os.environ['DJANGO_SETTINGS_MODULE'] = 'mingus.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
