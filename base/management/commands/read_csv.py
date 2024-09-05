from django.core.management.base import BaseCommand
import pandas as pd
from base.models import University, Program, Eligibility

class Command(BaseCommand):
    help = 'Load CSV data and interact with the database'

    def handle(self, *args, **kwargs):
        df = pd.read_csv('clean_ncr.csv')
        print(df)