import numpy as np
from scipy.io.wavfile import read, write


def generate_sine_wave(filename, duration, frequency, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = (np.sin(2 * np.pi * frequency * t) * 32767).astype(np.int16)
    write(filename, sample_rate, wave)

# Generate a 5-second sine wave at 440 Hz (A4 note)
generate_sine_wave("test.wav", duration=5, frequency=800)

def embed_mark(audio_file, output_file, watermark):
    sample_rate, audio = read(audio_file)

    if audio.dtype != np.int16:
        raise ValueError("Audio file must be in 16-bit format.")

    if len(audio.shape) > 1:
        audio = audio[:,0]

    audio_binary = np.unpackbits(audio.view(np.uint8))
    watermark_binary = np.array([int(b) for b in ''.join(format(ord(c), '08b') for c in watermark)], dtype=np.uint8)

    for i in range(len(watermark_binary)):
        audio_binary[i] = (audio_binary[i] & ~1) | watermark_binary[i]

    modified_audio = np.packbits(audio_binary).view(np.int16)
    write(output_file, sample_rate, modified_audio)


def extract_mark(audiofile, wmarklen):
    samplerate, audio = read(audiofile)

    if audio.dtype != np.int16:
        raise ValueError("Audio file must be in 16-bit format.")

    if len(audio.shape) > 1:
        audio = audio[:, 0]

    audiobin = np.unpackbits(audio.view(np.uint8))
    extracted_bits = audiobin[:wmarklen*8]

    watermark = ''.join(
            chr(int(''.join(str(bit) for bit in extracted_bits[i:i+8]),2))
            for i in range(0, len(extracted_bits),8)
    )
    return watermark


embed_mark('test.wav', 'output.wav', 'jeebus')
extracted_watermark = extract_mark('output.wav', len('jeebus'))
print(f"Extracted watermark: {extracted_watermark}")
