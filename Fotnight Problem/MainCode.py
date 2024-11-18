# Start with 'N' health
# Cover 'D' distance
# Damage rate is 'P'
# Speed is 'S'
# Healing Time is 'H'

def solve(S: str) -> int:
    Health, HealingRate, Distance, Speed, StormDamage = map(int, S.split())

    PassingTime = Distance/Speed
    
    RemainingHealth = Health - (StormDamage * PassingTime)
    
    if RemainingHealth >= 0:
        return PassingTime
    
    elif (-1 * RemainingHealth) > (HealingRate * PassingTime):
        return -1
    
    else:
        IfStopsForHealing = HealingRate - StormDamage
        if IfStopsForHealing < 0:
            return -1
        
        return PassingTime + ( -RemainingHealth/IfStopsForHealing )


def main():
    T = int(input()) 
    
    for _ in range(T):
        S = input()
        result = solve(S)
        print(str(result)) 

if __name__ == '__main__':
    main()
