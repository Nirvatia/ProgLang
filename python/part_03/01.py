n = int(input())

def solve(x):
    MAX_PER_CLASS = 25
    
    if n < MAX_PER_CLASS:
        print(f"1 {n}")
        return

    if n % MAX_PER_CLASS == 0:
        print(f"{n // MAX_PER_CLASS} {MAX_PER_CLASS}")
        return
    
    curr = MAX_PER_CLASS

    while True:
        rem = n % curr
        q = n // MAX_PER_CLASS

        if rem > q or (curr + 1 > MAX_PER_CLASS):
            curr -= 1
            continue
        else:
            break
        
    print(f"{n // curr} {curr}")
    
    return
    
solve(n)
        
