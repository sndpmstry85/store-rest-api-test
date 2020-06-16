from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest
# integration test - creates the item on and saves it to the database and then deletes and then confirms
# it has happened


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            StoreModel('test').save_to_db() # this allows us to add store id required when testing
                                            # db in mySQL and posgressql
            item = ItemModel('test', 19.99, 1)

            self.assertIsNone(ItemModel.find_by_name('test'),
                              "Found an item with name {}, but expected not to.".format(item.name))

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'))

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'))

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel ('test_store')
            item = ItemModel('test', 19.99, 1)#  item that uses the store id of '1'

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(item.store.name, 'test_store') # equal to the store created to 'test_store'
