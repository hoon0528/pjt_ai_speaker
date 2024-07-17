# Function to extract the number from the filename in the transcription line
def extract_number(line):
    try:
        return int(line.split(' ')[1].split(').wav')[0])
    except (IndexError, ValueError):
        return -1

# Read the transcriptions from the file
with open('transcriptions.txt', 'r', encoding='utf-8') as file:
    transcriptions = file.readlines()

# Sort the transcriptions by the numeric part of the filename
sorted_transcriptions = sorted(transcriptions, key=extract_number)

# Write the sorted transcriptions to a new output file
with open('sorted_transcriptions.txt', 'w', encoding='utf-8') as file:
    for line in sorted_transcriptions:
        file.write(line)

print("Transcriptions sorted and saved to 'sorted_transcriptions.txt'.")
