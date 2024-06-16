def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from peg {source} to peg {target}")
        return
    hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from peg {source} to peg {target}")
    hanoi(n-1, auxiliary, source, target)


n = 3
hanoi(n, 'A', 'B', 'C')
