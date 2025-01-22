class FlatIterator:

    def __init__(self, list_of_list):
        """Список атрибутов класса"""
        self.list_of_list = list_of_list

    def __iter__(self):
        """Список атрибутов для итерации по текущему списку"""
        self.current_list_iterator = iter(self.list_of_list)
        self.list_iterators = []
        return self

    def __next__(self):
        """Функция для определения следующего элемента в списке списков, возвращает этот элемент"""
        while True:
            try:
                item = next(self.current_list_iterator)
            except StopIteration:
                if not self.list_iterators:
                    raise StopIteration
                else:
                    self.current_list_iterator = self.list_iterators.pop()
                    continue
            if type(item) == list:
                self.list_iterators.append(self.current_list_iterator)
                self.current_list_iterator = iter(item)
            else:
                return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()