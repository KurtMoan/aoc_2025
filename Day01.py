class Day01:
    def part1(self, input_data):
        total = 0
        position = 50
        for line in input_data.splitlines():
            direction = line[0]
            distance = int(line[1:])
            print("Direction:", direction, "Distance:", distance)
            if direction == 'L':
                position -= distance
            elif direction == 'R':
                position += distance
            
            if position == 0:
                hundreds = (abs(position) // 100) + 1
                position += hundreds * 100
            if position >= 100:
                hundreds = position // 100
                position -= hundreds * 100
            
            print ("Current Position:", position)
            if position == 0:
                total += 1

        print("Code", total)
    
    def part2(self, input_data):
        total = 0
        position = 50
        pp = 50
        for line in input_data.splitlines():
            pp = position
            direction = line[0]
            distance = int(line[1:])
            hundreds = distance // 100
            distance = distance % 100
            total += hundreds
            # print("Direction:", direction, "Distance:", distance)
            if direction == 'L':
                position -= distance
            elif direction == 'R':
                position += distance
            
            if position == 0:
                total += 1
            elif position < 0:
                position += 100
                if pp != 0:
                    total += 1
            elif position >= 100:
                position -= 100
                total += 1
            
            # total += hundreds
            if direction == 'L':
                print ("input:", line, "## Position:", position, " <-- ", pp, "Hundreds Crossed:", hundreds, "Total:", total)   
            else:    
                print ("input:", line, "## Position:", pp, " --> ", position, "Hundreds Crossed:", hundreds, "Total:", total)   

        print("Code", total)
    
if __name__ == "__main__":
    day = Day01()
    with open("day01/test.txt") as f:
    # with open("day01/input.txt") as f:
        input_data = f.read().strip()

    result_part1 = day.part1(input_data)
    print(f"Part 1 Result: {result_part1}")

    result_part2 = day.part2(input_data)
    print(f"Part 2 Result: {result_part2}")
