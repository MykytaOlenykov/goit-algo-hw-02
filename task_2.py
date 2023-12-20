from collections import deque


def palindrome_check(word: str) -> bool:
    if len(word) <= 1:
        return False

    d = deque(word.lower())

    while len(d) > 1:
        if d.pop() != d.popleft():
            return False

    return True


def main():
    print(palindrome_check("дід"))
    print(palindrome_check("Авто"))
    print(palindrome_check("Анна"))
    print(palindrome_check("Aa"))
    print(palindrome_check("K"))
    print(palindrome_check(""))


if __name__ == "__main__":
    main()
