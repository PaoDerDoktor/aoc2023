def day4_part1_main() -> int:
    with open("day 04/inputs.txt", 'r') as inFile:
        cards: dict[int, tuple[set[int], list[int]]] = {int(line.split(': ')[0].split()[1]) : ({int(n) for n in line.split(': ')[1].split(" | ")[0].split()}, [int(n) for n in line.strip().split(': ')[1].split(" | ")[1].split()]) for line in inFile.readlines()}
        
        scores: list[int] = []
        
        for _, (winning, chosenList) in cards.items():
            chosen: set[int] = set(chosenList)
            if (cardinal:=len(chosen.intersection(winning))) != 0:
                scores.append(2**(cardinal-1))
        
        return sum(scores)


if __name__ == "__main__":
    print(day4_part1_main())
