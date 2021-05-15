import pywhatkit
import pyjokes
import wikipedia
from googletrans import Translator
import datetime
import datetime as dt
import pyowm
import requests
from requests import get
from bs4 import BeautifulSoup as bs
import speedtest
import json 
import random
from urllib.request import urlopen
from BancoDeDados.agenda import Db
from vagalume import lyrics
import smtplib
from soccerapi.api import Api888Sport
from soccer_data_api import SoccerDataAPI

def filtro(command,deletion):
    lista = list(command.split(" "))
    stopwords = ["translate","plot","ratings","lyrics"]
    stopwords.append(deletion)
    for word in list(lista):
        if word in stopwords:
            lista.remove(word)
    comando = ' '.join(str(e) for e in lista)
    return comando

class Contato:
    def __init__(self,nome,telefone):
        self.__nome = nome
        self.__telefone = telefone
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        self.__nome = nome

    def get_telefone(self):
        return self.__telefone
    
    def set_telefone(self,telefone):
        self.__telefone = telefone


class Operacao:
    def __init__(self,nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self,nome):
        self.__nome = nome

class Agenda(Operacao):
    def __init__(self,nome):
        super().__init__(nome)
    
    def save_contact(command):
        contact_number = ""
        nome = ""
        command = filtro(command,"save")
        for word in command:
            if word.isnumeric():
                contact_number += word
            elif word != " ":
                nome += word
        contato = Contato(nome,contact_number)
        database = Db()
        database.create_tables()
        sucess = database.insert_person(contato)
        if sucess == 0:
            return("The user has already been registered")
        else:
            return ("The contact from %s has been saved with sucess" % nome)
        
    
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
        whatsmessage = filtro(command,"send")
        whatsmessage = filtro(whatsmessage,"message")
        nome = ""
        for word in whatsmessage:
            if word == " ":
                break
            else:
                nome += word
        print(nome)
        database = Db()
        numero = ("+" + database.get_contato(nome)[0])
        print(numero)
        pywhatkit.sendwhatmsg(numero,whatsmessage[len(nome):],dt.datetime.now().hour,(dt.datetime.now().minute)+1)
        
        return whatsmessage[len(nome):]

class Climate(Operacao):
    def __init__(self,nome):
        super().__init__(nome)
    
    def get_temperature(command):
        owm = pyowm.OWM('38faf23199e7eefeb22681e7083922d6')
        city = 'Florianopolis'
        loc = owm.weather_manager().weather_at_place(city)
        weather = loc.weather
        temp = weather.temperature(unit='celsius')
        return temp["temp"]
    
    def get_climate(command):
        owm = pyowm.OWM('38faf23199e7eefeb22681e7083922d6')
        city = 'Florianopolis'
        loc = owm.weather_manager().weather_at_place(city)
        weather = loc.weather
        clima = weather.detailed_status
        return clima

class Translate(Operacao):
    def __init__(self,nome):
        super().__init__(nome)

    def translate_phrase(command):
        translator = Translator()
        translation = command.replace('Translating', '')
        if 'spanish' in command:
            translated = translator.translate(filtro(translation,"spanish"), src='en', dest='es')
        elif 'portuguese' in command:
            translated = translator.translate(filtro(translation,"portuguese"), src='en', dest='pt')
        elif 'russian' in command:
            translated = translator.translate(filtro(translation,"russian"), src='en', dest='ru')
        
        return translated.text

class Money(Operacao):
    def __init__(self,nome):
        super().__init__(nome)
    
    def dolarCotation(command):
        url = get('https://www.remessaonline.com.br/cotacao/cotacao-dolar')
        soup = bs(url.text, 'html.parser')
        dolar = soup.find('div', {'class': 'style__Text-sc-15flwue-2 cSuXFv'}).text[0:4]
        dolar = dolar.replace(',','.')
        dolar = float(dolar)
        dolar = round(dolar,2)
        return ("The Dolar-Real cotation of today is %.2f Reais"%dolar)

    def euroCotation(command):
        url = get('https://www.remessaonline.com.br/cotacao/cotacao-euro')
        soup = bs(url.text, 'html.parser')
        euro = soup.find('div', {'class': 'style__Text-sc-15flwue-2 cSuXFv'}).text[0:4]
        euro = euro.replace(',','.')
        euro = float(euro)
        euro = round(euro,2)
        return ("The Euro-Real cotation of today is %.2f Reais"%euro)
    
class Speed(Operacao):
    def __init__(self,nome):
        super().__init__(nome)
    
    def velocidade(command):
        speed = speedtest.Speedtest()
        download = speed.download()
        upload = speed.upload()
        return ("Your current download speed is %.2f Mbits"%(download/1000000))

class News(Operacao):
    def __init__(self,nome):
        super().__init__(nome)
    
    def noticias(command):
        r = requests.get("https://newsapi.org/v2/top-headlines?country=br&apiKey=4bd9187099e749659913e9cad9f73949")
        #Pode ser br ou us
        data = json.loads(r.content)
        news = data['articles'][random.randint(1,15)]['title']
        return (news)

class Film(Operacao):
    def __init__(self,nome):
        super().__init__(nome)
    
    def filmes(command):
        filme = command.replace('Seaching', '')
        filme_filtrado = filtro(filme,"story")
        add = filme_filtrado.replace(" ","+")
        url = "http://www.omdbapi.com/?t="+add+"&apikey=39b88076&plot=full"
        dados = urlopen(url).read()
        dados_p = json.loads(dados)
        return (dados_p["Title"] + ":" + dados_p["Plot"])
    
    def rating(command):
        filme = command.replace('Seaching', '')
        filme_filtrado = filtro(filme,"plot")
        add = filme_filtrado.replace(" ","+")
        url = "http://www.omdbapi.com/?t="+add+"&apikey=39b88076&plot=full"
        dados = urlopen(url).read()
        dados_p = json.loads(dados)
        dados_novos = dados_p["Ratings"]
        return ("The rating for: " + dados_p["Title"] + " is " + dados_novos[0]["Value"])
    
class Lyrics(Operacao):
    def __init__(self,nome):
        super().__init__(nome)
    
    def letra(command):
        artist_name = ""
        song_name = ""
        command = filtro(command,lyrics)
        for word in command:
            if word == " ":
                break
            else:
                artist_name += word
        command = filtro(command,artist_name)
        
        for word in command:
            if word == " ":
                break
            else:
                song_name += word
        command = filtro(command,song_name)
        
        result = lyrics.find(artist_name, song_name)

        if result.is_not_found():
            return ("Song not found")
        else:
            print(result.song.lyric)
            return("Here is the lyrics for: " + result.song.name + " of " + result.artist.name)

class Odds(Operacao):
    def __init__(self,nome):
        super().__init__(nome)

    def return_odd(command):
        api = Api888Sport()
        tournments = api.competitions()
        url = ''
        if 'champions league' in command:
            url = tournments['Champions League']['Champions League']
        if 'premier league' in command:
            url = tournments['England']['Premier League']
        if 'italian league' in command:
            url = tournments['Italy']['Serie A']
        if 'french league' in command:
            url = tournments['France']['Ligue 1']
        if 'german league' in command:
            url = tournments['Germany']['Bundesliga']
        if 'spanish league' in command:
            url = tournments['Spain']['La Liga']
        
        odds = api.odds(url)
        num = random.randint(0,(len(odds)-1))
        return("Odds for %s winning is %s and the odds for %s winning is %s"%(odds[num]['home_team'],odds[num]['full_time_result']['1'],odds[num]['away_team'],odds[num]['full_time_result']['2']))

class Soccer(Operacao):
    def __init__(self,nome):
        super().__init__(nome)
    
    def return_results(command):
        soccer_data = SoccerDataAPI()
        if "english" in command:
            teste = soccer_data.english_premier()
            
        elif "italian" in command:
            teste = soccer_data.serie_a()

        elif "german" in command:
            teste = soccer_data.bundesliga()
            
        elif "french" in command:
            teste = soccer_data.ligue_1()
           
        elif "spanish" in command:
            teste = soccer_data.la_liga()

        for i in range(0,5):
            print("%s is the number %s in the rank and has %s points, %s wins and %s losses"%(teste[i]['team'],teste[i]['pos'],teste[i]['points'],teste[i]['wins'],teste[i]['losses']))
        return("The results from the championship is shown above")

class Stocks(Operacao):
    def __init__(self,nome):
        super().__init__(nome)

    def return_stocks(command):
        API_KEY = 'PDOASB41QBCC5J7I'
        COMPANY = ''
        if "apple" in command:
            SYMBOL = "AAPL"
            COMPANY = 'Apple'
        elif 'netflix' in command:
            SYMBOL = "NFLX"
            COMPANY = 'Netflix'
        elif 'microsoft' in command:
            SYMBOL = 'MSFT'
            COMPANY = 'Microsoft'
        else:
            return ("The company is not yet registered in this Virtual Assistant")
        r = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ SYMBOL + '&apikey='+ API_KEY)
        if (r.status_code == 200):
            result = r.json()
            data = result['Time Series (Daily)']
            values_view = data.values()
            value_iterator = iter(values_view)
            first_value = next(value_iterator)
            return("The Company %s is with %s points at this moment and her volume is %s"%(COMPANY,first_value['4. close'],first_value['5. volume']))


        