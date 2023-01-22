import os
from pathlib import Path
import csv
from collections import defaultdict

CSV_FILE_NAME = "rank.csv"

class RankModel(object):
    def __init__(self, csv_file=CSV_FILE_NAME, column = ["name", "count"]):
        self.csv_file = csv_file
        if not os.path.exists(csv_file):
            Path(csv_file).touch()
        self.column = column
        self.data = defaultdict(int)
        self.load_data()
    
        
    def load_data(self):
        with open(self.csv_file, 'r+') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.data[row["name"]] = int(row["count"])
        return self.data
    
        
    def save(self, language_name):
        with open(self.csv_file, 'w+') as f:
            writer = csv.DictWriter(f, fieldnames=self.column)
            writer.writeheader()
            
            self.data[language_name] += 1
            for language_name, count in self.data.items():
                writer.writerow({
                    "name": language_name,
                    "count": count,
                })

            

            
            
