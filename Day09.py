class Day09:
    def part1(self, input_data):
        positions = []
        for line in input_data.splitlines():
            x, y = line.split(',')
            positions.append((x, y))

        # Convert positions to integers
        positions = [(int(x), int(y)) for x, y in positions]

        # Find the two positions that are furthest away
        max_distance = 0
        furthest_pair = None
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                x1, y1 = positions[i]
                x2, y2 = positions[j]
                distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
                if distance > max_distance:
                    max_distance = distance
                    furthest_pair = (positions[i], positions[j])

        print(f"Furthest pair: {furthest_pair}, Distance: {max_distance}")
        # Calculate area of rectangle formed by furthest pair
        (x1, y1), (x2, y2) = furthest_pair
        area = (abs(x2 - x1)+1) * (abs(y2 - y1)+1)
        print(f"Rectangle area: {area}")
        # print(positions)
        return area
    
    def part2(self, input_data):
        
        return None


if __name__ == "__main__":
    day = Day09()
    with open("day09/test.txt") as f:
    # with open("day09/input.txt") as f:
        input_data = f.read().strip()

    result_part1 = day.part1(input_data)
    print(f"Part 1 Result: {result_part1}")

    result_part2 = day.part2(input_data)
    print(f"Part 2 Result: {result_part2}")