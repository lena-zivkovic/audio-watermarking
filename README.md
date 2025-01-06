# Audio Watermarking with the LSB Technique

This project demonstrates how to embed and extract watermarks from audio files using the Least Significant Bit (LSB) technique.

## Introduction

The rapid growth of audio content through streaming platforms, social media, and digital distribution channels, has forever changed how we create, share, and consume media. However, this widespread accessibility has also introduced significant challenges, such as copyright infringement, unauthorized reproduction, and illegal distribution. Various solutions have emerged to address these issues, one of them being digital audio watermarking which focuses on embedding copyright details, ownership identifiers, or authentication codes within an audio signal.

### Digital Audio Watermarking

Digital audio watermarking is a process of embedding hidden data, known as a watermark, into an audio file without compromising its perceptual quality. Unlike metadata, which is external to the file and can be easily removed or modified, a watermark is integrated directly into the audio content, making it a more resilient and secure method of embeding information.

### How Does it Work

Audio watermarking involves altering specific properties of the audio signal to encode the watermark. These alterations are designed to be:

- Imperceptible: The changes should be inaudible to the human ear, ensuring the audio quality remains intact.
- Robust: The watermark must resist common audio processing operations like compression, filtering, or format conversion.
- Secure: The embedded data should be difficult to remove or modify without degrading the audio signal significantly.

There are several techniques for implementing digital audio watermarking, including time-domain methods, frequency-domain methods, and Least Significant Bit (LSB) modification.

## What is LSB Audio Watermarking

The Least Significant Bit (LSB) technique is one of the simplest and most widely used methods for audio watermarking. It operates directly on the audio samples in the time domain. By modifying the least significant bits of the audio signal, the LSB method embeds watermark data while maintaining the perceptual quality of the audio.

### Advantages

- High Imperceptibility: Changes made to the least significant bits are inaudible to the human ear.
- Simplicity: The technique is computationally simple and easy to implement.
- Minimal File Size Overhead: The watermark is directly embedded into the audio file without significantly increasing the file size.

### Limitations

- Vulnerability to Noise: LSB watermarking can be easily disrupted by signal processing operations, such as compression or filtering.
- Limited Capacity: The number of bits available for embedding is limited by the size of the audio file.


## Program Introduction

This program provides an implementation of LSB audio watermarking. Users can embed a text-based watermark into .wav files and later extract the watermark from watermarked files. The program is designed with simplicity and efficiency in mind, using Python and libraries NumPy and SciPy.

### Program Features

- Embed a text-based watermark into a .wav audio file using the LSB technique.
- Extract a watermark from a watermarked .wav file.
- support for customizable output filenames

### How it Works

**1. Embedding**
- The audio file is read, and its samples are converted into binary format.
- The watermark is converted into binary (ASCII representation).
- The least significant bits of the audio samples are replaced with the bits of the watermark.
- The modified audio data is saved to a new .wav file.

**2. Extraction**
- The watermarked file is read, and the least significant bits of the samples are extracted.
- These bits are grouped into bytes and converted back into characters.
- The reconstructed watermark is returned as output.

## Usage

### Dependencies

- Python 3.12.3
- Libraries: NumPy, SciPy

### Command-Line Interface

**1. Embedding a Watermark into a .wav file**

- Run the program with the following command:
<code>python3 watermarking.py \<audio_file> w \<watermark></code>

- You will be prompted to enter the name of the output file.

**Example:**
<code>python3 watermarking.py input.wav w "HelloWorld"</code>

Output:
- A watermarked .wav file with the watermark embedded

**2. Extracting the Watermark from a .wav file**

- Run the program with the following command:
<code>python3 watermarking.py \<audio_file> e \<watermark></code>

- The program will extract the watermark from the audio file.

**Example:**
<code>python3 watermarking.py input.wav w "HelloWorld"</code>

Output:
- The extracted watermark displayed in the console.

## Example

### Embedding

Command:
<code>python3 watermarking.py input.wav w "Secret"</code>

User input for output file:
> Enter the name for the output watermarked file: output

Result:
- The watermark "Secret" is embedded into output.wav

### Extraction

Command:
<code>python3 watermarking.py output.wav e "Secret"</code>

Result:
- The extracted watermark matches the length of the provided input watermark, returning the corresponding portion of the embedded date.

# sources
MP3 Audio Watermarking - Tianruo Sun, Lihao Yang, Zimo Cheng
https://hajim.rochester.edu/ece/sites/zduan/teaching/ece472/projects/2020/TianruoSun_LihaoYang_ZimoCheng_MP3Watermarking_ProjectReport.pdf

Audio Watermarking Fun with Python, Pydub, and ffmpeg - docred, Medium
https://docred.medium.com/audio-watermarking-fun-with-python-pydub-and-ffmpeg-427f8871587

Digital_Audio_Watermarking- - ACallglad
https://github.com/ACallglad/Digital_Audio_Watermarking-/tree/main

Twenty years of audio watermarking - a comprehensive review - Guang Hua, Jiwu Huang, Yun Q. Shi, Jonathan Goh, Vrizlynn L.L. Thing
https://www.sciencedirect.com/science/article/pii/S0165168416300263#abs0015

A survey: Digital audio watermarking techniques and applications - Sanjay Pratap Singh Chauhan, S. A. M. Rizvi
https://ieeexplore-ieee-org.ezproxy.rit.edu/abstract/document/6749625
