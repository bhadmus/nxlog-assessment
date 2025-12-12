from playwright.sync_api import Page, expect


class PageActions:
    def __init__(self, page: Page):
        self.page = page
        self.todo_text_field = page.locator('input.new-todo')
        self.todo_list_field = page.locator('[data-testid="todo-title"]')
        self.mark_todo_as_complete = '.todo-list>li:nth-child(1) input[type="checkbox"]'
        self.all_task_field = 'a[href="#/"]'
        self.active_task_field = 'a[href="#/active"]'
        self.completed_task_field = 'a[href="#/completed"]'
        self.delete_task_button = 'button.clear-completed'
        self.delete_todo_task_field = page.locator('button.clear-completed')

    def launch_url(self):
        self.page.set_viewport_size({"width": 1920, "height": 1080})
        self.page.goto("https://demo.playwright.dev/todomvc/#/")

    def insert_todo_task(self, text):
        self.todo_text_field.fill(text)
        self.page.keyboard.press("Enter")

    def verify_todo_task(self, text):
        expect(self.todo_list_field.filter(has_text=text)).to_contain_text(text)

    def click_element(self, element):
        self.page.click(element)

    def verify_task_status(self, element):
        expect(element).to_be_visible()

    def verify_deleted_task(self, element):
        expect(element).not_to_be_visible()
        