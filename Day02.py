import re

class Day02:
    def part1(self, input_data):
        total = 0
        for data in input_data.split(","):
            start = data.split("-")[0]
            end = data.split("-")[1]
            # print ("Processing data:", start , "-->", end)
            for num in range(int(start), int(end)+1):
                str_num = str(num)
                str_num_len = len(str_num)
                if(str_num_len % 2) != 0:
                    # print ("Skipping number (odd length):", str_num)
                    continue
                first_half = str_num[0:str_num_len//2]
                second_half = str_num[str_num_len//2:str_num_len]
                # print ("First Half:", first_half, "Second Half:", second_half)
                if first_half == second_half:
                    total += num
                    # print ("Found match in number:", str_num, "First Half:", first_half, "Second Half:", second_half)

        print("Total", total)

    def part2(self, input_data):
        total = 0
        for data in input_data.split(","):
            start = data.split("-")[0]
            end = data.split("-")[1]
            print ("Processing data:", start , "-->", end)
            for num in range(int(start), int(end)+1):
                str_num = str(num)
                if re.fullmatch(rf'(.*?)\1+', str_num):
                    total += num
                    continue

        print("Total", total)


if __name__ == "__main__":
    day = Day02()
    with open("day02/test.txt") as f:
    # with open("day02/input.txt") as f:
        input_data = f.read().strip()

    result_part1 = day.part1(input_data)
    print(f"Part 1 Result: {result_part1}")

    result_part2 = day.part2(input_data)
    print(f"Part 2 Result: {result_part2}")