def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for i in range(len(names)):
        print(write_letter(names[i], "Princes Peach"))
             
def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
    Dear {receiver}

    You are invited

    Sincerely,
    {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+
main()