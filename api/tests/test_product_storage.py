from services.product_storage import ProductStorage


def test_create_product_creates_product():
    product_storage = ProductStorage()
    product_storage.init()

    product_data = {
        'name': 'Test1',
        'price': 20
    }

    product_storage.create_product(product_data)
    product_data = product_storage.get_product(7)

    assert product_data[0] == 7
    assert product_data[1] == 'Test1'
    assert product_data[2] == 20
    assert product_data[3] is None
    assert product_data[4] == 0
    assert product_data[5] is True


def test_get_product_returns_product():
    product_storage = ProductStorage()
    product_storage.init()

    id = 2
    product_data = product_storage.get_product(id)

    assert (len(product_data), product_data[0]) == (6, 2)


def test_get_most_viewed_returns_more_than_one_view_desc():
    product_storage = ProductStorage()
    product_storage.init()

    products_data = product_storage.get_most_viewed()

    assert len(products_data) == 4
    assert products_data[0][0] == 3
    assert products_data[1][0] == 2
    assert products_data[2][0] == 4
    assert products_data[3][0] == 5


def test_deactivate_product_inactivates_product():
    product_storage = ProductStorage()
    product_storage.init()

    product_storage.deactivate_product(1)
    product_data = product_storage.get_product(1)

    assert product_data == {}
