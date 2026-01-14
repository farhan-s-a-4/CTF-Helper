import wave
import numpy as np
import matplotlib.pyplot as plt

def plot_wav_waveform(file_path):
    print("File found, as the process ends the morse code figur will be saved in the same directory as \"Flag.pdf\"")
    try:
        with wave.open(file_path, 'rb') as wf:
            n_channels = wf.getnchannels()
            sampwidth = wf.getsampwidth()
            frame_rate = wf.getframerate()
            n_frames = wf.getnframes()

            audio_data_bytes = wf.readframes(n_frames)

            dtype = np.int16 if sampwidth == 2 else (np.int8 if sampwidth == 1 else np.int32)

            signal = np.frombuffer(audio_data_bytes, dtype=dtype)

            time = np.linspace(0, n_frames / frame_rate, num=n_frames)

            plt.figure(figsize=(12, 4))

            if n_channels > 1:
                signal = signal[::2]
                time = time[::2] 
                plt.title(f'Waveform of {file_path} (Left Channel)')
            else:
                plt.title(f'Waveform of {file_path}')

            plt.plot(time, signal, color='blue')
            plt.xlabel("Time (seconds)")
            plt.ylabel("Amplitude")
            plt.grid(True)
            plt.savefig("Flag.pdf")

    except wave.Error as e:
        print(f"Error opening or reading WAV file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    plot_wav_waveform("morse_chal.wav")