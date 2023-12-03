def get_whole_number(grid: list[list[str|int]], location: tuple[int, int]) -> int:
    if not isinstance(grid[location[1]][location[0]], int):
        return -1
    
    startLoc: tuple[int, int] = location
    while 0 <= startLoc[0] < len(grid[startLoc[1]]) and isinstance(grid[startLoc[1]][startLoc[0]], int):
        startLoc = (startLoc[0]-1, startLoc[1])

    startLoc = (startLoc[0]+1, startLoc[1])
    
    numberString:  str             = ""
    numberPointer: tuple[int, int] = startLoc
    
    while 0 <= numberPointer[0] < len(grid[numberPointer[1]]) and isinstance(grid[numberPointer[1]][numberPointer[0]], int):
        numberString += str(grid[numberPointer[1]][numberPointer[0]])
        numberPointer = (numberPointer[0]+1, numberPointer[1])

    return int(numberString)

def day03_part2_main() -> int:
    with open("day 03/inputs.txt") as inFile:
        grid: list[list[str|int]] = [[int(c) if c.isnumeric() else c for c in line.strip()] for line in inFile.readlines()]
        
        gearsPositions: list[tuple[int, int]] = []
        
        for y, l in enumerate(grid):
            for x, c in enumerate(l):
                if isinstance(c, str) and c =='*':
                    gearsPositions.append((x, y))
        
        ratios: list[int] = []
        
        for gearPosition in gearsPositions:
            adjacents: list[int] = []
            
            if (0 <= gearPosition[0]-1) and (n:=get_whole_number(grid, (gearPosition[0]-1, gearPosition[1]))) != -1:
                adjacents.append(n)
            
            if (gearPosition[0]+1 < len(grid[0])) and (n:=get_whole_number(grid, (gearPosition[0]+1, gearPosition[1]))) != -1:
                adjacents.append(n)
            
            if (0 <= gearPosition[1]-1) and grid[gearPosition[1]-1][gearPosition[0]] == '.':
                if (0 <= gearPosition[0]-1) and (n:=get_whole_number(grid, (gearPosition[0]-1, gearPosition[1]-1))) != -1:
                    adjacents.append(n)
                if (gearPosition[0]+1 < len(grid[0])) and (n:=get_whole_number(grid, (gearPosition[0]+1, gearPosition[1]-1))) != -1:
                    adjacents.append(n)
            elif (0 <= gearPosition[1]-1) and (n:=get_whole_number(grid, (gearPosition[0], gearPosition[1]-1))) != -1:
                    adjacents.append(n)
            
            if (gearPosition[1]+1 < len(grid)) and grid[gearPosition[1]+1][gearPosition[0]] == '.':
                if (0 <= gearPosition[0]-1) and (n:=get_whole_number(grid, (gearPosition[0]-1, gearPosition[1]+1))) != -1:
                    adjacents.append(n)
                if (gearPosition[0]+1 < len(grid[0])) and (n:=get_whole_number(grid, (gearPosition[0]+1, gearPosition[1]+1))) != -1:
                    adjacents.append(n)
            elif (gearPosition[1]+1 < len(grid)) and (n:=get_whole_number(grid, (gearPosition[0], gearPosition[1]+1))) != -1:
                    adjacents.append(n)
            
            if len(adjacents) == 2:
                ratios.append(adjacents[0]*adjacents[1])
                
        return sum(ratios)
        

if __name__ == "__main__":
    print(day03_part2_main())
