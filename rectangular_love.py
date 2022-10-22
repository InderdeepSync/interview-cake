
def find_range_overlap(range1, range2):
    if not (range1[0] <= range2[0]):
        range1, range2 = range2, range1

    if range1[1] <= range2[0]:
        return None

    return [range2[0], min(range1[1], range2[1])]


def find_rectangular_overlap(rect1, rect2):
    range_x = find_range_overlap([rect1['left_x'], rect1['left_x'] + rect1['width'] - 1], [rect2['left_x'], rect2['left_x'] + rect2['width'] - 1])
    range_y = find_range_overlap([rect1['bottom_y'], rect1['bottom_y'] + rect1['height'] - 1], [rect2['bottom_y'], rect2['bottom_y'] + rect2['height'] - 1])

    if not range_x or not range_y:
        return {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }

    bottom_y, top_y = range_y
    left_x, right_x = range_x

    return {
        'left_x': left_x,
        'bottom_y': bottom_y,
        'width': right_x - left_x + 1,
        'height': top_y - bottom_y + 1,
    }


if __name__ == "__main__":
    rect_one = {
        'left_x': 1,
        'bottom_y': 2,
        'width': 3,
        'height': 4,
    }
    rect_two = {
        'left_x': 4,
        'bottom_y': 3,
        'width': 2,
        'height': 2,
    }

    print(find_rectangular_overlap(rect_one, rect_two))
