from playwright.sync_api import Page, expect


def test_change_password(page: Page):
    # Connexion
    page.goto("http://courrier.sharedsystem.com/login", timeout=60000)
    page.get_by_placeholder("Nom d'utilisateur").fill("yassine")
    page.locator("input[placeholder='Mot de passe']").first.fill("yassine1")
    page.get_by_role("button", name="Se connecter").click()

    expect(page.get_by_text("Gestion électronique des courriers")).to_be_visible()

    #la page du profil
    page.goto("http://courrier.sharedsystem.com/pages/profil")

    # Remplir les champs de modification de mot de passe
    page.get_by_placeholder("Entrez votre ancien mot de passe").fill("yassine1")
    page.get_by_placeholder("Entrez votre nouveau mot de passe").fill("yassine2")
    page.get_by_placeholder("Confirmez votre mot de passe").fill("yassine2")

    # Enregistrer
    page.get_by_role("button", name="Enregistrer").click()

    # Vérification du message de succès
    expect(page.get_by_text("Informations personnelles modifiées avec succès !")).to_be_visible()
