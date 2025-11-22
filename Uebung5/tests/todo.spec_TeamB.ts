// Bearbeitet von: JNHR, LNBT

import { expect, Page, test } from '@playwright/test';

test.describe('TodoMVC Tests', () => {
    test.beforeEach(async ({ page }: { page: Page }) => {
        await page.goto('https://demo.playwright.dev/todomvc/');
    });

    test("Ein neues Todo wird hinzugefügt", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.fill('Mein erstes Todo');
        await newTodoInput.press('Enter');

        await expect(page.getByText('Mein erstes Todo')).toBeVisible();
    });

    test("Mehrere neue Todos werden hinzugefügt", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.fill('Mein zweites Todo');
        await newTodoInput.press('Enter');
        await newTodoInput.fill('Mein drittes Todo');
        await newTodoInput.press('Enter');

        await expect(page.getByText('Mein zweites Todo')).toBeVisible();
        await expect(page.getByText('Mein drittes Todo')).toBeVisible();
    });

    test("Checkbox anhaken", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.fill('Checkbox-Test Todo');
        await newTodoInput.press('Enter');

        const toggleTodo = page.getByRole('checkbox', { name: 'Toggle Todo' });
        await toggleTodo.check();

        await expect(toggleTodo).toBeChecked();
    });

    test("Items left text", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.fill('1 Item left Todo');
        await newTodoInput.press('Enter');

        const itemsLeft = page.getByTestId('todo-count');
        await expect(itemsLeft).toHaveText('1 item left');

        await newTodoInput.fill('2 Items left Todo');
        await newTodoInput.press('Enter');

        await expect(itemsLeft).toHaveText('2 items left');

        const toggleTodo = page.getByRole('checkbox', { name: 'Toggle Todo' }).first();
        await toggleTodo.check();

        await expect(itemsLeft).toHaveText('1 item left');
    });

    test("Todo löschen", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.fill('Zu löschendes Todo');
        await newTodoInput.press('Enter');

        const todoItem = page.getByText('Zu löschendes Todo');
        await todoItem.hover();
        const deleteButton = page.getByRole('button');
        await deleteButton.click();

        await expect(todoItem).toHaveCount(0);
    });

    test("Toggle alle Todos", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.fill('Todo 1');
        await newTodoInput.press('Enter');
        await newTodoInput.fill('Todo 2');
        await newTodoInput.press('Enter');
        
        const toggleAll = page.getByRole('checkbox').first();
        await toggleAll.check();

        const checkboxes = page.getByRole('checkbox', { name: 'Toggle Todo' });
        const count = await checkboxes.count();
        for (let i = 0; i < count; i++) {
            await expect(checkboxes.nth(i)).toBeChecked();
        }
    });

    test ("Alle erledigten Todos löschen", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.fill('Erledigtes Todo 1');
        await newTodoInput.press('Enter');
        await newTodoInput.fill('Erledigtes Todo 2');
        await newTodoInput.press('Enter');

        const toggleAll = page.getByRole('checkbox').first();
        await toggleAll.check();


        const clearCompletedButton = page.getByText('Clear completed');
        await clearCompletedButton.click();
        
        await expect(page.getByText('Erledigtes Todo 1')).toHaveCount(0);
        await expect(page.getByText('Erledigtes Todo 2')).toHaveCount(0);
    });

    test ("Filter-test", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.fill('Aktives Todo');
        await newTodoInput.press('Enter');
        await newTodoInput.fill('Erledigtes Todo');
        await newTodoInput.press('Enter');
        await newTodoInput.fill('Noch ein offenenes Todo');
        await newTodoInput.press('Enter');

        const toggleTodo = page.getByRole('checkbox', { name: 'Toggle Todo' }).nth(1);
        await toggleTodo.check();

        const activeFilter = page.getByText('Active');
        await activeFilter.click();

        await expect(page.getByText('Aktives Todo')).toBeVisible();
        await expect(page.getByText('Erledigtes Todo')).toHaveCount(0);

        const completedFilter = page.getByText('Completed').first();
        await completedFilter.click();

        await expect(page.getByText('Erledigtes Todo')).toBeVisible();
        await expect(page.getByText('Aktives Todo')).toHaveCount(0);

        const allFilter = page.getByText('All').last();
        await allFilter.click();

        await expect(page.getByText('Aktives Todo')).toBeVisible();
        await expect(page.getByText('Erledigtes Todo')).toBeVisible();
    });

    test("EdgeCases", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.fill('    ');
        await newTodoInput.press('Enter');

        await expect(page.getByTestId('todo-list').getByRole('listitem')).toHaveCount(0);  
        
        await newTodoInput.fill('Sehr langes Todo '.repeat(20).trim());
        await newTodoInput.press('Enter');

        await expect(page.getByText('Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo Sehr langes Todo')).toBeVisible();
    });
});
