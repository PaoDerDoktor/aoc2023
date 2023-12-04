def day4_part2_main() -> int:
    with open("day 04/inputs.txt", 'r') as inFile:
        cards: dict[int, tuple[set[int], list[int]]] = {int(line.split(': ')[0].split()[1]) : ({int(n) for n in line.split(': ')[1].split(" | ")[0].split()}, [int(n) for n in line.strip().split(': ')[1].split(" | ")[1].split()]) for line in inFile.readlines()}
        
        copies: dict[int, int] = {id: 1 for id in cards.keys()}
        
        for cardId, (winning, chosenList) in cards.items():
            chosen: set[int] = set(chosenList)
            if (matches:=len(chosen.intersection(winning))) != 0:
                for i in range(1, matches+1):
                    if cardId+i in copies.keys():
                        copies[cardId+i] += copies[cardId]
        
        return sum(copies.values())


if __name__ == "__main__":
    print(day4_part2_main())
