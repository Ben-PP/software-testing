from pytest import fixture, raises
from .todo_list import TodoList


class TestTodoList:

    @fixture
    def todo_list(self) -> TodoList:
        todos = TodoList()
        todos.todos = [
            {"id": 1, "description": "task 1", "completed": False},
            {"id": 2, "description": "task 2", "completed": False},
            {"id": 3, "description": "task 3", "completed": False},
            {"id": 4, "description": "task 4", "completed": True},
        ]
        return todos

    @fixture
    def empty_todo_list(self) -> TodoList:
        return TodoList()

    class TestGetTodo:
        def test_get_todo_by_id(self, todo_list: TodoList):
            id_to_get_1 = 1
            id_to_get_2 = 2
            id_to_get_3 = 3

            todo1 = todo_list.get_todo(id_to_get_1)
            todo2 = todo_list.get_todo(id_to_get_2)
            todo3 = todo_list.get_todo(id_to_get_3)

            assert todo1.get("id") == id_to_get_1
            assert todo2.get("id") == id_to_get_2
            assert todo3.get("id") == id_to_get_3

        def test_get_todo_last_id(self, todo_list: TodoList):
            last_id = len(todo_list.todos)
            last_todo = todo_list.get_todo(last_id)

            assert last_todo.get("id") == last_id

        def test_get_todo_non_existing_id(self, todo_list: TodoList):
            non_existing_id = 100

            with raises(ValueError):
                todo_list.get_todo(non_existing_id)

        def test_get_todo_negative_id(self, todo_list: TodoList):
            negative_id = -1

            with raises(ValueError):
                todo_list.get_todo(negative_id)

    class TestAddTodo:
        def test_add_todo(self, todo_list: TodoList):
            task = "new task"
            old_todo_count = len(todo_list.todos)

            new_todo = todo_list.add_todo(task)

            assert new_todo.get("description") == task
            assert new_todo.get("completed") is False
            assert len(todo_list.todos) == old_todo_count + 1
            assert new_todo.get("id") == old_todo_count + 1

    class TestCompleteTodo:
        def test_complete_todo(self, todo_list: TodoList):
            id_to_complete = 1

            todo_list.complete_todo(id_to_complete)

            assert todo_list.get_todo(id_to_complete).get("completed") is True

        def test_complete_todo_non_existing_id(self, todo_list: TodoList):
            non_existing_id = 100

            with raises(ValueError):
                todo_list.complete_todo(non_existing_id)

    class TestDeleteTodo:

        def test_delete_todo_first(self, todo_list: TodoList):
            id_to_delete = todo_list.todos[0].get("id")
            old_todo_count = len(todo_list.todos)

            deleted_todo = todo_list.delete_todo(id_to_delete)

            assert deleted_todo.get("id") == id_to_delete
            assert len(todo_list.todos) == old_todo_count
            with raises(ValueError):
                todo_list.get_todo(id_to_delete)

        def test_delete_todo_middle(self, todo_list: TodoList):
            id_to_delete = 2
            old_todo_count = len(todo_list.todos)

            deleted_todo = todo_list.delete_todo(id_to_delete)

            assert deleted_todo.get("id") == id_to_delete
            assert len(todo_list.todos) == old_todo_count
            with raises(ValueError):
                todo_list.get_todo(id_to_delete)

        def test_delete_todo_last(self, todo_list: TodoList):
            id_to_delete = len(todo_list.todos)
            old_todo_count = len(todo_list.todos)

            deleted_todo = todo_list.delete_todo(id_to_delete)

            assert deleted_todo.get("id") == id_to_delete
            assert len(todo_list.todos) == old_todo_count
            with raises(ValueError):
                todo_list.get_todo(id_to_delete)

        def test_delete_todo_non_existing_id(self, todo_list: TodoList):
            non_existing_id = 100

            with raises(ValueError):
                todo_list.delete_todo(non_existing_id)

    class TestGetAllTodos:
        def test_get_all_todos(self, todo_list: TodoList):
            all_todos = todo_list.get_all_todos()

            assert len(all_todos) == len(todo_list.todos)
            assert all_todos == todo_list.todos

        def test_get_all_todos_empty(self, empty_todo_list: TodoList):
            all_todos = empty_todo_list.get_all_todos()

            assert len(all_todos) == 0
            assert all_todos == []

        def test_get_all_todos_with_deleted(self, todo_list: TodoList):
            id_to_delete = 1
            todo_list.delete_todo(id_to_delete)

            all_todos = todo_list.get_all_todos()

            assert len(all_todos) == len(
                [todo for todo in todo_list.todos if todo is not None]
            )
            assert id_to_delete not in [todo.get("id") for todo in all_todos]
