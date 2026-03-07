from app.multimodal.speech_to_text import transcribe_audio

with open("sample_input/sample_audio.wav", "rb") as f:
    text = transcribe_audio(f)

print(text)