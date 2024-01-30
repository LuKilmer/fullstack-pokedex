import re
import time
import os
import shutil
import pickle
from classes.Repository import Repository



try:
    
    tempo_inicio = time.time()
    repo = Repository()
    
   
    repo.load_names_by_json()

        

    tempo_decorrido = time.time() - tempo_inicio
    print(f'Terminado! com o tempo de {tempo_decorrido:.5f}')

except Exception as e:
    print(e.args)

