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

The Least Significant Bit (LSB) technique is a method of hiding data within an audio file by altering the least significant bit of each audio sample. Since these bits have minimal impact on the overall quality of the audio, this technique is a popular choice for embedding watermarks or covert messages.

### Advantages

- High Imperceptibility: Changes made to the least significant bits are inaudible to the human ear.
- Simplicity: The technique is computationally simple and easy to implement.
- Minimal File Size Overhead: The watermark is directly embedded into the audio file without significantly increasing the file size.

### Limitations

- Vulnerability to Noise: LSB watermarking can be easily disrupted by signal processing operations, such as compression or filtering.
- Limited Capacity: The number of bits available for embedding is limited by the size of the audio file.


## Program Introduction

### Program Features

### How it Works

## Usage

### Dependencies

### Command-Line Interface

### Embedding a Watermark into a .wav file

### Extracting the Watermark from a .wav file

## Example

### Embedding

### Extraction


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
