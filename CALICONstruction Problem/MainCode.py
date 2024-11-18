from collections import Counter
import math

def solve(givenLetter: str) -> str:
    # C can convert into 'U', 'N'
    # I can convert into 'H'
    
    maximum_freq = 0

    OneBlock = {'C' : 2, 'A' : 1, 'L' : 1, 'I' : 1, 'O' : 1}

    GivenBlock = Counter(givenLetter)

    CanHave = ['C', 'A', 'L', 'I', 'C', 'O', 'U', 'N', 'H']
    
    for key, value in GivenBlock.items():
        if key not in CanHave:
            maximum_freq = -1
            break
        
        elif key == 'U':
            GivenBlock['C'] += value
            GivenBlock['U'] = 0
        
        elif key == 'N':
            GivenBlock['C'] += value
            GivenBlock['N'] = 0
        
        if key != 'C':
            maximum_freq = max(maximum_freq, value)

    val = math.ceil(GivenBlock['C']/2)
    if maximum_freq < val:
        maximum_freq = max(maximum_freq, val)
        

    return maximum_freq


def main():
    T = int(input()) 
    
    for _ in range(T):
        S = input()
        result = solve(S)
        print(result)  

if __name__ == '__main__':
    main()
