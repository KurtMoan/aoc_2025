class Day05:
    def part1(self, input_data):
        # Implement the logic for part 1 here
        result = 0
        sections = input_data.strip().split('\n\n')
        ranges = sections[0].splitlines() if len(sections) > 0 else []
        ingredients = sections[1].splitlines() if len(sections) > 1 else []
        print("List 1:", ranges)
        print("List 2:", ingredients)
        for ingredient in ingredients:
            # Example processing logic
            ingredient_num = int(ingredient)
            for range_line in ranges:
                start, end = map(int, range_line.split('-'))
                if start <= ingredient_num <= end:
                    result += 1
                    break
        return result

    def process_ranges(self, ranges):
        new_ranges = []
        changed = False
        for range_line in ranges:
            start, end = map(int, range_line.split('-'))
            processed = False
            for n_start, n_end in new_ranges:
                # inside existing range
                if n_start <= start <= n_end and n_start <= end <= n_end:
                    processed = True
                    changed = True
                    break
                # overlaps existing range
                if start <= n_start <= end or start <= n_end <= end:
                    new_start = min(start, n_start)
                    new_end = max(end, n_end)
                    new_ranges.remove((n_start, n_end))
                    new_ranges.append((new_start, new_end))
                    processed = True
                    changed = True
                    break
                
            #new range outside existing ranges
            if not processed:
                new_ranges.append((start, end))
        return new_ranges, changed

    def part2(self, input_data):
        # Implement the logic for part 2 here
        result = 0
        sections = input_data.strip().split('\n\n')
        ranges = sections[0].splitlines() if len(sections) > 0 else []
        new_ranges = []
        changes = False
        rounds = 0
        while True:
            rounds += 1
            print(f"Round {rounds}:")
            new_ranges, changes = self.process_ranges(ranges)
            if not changes:
                break
            ranges = [f"{start}-{end}" for start, end in new_ranges]
        
        print("Merged Ranges:", new_ranges)

        for n_start, n_end in new_ranges:
            print(f"adding range from {n_start} to {n_end}")
            result += (int(n_end) - int(n_start) + 1)
        return result
    
if __name__ == "__main__":
    import sys
    day = Day05()
    # with open("day05/test.txt") as f:
    with open("day05/input.txt") as f:
        input_data = f.read().strip()
    # print("Part 1:", day.part1(input_data))
    print("Part 2:", day.part2(input_data))