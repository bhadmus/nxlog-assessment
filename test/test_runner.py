import pytest


@pytest.mark.parametrize("text",
                         [
                             ("Complete the Assessment"),
                             ("∑œøπ¥©ßåµ∫"),
                             ("1552571")
                         ]
                         )
def test_insert_characters_to_todo_task(actions, text: str):
    actions.insert_todo_task(text)
    actions.verify_todo_task(text)


def test_tasks_can_be_completed(actions):
    actions.insert_todo_task('Complete the Assessment')
    actions.click_element(actions.mark_todo_as_complete)
    actions.click_element(actions.completed_task_field)
    actions.verify_task_status(actions.delete_todo_task_field)


def test_tasks_can_be_deleted(actions):
    actions.insert_todo_task('Complete the Assessment')
    actions.click_element(actions.mark_todo_as_complete)
    actions.verify_task_status(actions.delete_todo_task_field)
    actions.click_element(actions.delete_task_button)
    actions.verify_deleted_task(actions.delete_todo_task_field)


def test_tasks_can_be_active(actions):
    actions.insert_todo_task('Complete the Assessment')
    actions.insert_todo_task('≈ç∫~µ∂ß∆†¥∑œø')
    actions.click_element(actions.mark_todo_as_complete)
    actions.click_element(actions.active_task_field)
    actions.verify_todo_task('≈ç∫~µ∂ß∆†¥∑œø')


def test_tasks_can_be_viewed_when_complete(actions):
    actions.insert_todo_task('Complete the Assessment')
    actions.insert_todo_task('≈ç∫~µ∂ß∆†¥∑œø')
    actions.click_element(actions.mark_todo_as_complete)
    actions.click_element(actions.completed_task_field)
    actions.verify_todo_task('Complete the Assessment')
