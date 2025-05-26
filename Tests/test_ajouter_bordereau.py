import pytest
from playwright.sync_api import Page, sync_playwright


def test_ajouter_bordereau(page: Page):
    
    page.goto("http://courrier.sharedsystem.com/pages/add-bordereau")

    
    page.locator('input[placeholder="Référence du Bordereau"]').wait_for()
    page.locator('input[placeholder="Référence du Bordereau"]').fill("test1")

    
    page.locator('input[placeholder="Sélectionner la date"]').nth(0).wait_for()
    page.locator('input[placeholder="Sélectionner la date"]').nth(0).fill("23/05/2025")

    
    page.locator('input[placeholder="Sélectionner la date"]').nth(1).wait_for()
    page.locator('input[placeholder="Sélectionner la date"]').nth(1).fill("30/05/2025")

    
    page.get_by_role("combobox", name="Bordereau de livraison").click()
    page.get_by_role("option", name="Bordereau de livraison").click()

    
    page.locator('textarea[placeholder="Description du Bordereau"]').fill("test")

    page.get_by_role("button", name="Créer").click()