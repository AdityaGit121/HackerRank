if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        try:
            a, b = input().split()
            print(int(a) // int(b))
        except (ZeroDivisionError, ValueError) as e:
            print("Error Code:", e)