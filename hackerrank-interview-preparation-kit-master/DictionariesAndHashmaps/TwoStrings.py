import os


def main():
    pairs = int(input())
    answers = [False] * pairs

    for pair in range(pairs):
        s1 = input()
        s2 = input()
        answers[pair] = len(set(s1) & set(s2)) > 0

    with open(os.environ['OUTPUT_PATH'], 'w') as f:
        f.write('\n'.join('YES' if answer else 'NO' for answer in answers))


if __name__ == '__main__':
    main()
