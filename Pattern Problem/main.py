def solve(S: str) -> str:
    a, b = map(int, S.split())
    res = set()
    for i in range(a):
        s = input()
        count = s.count("#")
        if not count == 0:
            res.add(count)
    if len(res) == 1:
        return "ferb"
    
    else:
        return "phineas"



def main():
    
    T = int(input())  # Added prompt for clarity

    for _ in range(T):
        S = input()  # Added prompt for clarity
        result = solve(S)
        print(result)  # Debug print to check output from `solve()`

if __name__ == '__main__':
    main()
