#
# author: Lena Zivkovic
# date: December 25, 2024
#
# watermarking.py: Embeding a watermark into an audio file using the LSB method
#


import numpy as np
from scipy.io.wavfile import read, write


#
# LSB algo for adding a watermark
#
def embed_watermark(audio_file, output_filename, watermark):
    sample_rate, audio = read(audio_file)

    if audio.dtype != np.int16:
        raise ValueError("Audio file must be in 16-bit format.")

    if len(audio.shape) > 1:
        audio = audio[:, 0]

    audio_binary = np.unpackbits(audio.view(np.uint8))
    watermark_binary = np.array([int(b) for b in ''.join(format(ord(c), '08b') for c in watermark)], dtype=np.uint8)

    for i in range(len(watermark_binary)):
        audio_binary[i] = (audio_binary[i] & ~1) | watermark_binary[i]

    modified_audio = np.packbits(audio_binary).view(np.int16)
    write(output_filename, sample_rate, modified_audio)


#
# code for extracting the watermark
def extract_watermark(audio_file, watermark_length):
    sample_rate, audio = read(audio_file)

    if audio.dtype != np.int16:
        raise ValueError("Audio file must be in 16-bit format.")

    if len(audio.shape) > 1:
        audio = audio[:, 0]

    audio_binary = np.unpackbits(audio.view(np.uint8))
    extracted_bits = audio_binary[:watermark_length*8]

    watermark = ''.join(
            chr(int(''.join(str(bit) for bit in extracted_bits[i:i+8]), 2))
            for i in range(0, len(extracted_bits), 8)
    )
    return watermark


def main():
    audio_file = input("Enter the name of the audio file to process: ")
    watermark = input("Enter the watermark: ")
    tag = input("Enter w to watermark the file or e to extract a watermark from the file: ")
    if tag == 'w':
        output_filename = "Watermarked_" + audio_file
        embed_watermark(audio_file, output_filename, watermark)
        print("Audio file watermarked.")
    elif tag == 'e':
        extracted = extract_watermark(audio_file, len(watermark))
        print(f"Extracted watermark: {extracted}")
    else: exit(1)

if __name__ == "__main__":
    main()
