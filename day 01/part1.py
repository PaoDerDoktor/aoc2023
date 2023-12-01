def day01_part1_main() -> int:
    with open("day 01/inputs.txt", 'r') as inFile:
        data: list[str] = [line.strip() for line in inFile.readlines()]
        
        acc: int = 0
        for entry in data:
            nString: str = ""
            for c in entry:
                if c.isnumeric():
                    nString += c
            
            if len(nString) == 0:
                continue
            else:
                acc += int(nString[0] + nString[-1])
        return acc
            

if __name__ == "__main__":
    print(day01_part1_main())
