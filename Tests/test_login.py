from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto("http://courrier.sharedsystem.com/login")

    
    page.get_by_placeholder("Nom d'utilisateur").fill("yassine")
    page.locator("input[placeholder='Mot de passe']").first.fill("yassine1")

    
    page.get_by_role("button", name="Se connecter").click()

    
    expect(page.get_by_text("Gestion électronique des courriers")).to_be_visible()

