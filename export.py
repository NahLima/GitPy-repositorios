from execute import main

import json


with open('repositoriesExport.txt', 'w') as file:
   for valor in main:
        file.write(str(valor))
