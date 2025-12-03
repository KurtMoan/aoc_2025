class Day03:
    def part1(self, input_data):
        sum = 0
        for line in input_data.splitlines():
            print(line)
            first_digit = line[len(line)-2]
            first_digit_loc = len(line)-2
            print(f"First digit: {first_digit}")

            for i in range(len(line)-3, -1, -1):
                if int(line[i]) >= int(first_digit):
                    first_digit = line[i]
                    first_digit_loc = i
            print(f"New first digit: {first_digit}", f"at location {first_digit_loc}")
            second_digit = line[first_digit_loc+1]
            for i in range(first_digit_loc+1, len(line)):
                
                if int(line[i]) >= int(second_digit):
                    second_digit = line[i]
            print(f"Second digit: {second_digit}")
            sum += int(first_digit + second_digit)
        return sum

    def get_first_digit(self, line, location, length):
        print(f"Finding first digit in length {length}, starting at location {location}")
        first_digit = line[len(line)-length-1]
        first_digit_loc = len(line)-length-1
        print(f"Initial first digit: {first_digit} at location {first_digit_loc}")
        for i in range(len(line)-length-1, location-1, -1):
            if int(line[i]) >= int(first_digit):
                first_digit = line[i]
                first_digit_loc = i
                # print(f"New first digit: {first_digit} at location {first_digit_loc}")
        print(f"Final first digit: {first_digit} at location {first_digit_loc}")
        return first_digit, first_digit_loc
    
    def part2(self, input_data):
        sum = 0
        for line in input_data.splitlines():
            digits = ''
            length = 12
            location = 0
            print("-----")
            print(line)
            for l in range(length, 0, -1):
                first_digit, location = self.get_first_digit(line, location, l)
                print(f"First digit: {first_digit} at location {location}")
                digits += first_digit
                location += 1
            print(f"Digits so far: {digits}")
            sum += int(digits)
        return sum

if __name__ == "__main__":
    day = Day03()
    with open("day03/test.txt") as f:
    # with open("day03/input.txt") as f:
        input_data = f.read().strip()
    # print("Part 1:", day.part1(input_data))
    print("Part 2:", day.part2(input_data))