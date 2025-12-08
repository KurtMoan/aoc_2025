class Day07:
    def print_array(self, array):
        for line in array:
            print("".join(line))
        print("\n")

    def part1(self, input_data):
        beams = []
        splits = 0
        for idxline, line in enumerate(input_data.splitlines()):
            beams.append([char for char in line])
            if(idxline == 0):
                continue
            if(idxline == 1):
                for idxchar, char in enumerate(beams[0]):
                    if char == "S":
                        beams[1][idxchar] = "|"
                        break
                continue
            for idxchar, char in enumerate(line):
                if(char == "."):
                    if(beams[idxline-1][idxchar] == "|"):
                        beams[idxline][idxchar] = "|"
                elif(char == "^"):                
                    if(beams[idxline-1][idxchar] == "|"):
                        beams[idxline][idxchar-1] = "|"
                        beams[idxline][idxchar+1] = "|"
                        splits += 1

            # print("beams after line:", idxline)
            # self.print_array(beams)
        return splits
    
    def part2(self, input_data):
        lines = input_data.splitlines()
        beam_counts = [0] * len(lines[0])
        beam_counts[lines[0].find("S")] = 1
        for line in lines:
            for i, char in enumerate(line):
                if char != "^":
                    continue
                count = beam_counts[i]
                if count > 0:
                    beam_counts[i-1] += count
                    beam_counts[i+1] += count
                    beam_counts[i] = 0

        return sum(count for count in beam_counts)
    

if __name__ == "__main__":
    day = Day07()
    # with open("day07/test.txt") as f:
    with open("day07/input.txt") as f:
        input_data = f.read()
    result1 = day.part1(input_data)
    print("Part 1 Result:", result1)
    result2 = day.part2(input_data)
    print("Part 2 Result:", result2)