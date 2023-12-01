def day01_part2_main() -> int:
    with open("day 01/inputs.txt", 'r') as inFile:
        data: list[str] = [line.strip() for line in inFile.readlines()]
        
        acc: int = 0
        for entry in data:
            sp: int = 0
            formatted: str = ""
            
            while sp < len(entry):
                if entry[sp:sp+3] == "one":
                    formatted += "1"
                    sp += 2
                elif entry[sp:sp+3] == "two":
                    formatted += "2"
                    sp += 2
                elif entry[sp:sp+5] == "three":
                    formatted += "3"
                    sp += 4
                elif entry[sp:sp+4] == "four":
                    formatted += "4"
                    sp += 3
                elif entry[sp:sp+4] == "five":
                    formatted += "5"
                    sp += 3
                elif entry[sp:sp+3] == "six":
                    formatted += "6"
                    sp += 2
                elif entry[sp:sp+5] == "seven":
                    formatted += "7"
                    sp += 4
                elif entry[sp:sp+5] == "eight":
                    formatted += "8"
                    sp += 4
                elif entry[sp:sp+4] == "nine":
                    formatted += "9"
                    sp += 3
                else:
                    formatted += entry[sp]
                    sp += 1
            
            nString: str = ""
            for c in formatted:
                if c.isnumeric():
                    nString += c
            
            if len(nString) == 0:
                continue
            else:
                acc += int(nString[0] + nString[-1])

            print(entry, formatted, nString, int(nString[0] + nString[-1]))
        return acc
            

if __name__ == "__main__":
    print(day01_part2_main())
