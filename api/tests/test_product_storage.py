from services.product_storage import ProductStorage


def test_get_product():
    product_storage = ProductStorage()
    product_storage.init()

    id = 2
    product_data = product_storage.get_product(id)

    assert (len(product_data), product_data[0]) == (6, 2)

def test
