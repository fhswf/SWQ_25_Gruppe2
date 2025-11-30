import { expect, Page, test } from '@playwright/test';

// [HSHR] Nutzung von Konstanten
const TODO_URL = 'https://demo.playwright.dev/todomvc/#/';
const NEW_TODO = 'What needs to be done?';

// [HSHR] Helper-Funktion zur Anlage eines neuen TODO-Eintrags
async function addTodo(page: Page, text: string) {
    const input = page.getByRole('textbox', { name: NEW_TODO });
    await input.fill(text);
    await input.press('Enter');
}

// [HSHR] Helper-Funktion zum togglen aller Checkboxen
async function toggleAll(page: Page, check: boolean) {
    const inputToggleAll = page.locator('input.toggle-all[type="checkbox"]');
    if (await inputToggleAll.count() > 0) {
        try {
            if (check) {
                await inputToggleAll.check();
            } else {
                await inputToggleAll.uncheck();
            }
            return;
        } catch {
        }
    }
}

test.describe('TodoMVC Tests', () => {
    test.beforeEach(async ({ page }: { page: Page }) => {
        await page.goto(TODO_URL);
    });

    // [HAHR, PRSE] Ein TODO der Liste hinzufügen
    test("Ein neues Todo wird hinzugefügt", async ({ page }) => {
        await addTodo(page, 'Kochen')
        await expect(page.getByText('Kochen')).toBeVisible();
    });

    // [HAHR, PRSE] Mehrere TODOs der Liste hinzufügen
    test("Mehrere TODOs der Liste hinzufügen", async ({ page }) => {
        await addTodo(page, 'Kochen')
        await expect(page.getByText('Kochen')).toBeVisible();
        await addTodo(page, 'Bügeln')
        await expect(page.getByText('Bügeln')).toBeVisible();
        await addTodo(page, 'Einkaufen')
        await expect(page.getByText('Einkaufen')).toBeVisible();
    });

    // [HAHR, PRSE] Eine Checkbox bei einem TODO anhaken und wieder rückgängig machen
    test("Eine Checkbox bei einem TODO anhaken und wieder rückgängig machen", async ({ page}) => {
        await addTodo(page, 'Einkaufen');
        const toggle = page.getByLabel('Toggle Todo');
        await toggle.check();
        await expect(toggle).toBeChecked();
        await toggle.uncheck();
        await expect(toggle).not.toBeChecked();
    });

    // [HAHR, PRSE] Abfrage Aktiver TODOs
    test("Abfrage Aktiver TODO", async ({ page }) => {
        await addTodo(page, 'Einkaufen');
        const itemsLeft = page.getByTestId('todo-count');
        await expect(itemsLeft).toHaveText('1 item left');
        await addTodo(page, 'Bügeln');
        await expect(itemsLeft).toHaveText('2 items left');
    });

    // [HAHR, PRSE] Ein bestimmtes TODO via X löschen
    test("Löschen eines TODO", async ({ page }) => {
        await addTodo(page, 'Kochen');
        await addTodo(page, 'Bügeln');
        const itemToDelete = page.getByRole('listitem').filter({ hasText: 'Bügeln' });
        await itemToDelete.hover();
        await itemToDelete.getByRole('button', { name: 'Delete' }).click();
        await expect(page.getByText('Bügeln')).not.toBeVisible();
        await expect(page.getByText('Kochen')).toBeVisible();
    });

    // [HAHR, PRSE] Sowohl alle als auch einzelne TODOs über ToggleAll-Button als erledigt/unerledigt markieren
    test("Toggle aller und einzelner TODOs", async ({page}) => {
        await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Kochen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Waschen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Bügeln');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByText('Mark all as complete').click();
        await page.getByText('Mark all as complete').click();
        await page.getByRole('listitem').filter({ hasText: 'Waschen' }).getByLabel('Toggle Todo').check();
        await page.getByText('Mark all as complete').click();
        await page.getByRole('listitem').filter({ hasText: 'Waschen' }).getByLabel('Toggle Todo').uncheck();
        await page.getByText('Mark all as complete').click();
    });

    // [HAHR, PRSE] Alle erledigten TODOs auf abgeschlossen setzen
    test('Alle erledigten TODOs auf abgeschlossen setzen', async ({ page }) => {
        await addTodo(page, 'Bügeln');
        await addTodo(page, 'Waschen');
        await addTodo(page, 'Kochen');
        await toggleAll(page, true);
        const clearCompleted = page.getByRole('button', { name: 'Clear completed' });
        await expect(clearCompleted).toBeVisible();
        await clearCompleted.click();
        await expect(page.locator('.todo-list li')).toHaveCount(0);
    });

    // [HAHR, PRSE] Prüfung ob die Ansichten „Active“, „Completed“, „All“ die richtigen TODOs anzeigen
    test('Anzeige korrekter TODOs in allen Ansichten', async ({ page }) => {
        await addTodo(page, 'Kochen');
        await addTodo(page, 'Bügeln');
        await addTodo(page, 'Waschen');
        await page.getByText('Bügeln').hover();
        await page.getByLabel('Toggle Todo', { exact: true }).nth(1).check();
        await page.getByRole('link', { name: 'Active' }).click();
        await expect(page.getByText('Bügeln')).not.toBeVisible();
        await expect(page.getByText('Kochen')).toBeVisible();
        await expect(page.getByText('Waschen')).toBeVisible();
        await page.getByRole('link', { name: 'Completed' }).click();
        await expect(page.getByText('Bügeln')).toBeVisible();
        await expect(page.getByText('Kochen')).not.toBeVisible();
        await expect(page.getByText('Waschen')).not.toBeVisible();
        await page.getByRole('link', { name: 'All' }).click();
        await expect(page.locator('.todo-list li')).toHaveCount(3);
    });

    // [HAHR, PRSE] Prüfung des Counters bei allen Ansichten
    test('Prüfung des Counters bei allen Ansichten', async ({ page }) => {
        await addTodo(page, 'Kochen');
        await addTodo(page, 'Bügeln');
        await addTodo(page, 'Waschen');
        const itemsLeft = page.getByTestId('todo-count');
        await expect(itemsLeft).toHaveText('3 items left');
        await page.getByRole('listitem').filter({ hasText: 'Bügeln' }).getByLabel('Toggle Todo').check();
        await expect(itemsLeft).toHaveText('2 items left');
        await page.getByRole('link', { name: 'Completed' }).click();
        await expect(itemsLeft).toHaveText('2 items left');
        await page.getByRole('link', { name: 'Active' }).click();
        await expect(itemsLeft).toHaveText('2 items left');
    });

    // [HAHR, PRSE] Leeres TODO / TODO nur aus Leerzeichen bestehend
    test('Test für ein leeres TODO', async ({ page }) => {
        const input = page.getByRole('textbox', { name: NEW_TODO });
        await input.press('Enter');
        await input.fill('     ');
        await input.press('Enter');
        await expect(page.locator('.todo-list li')).toHaveCount(0);
    });

    // [HAHR, PRSE] Einfügen eines sehr langen TODO-Eintrags
    test('Einfügen eines TODO mit langem Titel', async ({ page }) => {
        const longText = 'Test '.repeat(100).trim();
        await addTodo(page, longText);
        await expect(page.getByText(longText)).toBeVisible();
    });

    // [HAHR, PRSE] Prüfung der Sichtbarkeit des Clear Complete Buttons
    test("Sichtbarkeit des Clear Complete Buttons", async ({ page }) => {
        const itemsLeft = page.getByTestId('todo-count');
        await expect(itemsLeft).toHaveCount(0);
        const clearCompletedButton = page.getByRole('button', { name: 'Clear completed'});
        await expect(clearCompletedButton).toBeHidden();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Kochen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('listitem').filter({ hasText: 'Kochen' }).getByLabel('Toggle Todo').check();
        await expect(clearCompletedButton).toBeVisible();
    });
});
