from models.item import ItemModel
from models.store import StoreModel

from tests.base_test import BaseTest


class StoreTest(BaseTest):
    def test_create_store_items_empty(self): # creating store model
        store = StoreModel('test')

        self.assertListEqual(store.items.all(),[],
                             "The store's items length was not 0 even though no items were added.")# this code tests
        # that the items is a empty list and displays error message

    def test_crud(self): # this is testing save and updating (writing) into database which needs app context
        with self.app_context(): # when we are saving a store to database it does not need any items
            store = StoreModel('test') # create object (store)

            self.assertIsNone(StoreModel.find_by_name('test')) # check it does not exist

            store.save_to_db()  # save to database to make it exist

            self.assertIsNotNone(StoreModel.find_by_name('test')) # check that it does exist

            store.delete_from_db()  # delete from database

            self.assertIsNone(StoreModel.find_by_name('test')) # check that it now does not exist

    def test_store_relationship(self): # this is testing the relationships with items
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test_item')

    def test_store_json(self): # this is checking the database returns entry
        store = StoreModel('test')
        expected = {
            'id': None,
            'name': 'test',
            'items': []
        }

        self.assertDictEqual(store.json(), expected)

    def test_store_json_with_item(self): # this is checking the database returns entry with item
        with self.app_context():
            store = StoreModel('test')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()
            expected = {
                'id': 1,
                'name': 'test',
                'items': [{'name': 'test_item', 'price': 19.99}]
            }

            self.assertDictEqual(store.json(), expected)