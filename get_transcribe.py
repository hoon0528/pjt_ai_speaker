import os
from google.cloud import speech
from tqdm import tqdm
import io

# Google Cloud Speech-to-Text setup
client = speech.SpeechClient()

def transcribe_audio(file_path):
    with io.open(file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="ko-KR",
    )

    response = client.recognize(config=config, audio=audio)

    transcripts = []
    for result in response.results:
        transcripts.append(result.alternatives[0].transcript)

    return " ".join(transcripts)

# Directory containing WAV files
directory = 'test'
output_lines = []

# Transcribe all WAV files in the 'loopy' folder
for file_name in tqdm(os.listdir(directory)):
    if file_name.endswith('.wav'):
        file_path = os.path.join(directory, file_name)
        transcript = transcribe_audio(file_path)
        output_lines.append(f"{file_name}|{transcript}")

# Write transcriptions to output file
with open('transcriptions.txt', 'w', encoding='utf-8') as f:
    for line in output_lines:
        f.write(line + "\n")

print("Transcription completed. Check the 'transcriptions.txt' file for results.")