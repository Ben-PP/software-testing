import pytest
from .main import Queue, Queuer


class TestQueue:
    def test_add_one(self):
        # Arrange
        queue = Queue()
        # Act
        queue.add()
        # Assert
        assert queue.queue == [Queuer(id=1, position=1)]

    def test_add_two(self):
        # Arrange
        queue = Queue()
        # Act
        queue.add()
        queue.add()
        # Assert
        assert queue.queue == [
            Queuer(id=1, position=1),
            Queuer(id=2, position=2),
        ]

    def test_remove_first(self):
        # Arrange
        queue = Queue()
        queue.queue = [Queuer(id=1, position=1), Queuer(id=2, position=2)]
        # Act
        queue.remove(1)
        # Assert
        assert queue.queue == [Queuer(id=2, position=1)]

    def test_remove_from_middle(self):
        # Arrange
        queue = Queue()
        queue.queue = [
            Queuer(id=1, position=1),
            Queuer(id=2, position=2),
            Queuer(id=3, position=3),
        ]
        # Act
        queue.remove(1)
        # Assert
        assert queue.queue == [
            Queuer(id=2, position=1),
            Queuer(id=3, position=2),
        ]

    def test_remove_last(self):
        # Arrange
        queue = Queue()
        queue.queue = [Queuer(id=1, position=1), Queuer(id=2, position=2)]
        # Act
        queue.remove(2)
        # Assert
        assert queue.queue == [Queuer(id=1, position=1)]

    def test_remove_first_until_empty(self):
        # Arrange
        queue = Queue()
        queue.queue = [Queuer(id=1, position=1), Queuer(id=2, position=2)]
        # Act
        queue.remove(1)
        queue.remove(1)
        # Assert
        assert queue.queue == []

    def test_remove_from_empty(self):
        # Arrange
        queue = Queue()

        with pytest.raises(IndexError):  # Assert
            queue.remove(1)  # Act

    def test_remove_out_of_range(self):
        # Arrange
        queue = Queue()
        queue.queue = [Queuer(id=1, position=1)]

        with pytest.raises(IndexError):  # Assert
            queue.remove(3)  # Act

    def test_remove_first_method(self):
        queue = Queue()
        queue.queue = [
            Queuer(id=1, position=1),
            Queuer(id=2, position=2),
            Queuer(id=3, position=3),
            Queuer(id=4, position=4),
        ]
        id_to_remove = queue.queue[0].id
        queue.remove_first()

        assert id_to_remove not in [queuer.id for queuer in queue.queue]

    def test_remove_first_method_return_value(self):
        queue = Queue()
        queue.queue = [
            Queuer(id=1, position=1),
            Queuer(id=2, position=2),
            Queuer(id=3, position=3),
            Queuer(id=4, position=4),
        ]
        id_to_remove = queue.queue[0].id

        removed_queuer = queue.remove_first()

        assert removed_queuer.id == id_to_remove

    def test_remove_first_method_exception(self):
        queue = Queue()
        queue.queue = []

        with pytest.raises(RuntimeError):
            queue.remove_first()
