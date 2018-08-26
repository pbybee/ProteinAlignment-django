#!/bin/bash

#python manage.py collectstatic
python /web/manage.py migrate --run-syncdb
#python /web/manage.py test
/usr/local/bin/gunicorn proteinAlignSite.wsgi:application -w 2 -b :8000
