import speech_recognition as sr

class VoiceRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.memory = []

    def recognize_speech(self):
        with sr.Microphone() as source:
            print("말씀해주세요.")
            audio = self.recognizer.listen(source)

            try:
                text = self.recognizer.recognize_google(audio, language="ko-KR")
                print("인식된 텍스트: " + text)
                self.memory.append(text)
            except sr.UnknownValueError:
                print("음성 인식에 실패했습니다.")
            except sr.RequestError as e:
                print(f"음성 인식 서비스에 연결할 수 없습니다. 에러: {e}")

    def get_memory(self):
        return self.memory


voice_recognizer = VoiceRecognizer()

while True:
    voice_recognizer.recognize_speech()
    memory = voice_recognizer.get_memory()
    print("메모리에 저장된 텍스트:", memory)
