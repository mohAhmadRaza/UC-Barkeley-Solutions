def solve(S: str) -> str:
    result = []
    
    for i in range(1, len(S)+1):
        if S[i-1:i+1] == "RE":
           result.append("[###OREO###]")
        
        elif S[i-1] == 'O':
            result.append(" [--------] ")
        
        elif S[i-1] == '&':
            result.append("")
        
        else:
            continue
        
    return '\n'.join(result)


def main():
    T = int(input())
    
    for _ in range(T):
        S = input() 
        result = solve(S)
        print(result)

if __name__ == '__main__':
    main()
