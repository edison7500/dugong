"""
 Prints CSV of all fields of a model.
"""

import csv
import logging
import sys

from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Output the specified model as CSV"

    def add_arguments(self, parser):
        parser.add_argument("model", type=str)

    def handle(self, *args, **options):
        from django.apps import apps

        app_name, model_name = options["model"].split(".")
        model = apps.get_model(app_name, model_name)
        field_names = [f.name for f in model._meta.fields]
        writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
        writer.writerow(field_names)
        for instance in model.objects.all():
            writer.writerow([getattr(instance, f) for f in field_names])
