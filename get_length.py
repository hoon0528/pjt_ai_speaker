import os
import wave
import contextlib

# Directory containing WAV files
directory = 'loopy'

def get_wav_info(file_path):
    with contextlib.closing(wave.open(file_path, 'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return rate, duration

total_duration = 0.0

# Iterate over all WAV files in the directory
for file_name in os.listdir(directory):
    if file_name.endswith('.wav'):
        file_path = os.path.join(directory, file_name)
        sample_rate, duration = get_wav_info(file_path)
        total_duration += duration
        print(f"File: {file_name}, Sample Rate: {sample_rate} Hz, Duration: {duration:.2f} seconds")

# Convert total duration to minutes and seconds for better readability
minutes, seconds = divmod(total_duration, 60)
print(f"Total duration of all WAV files: {int(minutes)} minutes and {seconds:.2f} seconds")
