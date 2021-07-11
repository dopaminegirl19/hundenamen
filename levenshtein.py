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
        
def levenshtein(a, b):
    if not a: return len(b)
    if not b: return len(a)
    return min(levenshtein(a[1:], b[1:])+(a[0] != b[0]),
               levenshtein(a[1:], b)+1,
               levenshtein(a, b[1:])+1)
 
def run():   
    with open(input.csvname) as csv_file:
        for line in csv_file.readlines():
            array = line.split(',')
            names.append(array[0])

    for name in names:
        if levenshtein(name, "Luca"):
            oknames.append(name)
            
    print(", ".join(oknames))
    

if __name__ == '__main__':
    run()