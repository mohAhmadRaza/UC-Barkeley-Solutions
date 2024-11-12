
from collections import Counter

def solve(S: str) -> str:
    
    List = list(map(int, S.split()))
    freq = Counter(List)
    
    maximum = float('-inf')
    ans = 0
    for a, b in freq.items():
        if a*b > maximum:
            maximum = a*b
            ans = a
    
    return str(ans)


def main():
    T = int(input()) 
    
    for _ in range(T):
        N = input()
        S = input() 
        result = solve(S)
        print(result)

if __name__ == '__main__':
    main()


