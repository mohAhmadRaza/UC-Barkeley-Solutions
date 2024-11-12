def solve(S: str) -> str:
    
    Time = int(S)
    if Time == 0:
        return 'haha good one'
    
    elif Time >= 180:
        return 'canceled'
    
    else:
        string = "berkeley" * (Time // 10)
        return string + "time"


def main():
    T = int(input()) 
    
    for _ in range(T):
        S = input() 
        result = solve(S)
        print(result)

if __name__ == '__main__':
    main()
