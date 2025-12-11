class Day04:
    def part1(self, input_data):
        array = [list(line) for line in input_data.split('\n')]
        array2 = [row.copy() for row in array]
        # for row in array:
        #     print(''.join(row))
        for r in range(len(array)):
            for c in range(len(array[0])):
                if array[r][c] == '@':
                    count = 0
                    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < len(array) and 0 <= nc < len(array[0]) and array[nr][nc] == '@':
                            count += 1
                    if count < 4:
                        array2[r][c] = 'x'
        # print("After processing:")
        # for row in array2:
        #     print(''.join(row))
        
        antall = sum(row.count('x') for row in array2)
        return antall

    def array_processing(self, array):
        array2 = [row.copy() for row in array]
        for r in range(len(array)):
            for c in range(len(array[0])):
                if array[r][c] == '@':
                    count = 0
                    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < len(array) and 0 <= nc < len(array[0]) and array[nr][nc] == '@':
                            count += 1
                    if count < 4:
                        array2[r][c] = 'x'
        return array2
    
    def part2(self, input_data):
        array = [list(line) for line in input_data.split('\n')]
        total = 0
        while True:
            array = self.array_processing(array)
            antall = sum(row.count('x') for row in array)
            array = [[c if c != 'x' else '.' for c in row] for row in array]
            total += antall
            if antall == 0:
                break
        return total

if __name__ == "__main__":
    day = Day04()
    # with open("day04/test.txt") as f:
    with open("day04/input.txt") as f:
        input_data = f.read().strip()
    # print("Part 1:", day.part1(input_data))
    print("Part 2:", day.part2(input_data))