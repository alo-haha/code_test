from gtts import gTTS
import pygame
#입력된 텍스트를 음성으로 변환하여 저장하는 코드입니다.
#text = "안녕하세요. 저는 인공지능입니다."

#tts = gTTS(text=text, lang="ko")
#tts.save("hello.mp3")

#pygame.mixer.init()
#pygame.mixer.music.load("hello.mp3")
#pygame.mixer.music.play()

#while pygame.mixer.music.get_busy():
#    pass

#텍스트 파일을 읽어서 음성으로 변환하여 저장하는 코드입니다.
file_path = r"텍스트음성으로 변환/스크립트.txt"
with open(file_path, 'rt', encoding="utf-8") as f:
    read_file = f.read()
    
tts = gTTS(text=read_file, lang='ko')
tts.save(r"텍스트음성으로 변환/스크립트.mp3")