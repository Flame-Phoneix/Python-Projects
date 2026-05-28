from random import randrange

def diceroll(n):
    l = []
    for i in range(n):
        l.append(randrange(1,6))
    return l

def main():
    while True:
        ch = input("Roll the dice? (y/n): ")
        if ch.lower() == "n":
            print("Thank you for playing" )
            break
        elif ch.lower() == "y":
            n = int(input("How many dice you want to roll: "))
            r = diceroll(n)
            print(f"you rolled {r[0]}", end =", ")
            for i in range(1,len(r)):
                if i == len(r)-1:
                    print(f"and {r[i]}.\n")
                    break
                print(r[i], end=", ")           
        else:
            print("Invalid Choice")

main()
