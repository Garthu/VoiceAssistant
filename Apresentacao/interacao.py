class Interacao:
    
    def talk(engine,text):
        engine.say(text)
        print(text)
        engine.runAndWait()
        print('listening...')