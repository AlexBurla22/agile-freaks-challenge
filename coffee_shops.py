import sys
import pandas as pd
import math

def get_arguments(argv):
    if(len(argv) != 3):
        print('Please provide input as <user x coordinate> <user y coordinate> <shop data url>')
        x_coord = 0
        y_coord = 0
        url = ''
    else:
        try:
            x_coord = float(argv[0])
            y_coord = float(argv[1])
        except ValueError:
            print('Not a float')
        url = argv[2]
    return x_coord, y_coord, url

def get_data(url):
    return pd.read_csv(url, names=['name', 'x_coord', 'y_coord'])

def calculate_distances(data, position):
    return pd.DataFrame(data).apply(calculate_distance, args=(position,), axis=1)

def calculate_distance(row, position):
    shop_position = float(row['x_coord']), float(row['y_coord'])
    return math.sqrt(math.pow(shop_position[0] - position[0], 2) + math.pow(shop_position[1] - position[1], 2))

def main(argv):
    x, y, url = get_arguments(argv)
    if(url != ''):
        shops = get_data(url)
        list_distances = calculate_distances(shops, (x, y))
    input('Press enter to exit...')
 
if __name__ == "__main__":
    main(sys.argv[1:])