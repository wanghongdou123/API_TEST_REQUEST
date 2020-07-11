from api.requests_wework.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()


    def test_create(self):
        print(self.address.create("zhangsan111", "wangwu", "13800000009"))


    def test_update(self):
        print(self.address.update("zhangsan111", "wangwu", "13800000010"))


    def test_delete(self):
        print(self.address.delete("zhangsan111"))