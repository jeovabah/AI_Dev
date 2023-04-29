import speech_recognition as sr
import nltk
import pygame.mixer
from nltk.tokenize import word_tokenize
from gtts import gTTS
import os

# Inicializando o NLTK
nltk.download('punkt')

# Criando uma instância do Recognizer
r = sr.Recognizer()
# Init pygame mixer
pygame.mixer.init()

index = 0

# Loop para esperar por novas gravações até que a palavra "fim" seja dita
while True:
    # Usando o microfone como fonte de áudio
    with sr.Microphone() as source:
        print("Fale alguma coisa!")
        audio = r.listen(source)

    # Usando o Google Speech Recognition para transcrever o áudio em texto
    try:
        texto = r.recognize_google(audio, language='pt-BR')
        print("Você disse: " + texto)
        
        # Verificando se a palavra "fim" foi dita para finalizar o loop
        if "fim" in texto:
            break
        
        # Tokenizando a sentença
        tokens = word_tokenize(texto, language='portuguese')
        print(tokens)
        
        # Adicione aqui a lógica da sua assistente virtual para responder a perguntas
        # e executar tarefas
        
        # Aqui está um exemplo simples de resposta
        if "olá" or "Olá" in tokens:
            
            print("Olá! Como posso ajudar?")
            # Aqui está um exemplo de como fazer a assistente virtual responder por voz
            response = "Olá! Como posso ajudar?"
            tts = gTTS(text=response, lang='pt-br')

            # Incrementando o índice
            index += 1
            
            # Gerando um nome de arquivo único com o índice
            file_name = f"response_{index}.mp3"
            
            tts.save(file_name)
            pygame.mixer.music.load(file_name)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
    except sr.UnknownValueError:
        print("Não foi possível entender o que você disse")
    except sr.RequestError as e:
        print("Não foi possível conectar-se ao serviço de reconhecimento de fala; {0}".format(e))
