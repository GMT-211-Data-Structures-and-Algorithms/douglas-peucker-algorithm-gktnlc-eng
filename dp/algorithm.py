import math
import json

def perpendicular_distance(point, line_start, line_end):
    x0, y0 = point
    x1, y1 = line_start
    x2, y2 = line_end

    dx = x2 - x1
    dy = y2 - y1

    # since start and end are the same point, we just calculate the direct distance
    if dx == 0 and dy == 0:
        return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)

    numerator = abs(dy * x0 - dx * y0 + x2 * y1 - y2 * x1)
    denominator = math.sqrt(dx**2 + dy**2)
    return numerator / denominator


def douglas_peucker(points, epsilon):
    # we need at least 3 points to do anything meaningful
    if len(points) < 3:
        return points

    dmax = 0
    index = 0

    # going through each middle point to find the one farthest from the line
    for i in range(1, len(points) - 1):
        d = perpendicular_distance(points[i], points[0], points[-1])
        if d > dmax:
            dmax = d
            index = i

    if dmax > epsilon:
        # this point is too far away so we keep it and split the line here
        left = douglas_peucker(points[:index + 1], epsilon)
        right = douglas_peucker(points[index:], epsilon)
        return left[:-1] + right
    else:
        # all points are close enough to the line so we can safely remove them
        return [points[0], points[-1]]
    import json

def convert_coordinates_to_line(input_file):
    # reading the text file line by line and turning each one into a point
    points = []
    with open(input_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            x, y = float(parts[0]), float(parts[1])
            points.append((x, y))
    return points


def execute_douglas_peucker(input_file, output_file, epsilon):
    # loading the geojson file
    with open(input_file, 'r') as f:
        geojson = json.load(f)

    for feature in geojson.get('features', []):
        geometry = feature.get('geometry', {})
        geo_type = geometry.get('type', '')

        if geo_type == 'LineString':
            points = [(c[0], c[1]) for c in geometry['coordinates']]
            simplified = douglas_peucker(points, epsilon)
            geometry['coordinates'] = [[p[0], p[1]] for p in simplified]

        elif geo_type == 'MultiLineString':
            new_lines = []
            for line in geometry['coordinates']:
                points = [(c[0], c[1]) for c in line]
                simplified = douglas_peucker(points, epsilon)
                new_lines.append([[p[0], p[1]] for p in simplified])
            geometry['coordinates'] = new_lines

    # writing the simplified result to the output file
    with open(output_file, 'w') as f:
        json.dump(geojson, f)

    print("Done: " + output_file)