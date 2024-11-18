import math

def solve(S: str) -> str:

    B, N = map(int, S.split())

    Buildings = list(map(int, input().split()))

    left, right = 0, max(Buildings)
    
    def FindDanger(Bridge: int) -> int:
        danger = 0

        for i in Buildings:
            if i < Bridge:
                danger += Bridge - i
        
        return danger
    
    def FindCost(Bridge: int) -> int:
        cost = 0

        for i in Buildings:
            if i > Bridge:
                cost += i - Bridge
        
        return cost
    

    while left <= right:

        mid = math.floor(( left + right ) / 2 )

        Danger, Cost = FindDanger(mid), FindCost(mid)

        if Cost <= B:
            right = mid - 1
        
        elif Cost > B:
            left = mid + 1
        
        print('Danger : ', Danger)
        print('Cost : ', Cost)
        print('Left : ', left)
        print('Right : ', right)
    
    return str(left)

def main():
    T = int(input())

    for _ in range(T):
        string = input()

        result = solve(string)
        print(result)

if __name__ == '__main__':
    main()