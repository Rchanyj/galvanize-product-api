from services.product_storage import ProductStorage


def test_create_product():
    product_storage = ProductStorage()
    product_storage.init()

    product_data = {
        'name': 'Test1',
        'price': 20
    }

    product_storage.create_product(product_data)
    product_data = product_storage.get_product(4)

    assert product_data[0] == 4
    assert product_data[1] == 'Test1'
    assert product_data[2] == 20
    assert product_data[3] is None
    assert product_data[4] == 0
    assert product_data[5] is True


def test_get_product():
    product_storage = ProductStorage()
    product_storage.init()

    id = 2
    product_data = product_storage.get_product(id)

    assert (len(product_data), product_data[0]) == (6, 2)
