import numpy as np
import json

class Num_Generator:
    def __init__(self, database):
        '''initalize class resources'''
        self.database = database
        data = self.database.get_table_from_db()
        self.count = data[0].get('counter')
        print(self.count)

    def get_random_number(self):
        '''generates a random number, saves new data and calls function to update count'''
        number = int(np.random.randint(1, 100, size=1)[0])
        self.count += 1
        new_data = [{
            "counter": self.count,
            "number": number
        }]
        self.database.overwrite_click_metrics(new_data)