def mutate_string(string, position, character):
    res = list(string)
    res[position] = character
    res = "".join(res)
    return res

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)