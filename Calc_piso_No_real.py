#Asks the user a real number to find its floor. Then, it puts this number in the piso() function, which will return the floor of the number. Prints the floor of this number and the product between the number and its floor.
def main():
    Number = float(input("\n=====\nDo you want to find the floor of which number? "))
    print(f"=====\nThe floor of {Number} is:", piso(Number),f"\n=====\n{Number} times its floor is:", round(Number * piso(Number), 6),"\n")

#Defines a function to calculate the floor. 
def piso(n):
    if round(n) <= n:
        return round(n)
    else:
        if n < 0:
            return int(n) - 1
        if n > 0:
            return int(n)

main()



