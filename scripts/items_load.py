import csv

from hello.models import Item, ItemFeatures


def run():
    fhanditems = open('../data/items.csv')
    fhandsneakers = open('../data/sneakers.csv')
    fhandduck = open('../data/duck.csv')
    fhandhand_sanit = open('../data/hand_sanitizer.csv')
    fhandheadphones = open('../data/headphones.csv')
    fhandotters = open('../data/otter.csv')
    count = 0

    reader_items = csv.reader(fhanditems)
    reader_descriptions = [csv.reader(fhandsneakers), csv.reader(fhandheadphones), csv.reader(fhandotters),
                           csv.reader(fhandduck), csv.reader(fhandhand_sanit)]

    Item.objects.all().delete()
    ItemFeatures.objects.all().delete()

    for row in reader_items:
        i, created = Item.objects.get_or_create(title=row[0], description=row[1], price=row[2], picture=row[3])
        for description in reader_descriptions[count]:
            d, created = ItemFeatures.objects.get_or_create(feature=description, item=i)

    fhanditems.close()
    fhandsneakers.close()
    fhandduck.close()
    fhandhand_sanit.close()
    fhandheadphones.close()
    fhandotters.close()


