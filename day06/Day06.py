import re

class Day06:
    def part1(self, input_data):
        array = []
        total = 0
        for line in input_data.splitlines():
            array.append([x for x in line.split()])
        # print(array)
        
        operations = array[-1]
        for index, operation in enumerate(operations):
            sum = int(array[0][index])
            # print(f"Starting with {sum} for operation {operation} at index {index}")
            if operation == "*":
                for line in range(1, len(array)-1):
                    # print(f"Multiplying {sum} by {array[line][index]}")
                    sum *= int(array[line][index])
            elif operation == "+":
                for line in range(1, len(array)-1):
                    # print(f"Adding {sum} by {array[line][index]}")
                    sum += int(array[line][index])
            total += sum
        return total

    def parse_array(self, input_data):
        array = []
        operations = []
        for line in input_data.splitlines():
            array.append(line)
        print("operations:", array[-1])
        ops_line = array[-1]
        indexes = [i for i, ch in enumerate(ops_line) if ch in {'*', '+'}]
        indexes.append(len(array[-1]))
        print("indexes:", indexes)
        for chars in re.split('[*+\n]', input_data):
            operations.append(chars)
              
        print(operations)
        return None

    def calc(self, list, operations):
        total = 0
        
        return total
    
    def part2(self, input_data):
        array = []
        total = 0
        # for line in input_data.splitlines():
        #     array.append([x for x in re.split('[*+]', line)])
        # print(array)
        self.parse_array(input_data)
        # operations = array[-1]
        # for index, operation in enumerate(operations):
        #     sum = int(array[0][index])
        #     # print(f"Starting with {sum} for operation {operation} at index {index}")
        #     if operation == "*":
        #         for line in range(1, len(array)-1):
        #             # print(f"Multiplying {sum} by {array[line][index]}")
        #             sum *= int(array[line][index])
        #     elif operation == "+":
        #         for line in range(1, len(array)-1):
        #             # print(f"Adding {sum} by {array[line][index]}")
        #             sum += int(array[line][index])
        #     total += sum
        return total

if __name__ == "__main__":
    import sys
    day = Day06()
    with open("day06/test.txt") as f:
    # with open("day06/input.txt") as f:
        input_data = f.read().strip()
    # print("Part 1:", day.part1(input_data))
    print("Part 2:", day.part2(input_data))