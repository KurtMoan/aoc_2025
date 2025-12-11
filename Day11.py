from functools import cache
class Day11:
    @cache
    def get_number_of_paths(self, device, input_data, visited):
        connections = {}
        for line in input_data.splitlines():
            dev, paths = line.split(': ')
            path_list = paths.split(' ')
            # print(f"Device: {dev}, Paths: {path_list}")
            connections[dev] = path_list
        if device not in connections or device == 'out':
            if 'dac' in visited and 'fft' in visited:
                return 1  # Invalid path if 'eee' has been visited
            return 0  # No further paths

        total_paths = 0
        for next_device in connections[device]:
            if next_device not in visited:
                visited += ' ' + next_device
                total_paths += self.get_number_of_paths(next_device, input_data, visited)
                visited = visited.rsplit(' ', 1)[0]  # Backtrack
        return total_paths

    def part1(self, input_data):
        connections = {}
        for line in input_data.splitlines():
            dev, paths = line.split(': ')
            path_list = paths.split(' ')
            # print(f"Device: {dev}, Paths: {path_list}")
            connections[dev] = path_list
            c = list(connections.items())

        result = self.get_number_of_paths('you', c, 'you')
        return result

        

    def part2(self, input_data):
        result = self.get_number_of_paths('svr', input_data, 'svr')
        return result


if __name__ == "__main__":
    day = Day11()
    # with open("day11/test2.txt") as f:
    with open("day11/input.txt") as f:
        input_data = f.read().strip()

    # result_part1 = day.part1(input_data)
    # print(f"Part 1 Result: {result_part1}")

    result_part2 = day.part2(input_data)
    print(f"Part 2 Result: {result_part2}")