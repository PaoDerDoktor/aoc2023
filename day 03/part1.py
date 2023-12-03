def day03_part1_main() -> int:
    with open("day 03/inputs.txt") as inFile:
        grid: list[list[str|int]] = [[int(c) if c.isnumeric() else c for c in line.strip()] for line in inFile.readlines()]
        
        numbersStarts: list[tuple[int, int]] = []
        
        for y, l in enumerate(grid):
            for x, c in enumerate(l):
                if isinstance(c, int) and (not isinstance(grid[y][x-1], int) or x == 0):
                    numbersStarts.append((x, y))
        
        partNumbers: list[int] = []
        
        for numberStart in numbersStarts:
            currentLoc: tuple[int, int] = numberStart
            while 0 <= currentLoc[0] < len(grid[currentLoc[1]]) and isinstance(grid[currentLoc[1]][currentLoc[0]], int):
                found: bool = False
                
                for offset in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    checked: tuple[int, int] = (currentLoc[0]+offset[0], currentLoc[1]+offset[1])
                    
                    if (not 0 <= checked[0] < len(grid[0])) or (not 0 <= checked[1] < len(grid)):
                        continue
                    
                    if isinstance(grid[checked[1]][checked[0]], str) and grid[checked[1]][checked[0]] != ".":
                        found = True
                        break
                
                if found:
                    numberString:  str             = ""
                    numberPointer: tuple[int, int] = numberStart
                    
                    while 0 <= numberPointer[0] < len(grid[numberPointer[1]]) and isinstance(grid[numberPointer[1]][numberPointer[0]], int):
                        numberString += str(grid[numberPointer[1]][numberPointer[0]])
                        numberPointer = (numberPointer[0]+1, numberPointer[1])
                    
                    partNumbers.append(int(numberString))
                    
                    break
                
                currentLoc = (currentLoc[0]+1, currentLoc[1])
        
        return sum(partNumbers)
        

if __name__ == "__main__":
    print(day03_part1_main())
