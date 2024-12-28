#
# author: Lena Zivkovic
# date: December 25, 2024
#
# watermarking.py: Embeding a watermark into an audio file using the LSB method
#


import numpy as np
from scipy.io.wavfile import read, write
import argparse

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
    parser = argparse.ArgumentParser(description="Audio Watermarking Tool")
    parser.add_argument("audio_file", type=str, help="The name of the audio file to process.")
    parser.add_argument("tag", type=str, choices=["w", "e"], help="'w' to watermark or 'e' to extract a watermark.")
    parser.add_argument("watermark", type=str, help="The watermark string for embedding or length for extraction.")
    args = parser.parse_args()

    if args.tag == 'w':
        output_filename = input("Enter the name for the output watermarked file: ")
        output_filename += ".wav"
        embed_watermark(args.audio_file, output_filename, args.watermark)
        print(f"Audio file watermarked and saved as '{output_filename}'.")
    elif args.tag == 'e':
        extracted = extract_watermark(args.audio_file, len(args.watermark))
        print(f"Extracted watermark: {extracted}")
    else:
        print("Invalid tag. Use 'w' to watermark or 'e' to extract.")
        exit(1)

if __name__ == "__main__":
    main()
