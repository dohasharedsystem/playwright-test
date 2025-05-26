from playwright.sync_api import Page, expect


def test_add_courrier(page: Page):
    page.goto("http://courrier.sharedsystem.com/login")
    
    page.get_by_placeholder("Nom d'utilisateur").fill("yassine")
    page.get_by_placeholder("Mot de passe").fill("yassine1")
    
    page.get_by_role("button", name="connexion").click()

    expect(page.get_by_text("Gestion électronique des courriers")).to_be_visible()

    page.goto("http://courrier.sharedsystem.com/pages/create-mail")

    # Sélection de la nature du courrier (dropdown personnalisé)
    page.locator("label:has-text('Nature')").locator("xpath=..").locator(".p-dropdown").click()
    page.get_by_role("option", name="Courrier Arrivé").click()

    # Objet
    page.get_by_label("Objet du courrier").fill("test")

    # Champ référence (readonly)
    reference_field = page.get_by_label("<<Nouveau>>")
    expect(reference_field).to_be_visible()
    expect(reference_field).to_have_attribute("readonly", '')

    # Type
    page.get_by_label("Sélectionner le type").click()
    page.get_by_role("option", name="typec1").click()

    # Canal
    page.get_by_label("Sélectionner le canal").click()
    page.get_by_role("option", name="canal 1").click()

    # Date d'arrivée
    page.locator('button[aria-label="Choose Date"]').click()
    page.locator('td.p-datepicker-day >> text="21"').click()

    # Urgence
    page.get_by_label("Sélectionner Urgence").click()
    page.get_by_role("option", name="Urgent").click()

    # Limite de réponse
    page.locator('input[placeholder=""][aria-haspopup="dialog"]').nth(1).fill("2025-05-28")

    # Direction
    page.get_by_label("Sélectionner la direction").click()
    page.get_by_role("option", name="Direction Audit").click()

    # Expéditeur
    page.get_by_label("Sélectionner l'expediteur").click()
    page.get_by_role("option", name="Doha Doha").click()

    # Destinataire
    page.get_by_label("Sélectionner Destinataire").click()
    page.get_by_role("option", name="Test Test").click()

    # Catégorie
    page.get_by_label("Sélectionner la Categorie").click()
    page.get_by_role("option", name="categorie 6").click()

    # Bordereau
    page.get_by_label("Bordereau").click()
    page.get_by_role("option", name="dd").click()

    # Description
    page.get_by_label("Description du courrier").fill("test")

    # Enregistrement
    page.get_by_role("button", name="Enregistrer un Courrier").click()

    # Vérification de la création
    expect(page.get_by_text("Crée avec succès")).to_be_visible()