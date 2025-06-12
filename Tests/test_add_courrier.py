from playwright.sync_api import Page, expect


def test_add_courrier(page: Page):
    page.goto("http://courrier.sharedsystem.com/login", timeout=60000)

    # Connexion
    page.get_by_placeholder("Nom d'utilisateur").fill("yassine")
    page.locator("input[placeholder='Mot de passe']").first.fill("yassine1")
    page.get_by_role("button", name="Se connecter").click()

    expect(page.get_by_text("Gestion électronique des courriers")).to_be_visible()

    # Aller à la page de création
    page.goto("http://courrier.sharedsystem.com/pages/create-mail")

        # DEBUG VISUEL (optionnel)
    page.pause()

    # Dropdown Statut de courrier — attendre que le composant soit visible ET attaché au DOM
    dropdown = page.locator("p-dropdown[formcontrolname='courrierStatus'] .p-dropdown-trigger")
    dropdown.wait_for(state="attached", timeout=10000)
    dropdown.wait_for(state="visible", timeout=10000)

    # Vérifier aussi qu’il est cliquable
    expect(dropdown).to_be_visible()
    expect(dropdown).to_be_enabled()

    # Effectuer le clic
    dropdown.click()

    # Sélectionner l'option
    page.get_by_role("option", name="Courrier Arrivé").click()


    # Sujet
    page.locator("input[formcontrolname='courrierSujet']").fill("test")

    # Référence (lecture seule)
    reference_field = page.locator("input[formcontrolname='courrierRef']")
    expect(reference_field).to_be_visible()
    expect(reference_field).to_have_attribute("readonly", "")

    # Type
    page.get_by_role("combobox", name="Sélectionner le type").click()
    page.get_by_role("option", name="type 1").click()

    # Canal
    page.get_by_label("Sélectionner le canal").click()
    page.get_by_role("option", name="canal 1").click()

    # Date d’arrivée
    page.locator('button.p-datepicker-trigger').click()
    page.locator(".p-datepicker").wait_for(state="visible")
    page.locator("span.p-element", has_text="21").click()

    # Urgence
    page.get_by_label("Sélectionner Urgence").click()
    page.get_by_role("option", name="Urgent").click()

    # Limite de réponse
    deadline_input = page.locator("input[placeholder=''][aria-haspopup='dialog']").nth(1)
    deadline_input.wait_for(state="visible")
    deadline_input.fill("2025-05-28")

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

    # Vérification succès
    expect(page.get_by_text("Crée avec succès")).to_be_visible()
