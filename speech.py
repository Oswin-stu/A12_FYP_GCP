from transformers import pipeline

cls = pipeline("automatic-speech-recognition")

res = cls("hello world.mp3")

print(res)
