class Day10:
    def part1(self, input_data):
        total = 0
        # Implement part 1 logic here
        print("Code", total)
    
    def part2(self, input_data):
        total = 0
        # Implement part 2 logic here
        print("Code", total)

if __name__ == "__main__":
    day = Day10()
    with open("day10/test.txt") as f:
    # with open("day10/input.txt") as f:
        input_data = f.read().strip()

    result_part1 = day.part1(input_data)
    print(f"Part 1 Result: {result_part1}")

    result_part2 = day.part2(input_data)
    print(f"Part 2 Result: {result_part2}")