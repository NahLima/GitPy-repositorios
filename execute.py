from webscraping import process_url
from report import generate_report
import json
import sys

sys.stdout = open("exportRepository.txt", "w")

if __name__ == '__main__':
    #tree = process_url('NahLima/API-REST---EXPRESS---MYSQL-')
    tree = process_url('vivadecora/desafio-backend-trabalhe-conosco')
    generate_report('vivadecora/desafio-backend-trabalhe-conosco', tree)

# retorna tudo no console 
sys.stdout.close()

