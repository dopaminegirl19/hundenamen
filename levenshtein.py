import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    '--csvname',
    default='20210103_hundenamen.csv',
    help='provide an string path to input .csv file'
)

input = parser.parse_args()

names = []
oknames = []
        
def l_dist(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(l_dist(a[1:], b[1:])+(a[0] != b[0]),
               l_dist(a[1:], b)+1,
               l_dist(a, b[1:])+1)
 
def run():   
    with open('20210103_hundenamen.csv') as csv_file:
        for line in csv_file.readlines():
            array = line.split(',')
            names.append(array[0])

    for name in sorted(set(names)):
        if abs(len(name) - len('"Luca"')) > 1:
            pass # make process faster as we are looking for max 1 insertion or deletion
        elif l_dist(name, '"Luca"') == 1:
            oknames.append(name)
            
    print(", ".join(oknames))
    

if __name__ == '__main__':
    run()