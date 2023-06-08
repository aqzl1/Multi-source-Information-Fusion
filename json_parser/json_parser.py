import ijson

def generator(file_path):
    with open(file_path, "r") as f:
        matrix = ijson.items(f, 'annotations.item.segmentation.item', use_float = True)
        for mat in matrix:
            yield list(mat)


if __name__ == '__main__':
    pois = generator(r".\train_test2017.json")
    for poi in pois:
        print(poi)