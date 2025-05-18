# Here is the dictionary
distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():
    spacecraft = input("Enter a spacecraft: ")

#Exception for two errors you have and then told the end user why - 
#KeyError because something is not in the dictionary
#ValueError can't convert the value (maybe a string was input)
    try:
        m = convert(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' is not in dictionary")
    except ValueError:        
        print(f"'Can't convert '{distances[spacecraft]}")
        return

def convert(au):
    return au * 14959787070

main()
