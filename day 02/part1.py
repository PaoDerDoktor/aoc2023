def day02_part1_main() -> int:
    with open("day 02/inputs.txt", 'r') as inFile:
        data: list[str] = [line.strip() for line in inFile.readlines()]
        
        games: dict[int, list[dict[str, int]]] = {}
        
        for entry in data:
            gameId: int = int(entry.split()[1][:-1])
            
            cubes: list[dict[str, int]] = []
            
            packsStrings: list[str] = entry.split(': ')[1].split('; ')
            
            for packString in packsStrings:
                unit: dict[str, int] = {}
                
                pairsStrings: list[str] = packString.split(', ')
                
                for pairString in pairsStrings:
                    descString: list[str] = pairString.split()
                    
                    unit[descString[1]] = int(descString[0])
                
                cubes.append(unit)
            
            games[gameId] = cubes
        
        possibleIDs: list[int] = []
        for gameId, game in games.items():
            possible: bool = True
            
            for pack in game:
                if pack.get("red", 0) > 12:
                    possible = False
                    break
                
                if pack.get("green", 0) > 13:
                    possible = False
                    break
                
                if pack.get("blue", 0) > 14:
                    possible = False
                    break
            
            if possible:
                possibleIDs.append(gameId)
        
        return sum(possibleIDs)
        

if __name__ == "__main__":
    print(day02_part1_main())
