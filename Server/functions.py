import custom_errors as error
from c_point import point

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    """print('Texts:')"""

    for text in texts:
        """print('\n"{}"'.format(text.description))"""
        f = open("./receipts/receipt_text.txt", "a")
        f.write('{}\n'.format(text.description))
        f.close()

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        """print('bounds: {}'.format(','.join(vertices)))"""
        f = open("./bounds/receipt_bounds.txt", "a")
        f.write('{} bounds: {}\n'.format(text.description, ','.join(vertices)))
        f.close()

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

def get_midpoint(point_a, point_b):
    return_point = point((point_b.x+point_a.x)/2, (point_b.y+point_a.y)/2)
    return return_point

def get_slope(point_a, point_b):
    try:
        if type(point_a) is point and type(point_b) is point:
            # get the slope of the line and return it
            slope = (point_b.get_y() - point_a.get_y())/(point_b.get_x() - point_a.get_x())
            return slope
        else:
            raise error.invalid_param
    except Exception as err:
        print(err)

def is_on_line(point_a, point_b, slope):
    # print(f"point_a: {point_a.get_x()}, {point_a.get_y()}")
    # print(f"point_b: {point_b.get_x()}, {point_b.get_y()}")
    # print(f"slope: {slope}")

    # y2 = m(x2-x1) + y1
    # print(point_b.get_y())
    # print(slope*(point_b.get_x()-point_a.get_x()) + point_a.get_y())

    try:
        if point_b.get_y() == (slope * (point_b.get_x()-point_a.get_x()) + point_a.get_y()):
            print("the points are on the line")
        else:
            raise error.not_on_line

    except Exception as err:
        print(err)
       