def main():
    x = get_int("What's x ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try: 
            return int(input(prompt))
        except ValueError:

#use the pass and you stay in the loop but don't say anything....
            pass

main()
