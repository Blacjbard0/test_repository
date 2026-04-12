# -*- coding: utf-8 -*-
import random
import time
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def print_slow(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def dramatic_reveal():
    drums = ["じゃ", "か", "じゃ", "か", "じゃ", "か", "じゃ", "〜", "〜", "ん！！！"]
    for beat in drums:
        print(f"\r  {beat}    ", end='', flush=True)
        time.sleep(0.18)
    print()

def spring_line():
    print("  🌸 🌷 🌺 🌼 🌸 🌷 🌺 🌼 🌸 🌷 🌺")

def main():
    print()
    spring_line()
    print()
    print_slow("  ✨ パパとママ、どっちが大好き？✨", delay=0.07)
    print()
    spring_line()
    print()

    time.sleep(0.8)
    print_slow("  さあ、運命の答えは...？", delay=0.08)
    print()
    time.sleep(1.0)

    print("  ", end='', flush=True)
    dramatic_reveal()
    print()

    result = random.choice(["パパ", "ママ"])

    if result == "パパ":
        print("  🎉🌸  大好きなのは... 【 パパ 】！！ 🌸🎉")
        print()
        print("  👨 パパ、愛されてるよ〜！ (^o^)/")
    else:
        print("  🎉🌷  大好きなのは... 【 ママ 】！！ 🌷🎉")
        print()
        print("  👩 ママ、愛されてるよ〜！ (^o^)/")

    print()
    spring_line()
    print()
    print("  🌸 春のように あたたかい気持ちで〜 🌸")
    print()

if __name__ == "__main__":
    main()
