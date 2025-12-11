class Day08:
    def part1(self, input_data):
        # Implement the logic for part 1 here
        lines = input_data.splitlines()
        nodes = [list(map(int, line.split(','))) for line in lines]
        nodes_connected = []
        distances = []
        for idx, node in enumerate(nodes):
            for node2 in nodes[idx + 1:]:
                distance = ((node[0] - node2[0])**2 + (node[1] - node2[1])**2 + (node[2] - node2[2])**2)**0.5
                distances.append((distance, (node, node2)))
        print(f"Total distances to process: {len(distances)}")
        i = 0
        for distance, (node, node2) in sorted(distances, key=lambda x: x[0]):
            i+=1
            print(distance, node, node2)
            processed = 0
            for group in nodes_connected:
                if (node in group or node2 in group) and not processed:
                    if node in group and node2 in group:
                        # print(f"--> Both {node} and {node2} are in group {group}")
                        i-=1
                        processed = 3
                        break
                    if node in group and node2 not in group:
                        if processed == 2:
                            # print(f"--> Merging groups because {node} is in group {group} and {node2} is in another group")
                            for g in nodes_connected:
                                if node2 in g:
                                    group.extend(g)
                                    nodes_connected.remove(g)
                                    break
                            processed = 3
                            break
                        group.append(node2)
                        # print(f"--> Added {node2} to group {group}")
                        processed = 1
                        break
                    if node2 in group and node not in group:
                        if processed == 1:
                            # print(f"--> Merging groups because {node2} is in group {group} and {node} is in another group")
                            for g in nodes_connected:
                                if node in g:
                                    group.extend(g)
                                    nodes_connected.remove(g)
                                    break
                            processed = 3
                            break
                        # print(f"--> Added {node} to group {group}")
                        processed = 2
                        break
            if processed == 0:
                nodes_connected.append([node, node2])
                # print(f"--> Created new group with {node} and {node2}")
            if i>1000:
                break
            
        nodes_connected.sort(key=lambda group: len(group), reverse=True)
        print(f"Group {0}({len(nodes_connected[0])}): {nodes_connected[0]}")
        print(f"Group {1}({len(nodes_connected[1])}): {nodes_connected[1]}")
        print(f"Group {2}({len(nodes_connected[2])}): {nodes_connected[2]}")
        return len(nodes_connected[0]) * len(nodes_connected[1]) * len(nodes_connected[2])

    def part2(self, input_data):
        # Implement the logic for part 2 here
        return None

if __name__ == "__main__":
    day = Day08()
    # with open("day08/test.txt") as f:
    with open("day08/input.txt") as f:
        input_data = f.read().strip()
    print("Part 1:", day.part1(input_data))
    print("Part 2:", day.part2(input_data))