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

    def part2(self, input_data):
        # Implement the logic for part 2 here
        result = 0
        sections = input_data.strip().split('\n\n')
        ranges = sections[0].splitlines() if len(sections) > 0 else []
        new_ranges = []
        for range_line in ranges:
            start, end = map(int, range_line.split('-'))
            print(f"Processing range {start}-{end}")
            processed = False
            for n_start, n_end in new_ranges:
                print(f" Comparing with existing range {n_start}-{n_end}")
                # inside existing range
                if n_start <= start <= n_end and n_start <= end <= n_end:
                    print(f" --> Range {start}-{end} is inside existing range {n_start}-{n_end}")
                    processed = True
                    break
                # overlaps existing range
                if start <= n_start <= end or start <= n_end <= end:
                    print(f" --> Range {start}-{end} overlaps existing range {n_start}-{n_end}")
                    new_start = min(start, n_start)
                    new_end = max(end, n_end)
                    new_ranges.remove((n_start, n_end))
                    new_ranges.append((new_start, new_end))
                    processed = True
                    break
                
            #new range outside existing ranges
            if not processed:
                print(f" --> Adding new range {start}-{end}")
                new_ranges.append((start, end))
        
        print("Merged Ranges:", new_ranges)

        for n_start, n_end in new_ranges:
            for i in range(n_start, n_end + 1):
                result.add(i)
        return len(result)
    
if __name__ == "__main__":
    import sys
    day = Day05()
    # with open("day05/test.txt") as f:
    with open("day05/input.txt") as f:
        input_data = f.read().strip()
    # print("Part 1:", day.part1(input_data))
    print("Part 2:", day.part2(input_data))