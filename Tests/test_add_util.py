from playwright.sync_api import Page, expect


def test_ajout_utilisateur(page: Page):
    #Login
    page.goto("http://courrier.sharedsystem.com/login")
    page.get_by_placeholder("Nom d'utilisateur").fill("yassine")
    page.locator("input[placeholder='Mot de passe']").first.fill("yassine1")
    page.get_by_role("button", name="Se connecter").click()

    expect(page.get_by_text("Gestion électronique des courriers")).to_be_visible()

    # Aller à la page d'ajout utilisateur
    page.goto("http://courrier.sharedsystem.com/pages/gestion-des-users")

    #Remplir les champs du formulaire
    page.locator('#name').fill("Dido")
    page.locator('[formcontrolname="TUserFirstName"]').fill("Sofie")
    page.locator('[formcontrolname="TUserPhoneNumber"]').fill("0612345678")
    page.locator('[formcontrolname="TUserLogin"]').nth(0).fill("Développeuse")
    page.locator('[formcontrolname="TUserLogin"]').nth(1).fill("sofie.dido")
    page.locator('[formcontrolname="TUserEmail"]').fill("sofie.dido@example.com")

    # Sélectionner un service
    page.get_by_role("combobox", name="Sélectionner le service").click()
    page.get_by_role("option", name="service 1").click()  

    # Sélectionner un rôle
    page.get_by_role("combobox", name="Sélectionner le role").click()
    page.get_by_role("option", name="Utilisateur").click() 

    # Mot de passe
    page.locator('input[type="password"]').nth(0).fill("Test@1234")
    page.locator('input[type="password"]').nth(1).fill("Test@1234")

    # Enregistrer
    page.get_by_text("Enregistrer").click()

    # Vérifier la réussite de l'ajout 
    expect(page.get_by_text("Utilisateur ajouté avec succès")).to_be_visible()
