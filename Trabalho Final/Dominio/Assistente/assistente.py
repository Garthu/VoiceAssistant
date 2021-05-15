import speech_recognition as sr
from Dominio.GerenciaDeFuncoes.operacoes import *

class Assistente:

    def take_command():
        listener = sr.Recognizer()
        command = 'Nothing'
        try:
            with sr.Microphone() as source:
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'alexa' in command:
                    command = command.replace('alexa', '')
        except:
            pass
        return command


    def run():
        while True:
            command = Assistente.take_command()
            if 'play' in command:
                video = TocaVideo.play(command)
                return ('The video: ' + video + ' is currently playing')

            elif 'time' in command:
                hora = Hora.get_time(command)
                return ('Current time is ' + hora)

            elif 'calendar' in command:
                dia = Dia.get_day(command)
                return dia
            
            elif 'save' in command:
                contact = Agenda.save_contact(command)
                return contact

            elif 'search' in command:
                info = Search.wikipedia_search(command)
                return info
            
            elif 'story' in command:
                filmes = Film.filmes(command)
                return filmes
            
            elif 'ratings' in command:
                rate = Film.rating(command)
                return rate

            elif 'joke' in command:
                joke = Joke.make_a_joke(command)
                return joke

            elif 'send message' in command:
                mensagem = SendMessage.send_message(command)
                return ("The message: " + mensagem + " is sent")

            elif 'who are you' in command:
                return ("Hello my name is Alexa your personal Assistant")

            elif 'translate' in command:
                traducao = Translate.translate_phrase(command)
                return traducao
            
            elif 'temperature' in command:
                temperatura = Climate.get_temperature(command)
                return ("The temperature of Florianopolis is " + str(temperatura) + " degrees ceusius")
            
            elif 'climate' in command:
                clima = Climate.get_climate(command)
                return ("The weather of Florianopolis is " + clima)
            
            elif 'money' in command:
                cotacao = Money.dolarCotation(command)
                return cotacao
            
            elif 'euro' in command:
                cotacao = Money.euroCotation(command)
                return cotacao
            
            elif 'speed' in command:
                velocidade = Speed.velocidade(command)
                return velocidade
            
            elif 'news' in command:
                noticias = News.noticias(command)
                return noticias
            
            elif 'lyrics' in command:
                letras = Lyrics.letra(command)
                return letras
            
            elif 'odds' in command:
                odd = Odds.return_odd(command)
                return odd

            elif 'soccer results' in command:
                soccer = Soccer.return_results(command)
                return soccer

            elif 'stocks' in command:
                stocks = Stocks.return_stocks(command)
                return stocks 

            elif 'break' in command:
                exit()
            else:
                return ("Please say the command again.")