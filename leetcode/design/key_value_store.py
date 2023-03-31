class KeyValueStore:
    def __init__(self):
        self.store = {}
        self.transaction_stack = []

    def set(self, key, value):
        if self.transaction_stack:
            current_transaction = self.transaction_stack[-1]
            current_transaction[key] = value
        else:
            self.store[key] = value

    def get(self, key):
        if self.transaction_stack:
            current_transaction = self.transaction_stack[-1]
            if key in current_transaction:
                return current_transaction[key]
        if key in self.store:
            return self.store[key]
        return None

    def delete(self, key):
        if self.transaction_stack:
            current_transaction = self.transaction_stack[-1]
            current_transaction[key] = None
        else:
            del self.store[key]

    def begin(self):
        self.transaction_stack.append({})

    def rollback(self):
        if self.transaction_stack:
            self.transaction_stack.pop()

    def commit(self):
        print(self.transaction_stack)
        if self.transaction_stack:
            current_transaction = self.transaction_stack[-1]
            for key, value in current_transaction.items():
                if value is None:
                    del self.store[key]
                else:
                    self.store[key] = value
            self.transaction_stack.pop()

def test_key_value_store():
    kvs = KeyValueStore()

    # Test set() and get()
    kvs.set('key1', 'value1')
    assert kvs.get('key1') == 'value1'

    # Test delete() and get()
    kvs.delete('key1')
    assert kvs.get('key1') is None

    # Test nested transactions
    kvs.set('key2', 'value2')
    kvs.begin()
    kvs.set('key2', 'new_value')
    assert kvs.get('key2') == 'new_value'
    # kvs.begin()
    # kvs.set('key2', 'even_newer_value')
    # assert kvs.get('key2') == 'even_newer_value'
    # kvs.rollback()
    # assert kvs.get('key2') == 'new_value'
    # kvs.commit()
    # assert kvs.get('key2') == 'new_value'
    #
    # # Test commit() and rollback()
    # kvs.begin()
    # kvs.set('key3', 'value3')
    # assert kvs.get('key3') == 'value3'
    # kvs.begin()
    # kvs.set('key3', 'new_value3')
    # assert kvs.get('key3') == 'new_value

test_key_value_store()