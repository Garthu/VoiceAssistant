import pywhatkit
import pyjokes
import wikipedia
from googletrans import Translator
import datetime
import datetime as dt


class Operacao:
    def __init__(self,nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        self.__nome = nome
    
class TocaVideo(Operacao):
    def __init__(self,nome):
        super().__init__(nome)
    
    def play(command):
        song = command.replace('play', '')
        pywhatkit.playonyt(song)
        
        return song

class Hora(Operacao):
    def __init__(self,nome):
        super().__init__(nome)
    
    def get_time(command):
        time = datetime.datetime.now().strftime('%I:%M %p')
        
        return time

class Dia(Operacao):
    def __init__(self,nome):
        super().__init__(nome)
    
    def get_day(command):
        meses = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        fala = 'Today is day %d of %s'%(dt.datetime.now().day, meses[dt.datetime.now().month-1]) 
        
        return fala

class Search(Operacao):
    def __init__(self,nome):
        super().__init__(nome)
    
    def wikipedia_search(command):
        person = command.replace('Seaching', '')
        info = wikipedia.summary(person, 1)
        
        return info

class Joke(Operacao):
    def __init__(self,nome):
        super().__init__(nome)
    
    def make_a_joke(command):
        
        return pyjokes.get_joke()

class SendMessage(Operacao):
    def __init__(self,nome):
        super().__init__(nome)

    def send_message(command):
        whatsmessage = command.replace('Sending Message', '')
        pywhatkit.sendwhatmsg('+5548991640472',whatsmessage[14:],dt.datetime.now().hour,(dt.datetime.now().minute)+1)
        
        return whatsmessage[14:]



class Translate(Operacao):
    def __init__(self,nome):
        super().__init__(nome)

    def translate_phrase(command):
        translator = Translator()
        translation = command.replace('Translating', '')
        translated = translator.translate(translation[11:], src='en', dest='pt')
        
        return translated.text
