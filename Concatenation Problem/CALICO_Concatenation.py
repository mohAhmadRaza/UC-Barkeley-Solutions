def solve(S: str) -> str:
    ToCompare = 'CALICO'
    ind = 0
    stringToCompare = S

    for j in range(len(ToCompare)):
        if ind < len(stringToCompare) and ToCompare[j] == stringToCompare[ind].upper():
            ind += 1
        else:
            ind = 0

    if ind == 6:
        return ToCompare
    if ind == 0:
        return stringToCompare
    else:
        return ToCompare + stringToCompare[ind:]


def main():
    try:
        T = int(input())  # Added prompt for clarity
    except ValueError:
        print("Please enter a valid integer for the number of test cases.")
        return
    
    for _ in range(T):
        S = input()  # Added prompt for clarity
        result = solve(S)
        print(result)  # Debug print to check output from `solve()`

if __name__ == '__main__':
    main()
