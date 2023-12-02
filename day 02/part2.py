def day02_part2_main() -> int:
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
        
        setsPowers: list[int] = []
        for gameId, game in games.items():
            r: int = 0
            g: int = 0
            b: int = 0
            
            for pack in game:
                if "red" in pack and pack["red"] > r:
                    r = pack["red"]
                
                if "green" in pack and pack["green"] > g:
                    g = pack["green"]
                
                if "blue" in pack and pack["blue"] > b:
                    b = pack["blue"]
            
            setsPowers.append(r*g*b)
        
        return sum(setsPowers)
        

if __name__ == "__main__":
    print(day02_part2_main())
