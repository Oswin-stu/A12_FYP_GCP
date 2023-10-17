from transformers import pipeline

cls = pipeline("automatic-speech-recognition")

res = cls("hello.mp3")

print(res)
