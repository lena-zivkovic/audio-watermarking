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
    # make this so it outputs the watermarked file so u can call export in main.


#
# code for extracting the watermark
# def extract_watermark()
# TODO


#
# print the extracted watermark
# def print_watermark()
# TODO


def main():
    def get_input():
    audio_file = input("Enter the name of the audio file to process: ")
    watermark = input("Enter the watermark: ")
    tag = input("Enter w to watermark the file or e to extract a watermark from the file")
    if tag == 'w':
        output_filename = input("Enter the name for the output audio file: ")
        embed_watermark(audio_file, output_filename, watermark)
    elif tag == 'e':
        # extract
    else: exit(1)

if __name__ == "__main__":
    main()
