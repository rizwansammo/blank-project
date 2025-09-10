#!/usr/bin/env python
import os
import sys

def main():
    """Run administrative tasks."""
    settings_module = os.environ.get("DJANGO_SETTINGS_MODULE")
    if not settings_module:
        env = os.environ.get("ENV", "dev").lower()
        if env == "prod":
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_site.settings.prod")
        else:
            os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_site.settings.dev")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)

if __name__ == "__main__":
    main()