import argparse
import sys
import subprocess
from os import path
from time import sleep

import numpy as np
from colorama import Fore, Back, Style


def parse_input_path():
    parser = argparse.ArgumentParser(
        description='Process file with sentences and output accuracy score')
    parser.add_argument('input_file', metavar='My_file.txt', type=str,
                        nargs=1, help='input file for analyze')
    args = parser.parse_args()
    return args.input_file[0]


def is_valid(file_path):
    with open(file_path) as file:
        try:
            float(file.readline().strip().split()[-1])
        except ValueError:
            return False

    return True


def analyze(file_path):
    n_lines = int(subprocess.check_output(f'wc -l {file_path}', shell=True).split()[0])
    scores = np.zeros(n_lines, dtype=float)
    wrong_sentences = []

    with open(file_path) as file:
        for i in range(n_lines):
            line = file.readline().strip()
            score = line.split()[-1]
            scores[i] = score
            if score != '1':
                wrong_sentences.append(line)
    accuracy = round(scores.mean() * 100, 3)

    print(f'General score is' + Fore.GREEN + f' {accuracy} %\n')
    sleep(0.7)
    print(Fore.YELLOW + 'Wrong sentences:')
    for sentence in wrong_sentences:
        without_score = (' ').join(sentence.split()[:-1])
        score = sentence.split()[-1]
        print(Fore.RESET + without_score + Fore.RED + ' ' + score)


def main():
    file_path = path.abspath(parse_input_path())

    if not path.exists(file_path):
        print(Back.RED + f'file {file_path} doesn\'t exist')
    elif not path.isfile(file_path):
        print(Back.RED + f'{file_path} isn\'t a file')
    elif not is_valid(file_path):
        print(Back.YELLOW + 'It seems that file isn\'t valid. Are you sure that you passed correct file?')
    else:
        analyze(file_path)


if __name__ == '__main__':
    main()
