#!/usr/bin/env python
import os,sys

# Paths on the live server
sys.path.append('/srv/www/app_name/app_name/')
sys.path.append('/srv/www/app_name/app_name/app_name/')
sys.path.append('/srv/config/')
sys.path.append('/srv/')

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app_name.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
