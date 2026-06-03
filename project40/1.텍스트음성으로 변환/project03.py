from gtts import gTTS
text = "안녕하세요. 저는 인공지능입니다."
tts = gTTS(text=text, lang='ko')
tts.save(r"텍스트음성으로 변환/hello.mp3")