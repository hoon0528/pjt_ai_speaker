import os
from tqdm import tqdm
from pydub import AudioSegment

# Directories
source_directory = 'loopy'
target_directory = os.path.join(source_directory, 'mono')

# Ensure the target directory exists
os.makedirs(target_directory, exist_ok=True)

def convert_to_mono(file_path, target_path):
    audio = AudioSegment.from_wav(file_path)
    audio = audio.set_channels(1)
    audio.export(target_path, format="wav")

# Iterate over all WAV files in the source directory
for file_name in tqdm(os.listdir(source_directory)):
    if file_name.endswith('.wav'):
        source_path = os.path.join(source_directory, file_name)
        target_path = os.path.join(target_directory, file_name)
        
        # Convert to mono and save to target directory
        convert_to_mono(source_path, target_path)
        print(f"Converted {file_name} to mono and saved to {target_path}")

print("All files have been converted to mono.")
