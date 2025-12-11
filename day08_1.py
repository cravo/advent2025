from collections import Counter

junction_box_data = [
"162,817,812",
"57,618,57",
"906,360,560",
"592,479,940",
"352,342,300",
"466,668,158",
"542,29,236",
"431,825,988",
"739,650,466",
"52,470,668",
"216,146,977",
"819,987,18",
"117,168,530",
"805,96,715",
"346,949,466",
"970,615,88",
"941,993,340",
"862,61,35",
"984,92,344",
"425,690,689"
]

def parse_box(box_str):
    return tuple(int(x) for x in box_str.split(','))
  
def connect_junction_boxes(junction_boxes, closest_pair):
    
    circuit1 = junction_boxes[closest_pair[0]]['circuit']
    circuit2 = junction_boxes[closest_pair[1]]['circuit']

    if circuit1 != circuit2:
        for box in junction_boxes:
            if box['circuit'] == circuit2:
                box['circuit'] = circuit1
        return True

    return False

def build_edges(points):
    edges = []
    n = len(points)
    for i in range(n):
        x1, y1, z1 = points[i]['x'], points[i]['y'], points[i]['z']
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]['x'], points[j]['y'], points[j]['z']
            dx = x1 - x2
            dy = y1 - y2
            dz = z1 - z2
            d2 = dx * dx + dy * dy + dz * dz
            edges.append((d2, i, j))
    edges.sort(key=lambda e: e[0])
    return edges

if __name__ == "__main__":

    with open("day08.txt", "r") as file:
        junction_box_data = file.readlines()

    junction_boxes = [{
        'x': pos[0],
        'y': pos[1],
        'z': pos[2],
        'circuit': i
    } for i, pos in enumerate([parse_box(box) for box in junction_box_data])]

    edges = build_edges(junction_boxes)

    connections = 0
    while connections < 1000:
        closest_pair = (edges[connections][1], edges[connections][2])
        connect_junction_boxes(junction_boxes, closest_pair)
        connections += 1


    circuit_counts = Counter(box['circuit'] for box in junction_boxes)
    sorted_circuit_counts = sorted(circuit_counts.items(), key=lambda item: item[1], reverse=True)
    for circuit_id, count in sorted_circuit_counts:
        print(f"Circuit {circuit_id}: {count} boxes")

    product = sorted_circuit_counts[0][1] * sorted_circuit_counts[1][1] * sorted_circuit_counts[2][1]
    print(f"Product of sizes of three largest circuits: {product}")
