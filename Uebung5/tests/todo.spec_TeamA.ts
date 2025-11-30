import { expect, Page, test } from '@playwright/test';

test.describe('TodoMVC Tests', () => {
    test.beforeEach(async ({ page }: { page: Page }) => {
        await page.goto('https://demo.playwright.dev/todomvc/');
    });

    // Demo Test
    test("Demo Test", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.fill('Mein erstes Todo');
        await newTodoInput.press('Enter');

        await expect(page.getByText('Mein erstes Todo')).toBeVisible();
    });


    // [HAHR, PRSE] Ein TODO der Liste hinzufügen
    test("Ein neues Todo wird hinzugefügt", async ({ page }) => {
        await page.goto('https://demo.playwright.dev/todomvc/#/');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Kochen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    });

    // [HAHR, PRSE] Mehrere TODOs der Liste hinzufügen
    test("Mehrere TODOs der Liste hinzufügen", async ({ page }) => {
        await page.goto('https://demo.playwright.dev/todomvc/#/');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Wischen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Bügeln');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Einkaufen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    });

    // [HAHR, PRSE] Eine Checkbox bei einem TODO anhaken und wieder rückgängig machen
    test("Eine Checkbox bei einem TODO anhaken und wieder rückgängig machen", async ({ page}) => {
        await page.goto('https://demo.playwright.dev/todomvc/#/');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Einkaufen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('listitem').filter({ hasText: 'Einkaufen' }).getByLabel('Toggle Todo').check();
        await page.getByRole('listitem').filter({ hasText: 'Einkaufen' }).getByLabel('Toggle Todo').uncheck();
    });

    // [HAHR, PRSE] Abfrage Aktiver TODOs
    test("Abfrage Aktiver TODO", async ({ page }) => {
        await page.goto('https://demo.playwright.dev/todomvc/#/');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Kochen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        const itemsLeft = page.getByTestId('todo-count');
        await expect(itemsLeft).toHaveText('1 item left');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Bügeln');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await expect(itemsLeft).toHaveText('2 items left');
    });

    // [HAHR, PRSE] Ein bestimmtes TODO via X löschen
    test("Löschen eines TODO", async ({ page }) => {
        await page.goto('https://demo.playwright.dev/todomvc/#/');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Kochen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Bügeln');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByText('Bügeln').hover();
        await page.getByRole('button', { name: 'Delete' }).click();
    });

    // [HAHR, PRSE] Sowohl alle als auch einzelne TODOs über ToggleAll-Button als erledigt/unerledigt markieren
    test("Toggle aller und einzelner TODOs", async ({page}) => {
        await page.goto('https://demo.playwright.dev/todomvc/#/');
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
        await page.goto('https://demo.playwright.dev/todomvc/#/');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Bügeln');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Waschen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Kochen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByText('Mark all as complete').click();
        await page.getByRole('button', { name: 'Clear completed' }).click();
    });

    // [HAHR, PRSE] Prüfung ob die Ansichten „Active“, „Completed“, „All“ die richtigen TODOs anzeigen
    test('Anzeige korrekter TODOs in allen Ansichten', async ({ page }) => {
        await page.goto('https://demo.playwright.dev/todomvc/#/');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Kochen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Bügeln');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Waschen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('link', { name: 'Active' }).click();
        await page.getByRole('link', { name: 'All' }).click();
        await page.getByRole('listitem').filter({ hasText: 'Bügeln' }).getByLabel('Toggle Todo').check();
        await page.getByRole('link', { name: 'Active' }).click();
        await page.getByRole('link', { name: 'All' }).click();
        await page.getByRole('link', { name: 'Active' }).click();
        await page.getByRole('link', { name: 'Completed' }).click();
    });

    // [HAHR, PRSE] Prüfung des Counters bei allen Ansichten
    test('Prüfung des Counters bei allen Ansichten', async ({ page }) => {
        await page.goto('https://demo.playwright.dev/todomvc/#/');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Kochen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Bügeln');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Waschen');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('link', { name: 'Active' }).click();
        await page.getByRole('link', { name: 'All' }).click();
        const itemsLeft = page.getByTestId('todo-count');
        await expect(itemsLeft).toHaveText('3 items left');
        await page.getByRole('listitem').filter({ hasText: 'Bügeln' }).getByLabel('Toggle Todo').check();
        await page.getByRole('link', { name: 'Active' }).click();
        await expect(itemsLeft).toHaveText('2 items left');
        await page.getByRole('link', { name: 'All' }).click();
        await page.getByRole('link', { name: 'Active' }).click();
        await page.getByRole('link', { name: 'Completed' }).click();
        await expect(itemsLeft).toHaveText('2 items left');
    });

    // [HAHR, PRSE] Leeres TODO / TODO nur aus Leerzeichen bestehend
    test('Test für ein leeres TODO', async ({ page }) => {
        await page.goto('https://demo.playwright.dev/todomvc/#/');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('       ');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    });

    // [HAHR, PRSE] Einfügen eines sehr langen TODO-Eintrags
    test('Einfügen eines TODO mit langem Titel', async ({ page }) => {
        await page.goto('https://demo.playwright.dev/todomvc/#/');
        await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
        await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('Test '.repeat(100).trim());
        await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
    });

    // [HAHR, PRSE] Prüfung der Sichtbarkeit des Clear Complete Buttons
    test("Sichtbarkeit des Clear Complete Buttons", async ({ page }) => {
        await page.goto('https://demo.playwright.dev/todomvc/#/');
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
