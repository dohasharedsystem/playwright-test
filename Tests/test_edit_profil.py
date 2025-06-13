from playwright.sync_api import Page, expect


def test_edit_profil(page: Page):
    # Connexion
    page.goto("http://courrier.sharedsystem.com/login", timeout=60000)
    page.get_by_placeholder("Nom d'utilisateur").fill("yassine")
    page.locator("input[placeholder='Mot de passe']").first.fill("yassine1")
    page.get_by_role("button", name="Se connecter").click()

    expect(page.get_by_text("Gestion électronique des courriers")).to_be_visible()

    # Aller sur la page du profil
    page.goto("http://courrier.sharedsystem.com/pages/profil")

    # Modifier les champs modifiables
    page.locator("input[formcontrolname='tUserLastName']").fill("elarrr")
    page.locator("input[formcontrolname='tUserFirstName']").fill("yassine")
    page.locator("input[formcontrolname='tUserPhoneNumber']").fill("1211111111")  # 10 chiffres comme demandé

    # Cliquer sur Enregistrer
    page.get_by_role("button", name="Enregistrer").click()

    # Vérification après enregistrement (à ajuster selon le message de succès exact)
    expect(page.locator("div.p-toast-summary").first).to_be_visible()
    expect(page.locator("div.p-toast-detail").first).to_have_text("Informations personnelles modifiées avec succès !")