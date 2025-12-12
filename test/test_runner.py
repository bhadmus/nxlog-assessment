import pytest
from playwright.sync_api import Page
from objects.page_actions import PageActions
from time import sleep


@pytest.mark.parametrize("text",
                         [
                             ("Complete the Assessment"),
                             ("∑œøπ¥©ßåµ∫"),
                             ("1552571")
                         ]
                         )
def test_insert_characters_to_todo_task(page: Page, text: str):
    test = PageActions(page)
    test.launch_url()
    test.insert_todo_task(text)
    test.verify_todo_task(text)


def test_tasks_can_be_completed(page: Page):
    test = PageActions(page)
    test.launch_url()
    test.insert_todo_task('Complete the Assessment')
    test.click_element(test.mark_todo_as_complete)
    test.click_element(test.completed_task_field)
    test.verify_task_status(test.delete_todo_task_field)


def test_tasks_can_be_deleted(page: Page):
    test = PageActions(page)
    test.launch_url()
    test.insert_todo_task('Complete the Assessment')
    test.click_element(test.mark_todo_as_complete)
    test.verify_task_status(test.delete_todo_task_field)
    test.click_element(test.delete_task_button)
    test.verify_deleted_task(test.delete_todo_task_field)


def test_tasks_can_be_active(page: Page):
    test = PageActions(page)
    test.launch_url()
    test.insert_todo_task('Complete the Assessment')
    test.insert_todo_task('≈ç∫~µ∂ß∆†¥∑œø')
    test.click_element(test.mark_todo_as_complete)
    test.click_element(test.active_task_field)
    test.verify_todo_task('≈ç∫~µ∂ß∆†¥∑œø')


def test_tasks_can_be_viewed_when_complete(page: Page):
    test = PageActions(page)
    test.launch_url()
    test.insert_todo_task('Complete the Assessment')
    test.insert_todo_task('≈ç∫~µ∂ß∆†¥∑œø')
    test.click_element(test.mark_todo_as_complete)
    test.click_element(test.completed_task_field)
    test.verify_todo_task('Complete the Assessment')
