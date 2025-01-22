class FlatIterator:

    def __init__(self, list_of_list):
        """Список атрибутов класса"""
        self.list_of_list = list_of_list

    def __iter__(self):
        """Список атрибутов для итерации по текущему списку"""
        self.list_iterator = iter(self.list_of_list)
        self.new_list = []
        self.current_position = -1
        return self

    def __next__(self):
        """Функция для определения следующего элемента в списке списков, возвращает этот элемент"""
        self.current_position += 1
        if len(self.new_list) == self.current_position:
            self.new_list = None
            self.current_position = 0
            if self.new_list is None:
                self.new_list = next(self.list_iterator)
        item = self.new_list[self.current_position]
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()