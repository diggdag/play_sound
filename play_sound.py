#!/usr/bin/env python3
import sys
import time
import subprocess

def play_sound(file_path):
    subprocess.run(['/usr/bin/afplay', file_path])

def main(start_time, interval_minutes, repeat_count, sound_file_path):
    for i in range(repeat_count):
        current_time = time.strftime("%H:%M", time.localtime())
        print(f"Current time: {current_time}")

        # 指定した開始時刻まで待機
        while current_time != start_time:
            time.sleep(60)  # 1分ごとにチェック
            current_time = time.strftime("%H:%M", time.localtime())
            print(f"Current time: {current_time}")

        print(f"Playing sound at {current_time}...")
        play_sound(sound_file_path)

        if i < repeat_count - 1:
            print(f"Waiting {interval_minutes} minutes before next play...")
            time.sleep(interval_minutes * 60)

    print("Program completed.")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./play_sound.py <start_time> <interval_minutes> <repeat_count> <sound_file_path>")
        sys.exit(1)

    start_time = sys.argv[1]
    interval_minutes = int(sys.argv[2])
    repeat_count = int(sys.argv[3])
    sound_file_path = sys.argv[4]

    print("Starting the program...")
    main(start_time, interval_minutes, repeat_count, sound_file_path)
