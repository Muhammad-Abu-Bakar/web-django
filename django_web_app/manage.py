#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_web_app.settings')

    if 'runserver' in sys.argv:
        # Check if a port number is provided
        if len(sys.argv) > 2:
            port = sys.argv[2]
        else:
            port = '8000'  # Default port

        # Adjust the runserver command to include the port
        sys.argv[2] = port

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
