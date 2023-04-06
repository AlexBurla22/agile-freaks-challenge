import sys
import pandas as pd

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
    return pd.read_csv(url)

def main(argv):
    x, y, url = get_arguments(argv)
    if(url != ''):
        shops = get_data(url)
        print(shops)
    input('Press enter to exit...')

if __name__ == "__main__":
    main(sys.argv[1:])