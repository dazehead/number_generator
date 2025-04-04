import numpy as np
import json

class Num_Generator:
    def __init__(self):
        with open('database.json', 'r') as file:
            data = json.load(file)
            self.count = data['count']

    def get_random_number(self):
        number = int(np.random.randint(1, 100, size=1)[0])
        self.count += 1
        new_data = {
            "count": self.count,
            "number": number
        }
        self.update_count(new_data)
    
    def update_count(self, new_data):
        with open('database.json', 'w') as file:
            json.dump(new_data, file, indent=4)