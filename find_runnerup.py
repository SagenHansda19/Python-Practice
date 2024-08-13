if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    r = sorted(set(arr), reverse = True)
    print(r[1])
