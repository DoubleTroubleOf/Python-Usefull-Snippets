from myapp.models import MyModel

def create_duplicates():
    objects = list(MyModel.objects.all())
    for index in range(len(objects)):
        item = objects[index]
        item.pk=None    # set object pk to None.
        item.product_id = hash(item.product_id) # generate new value for unique fields
        item.save() # save object as new row in DB
        item.drops.clear()  # clear foreign keys exists and needed


if __name__ == '__main__':
    print("Object before duplicating:  ", MyModel.objects.all().count())
    create_duplicates()
    print("Object after duplicating:  ", MyModel.objects.all().count())
