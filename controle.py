from Apresentacao.interacao import Interacao
from Dominio.Assistente.assistente import Assistente

import pyttsx3
           

if __name__ == '__main__':
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    print('listening...')
    while True:
        response = Assistente.run()
        if response == "quit program":
            break
        Interacao.talk(engine,response)
