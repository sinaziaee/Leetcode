def hanoi(n, src, aux, tar):
    if n == 1:
        print(src, "To", tar)
        return
    
    hanoi(n-1, src, tar, aux)
    print(src, "To", tar)
    hanoi(n-1, aux, src, tar)
    
    
if __name__ == '__main__':
    no_of_disks = 4
    print("------------------------------")
    hanoi(no_of_disks, "A", "B", "C")