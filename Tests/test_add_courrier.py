from playwright.sync_api import Page, expect


def test_add_courrier(page: Page):
    page.goto("http://courrier.sharedsystem.com/login", timeout=60000)

    
    page.get_by_placeholder("Nom d'utilisateur").fill("yassine")
    page.locator("input[placeholder='Mot de passe']").first.fill("yassine1")
    page.get_by_role("button", name="Se connecter").click()

    expect(page.get_by_text("Gestion électronique des courriers")).to_be_visible()
    
    page.goto("http://courrier.sharedsystem.com/pages/create-mail")

    dropdown_trigger = page.locator("p-dropdown[formcontrolname='courrierStatus']")
    dropdown_trigger.wait_for(state="visible", timeout=30000)
    dropdown_trigger.click()

    page.wait_for_selector("ul[role='listbox']", timeout=5000)
    page.get_by_role("option", name="Courrier Arrivé").click()

    
    page.locator("input[formcontrolname='courrierSujet']").fill("test")

    
    reference_field = page.locator("input[formcontrolname='courrierRef']")
    expect(reference_field).to_be_visible()
    expect(reference_field).to_have_attribute("readonly", "")

    
    page.get_by_role("combobox", name="Sélectionner le type").click()
    page.get_by_role("option", name="type 1").click()

    
    page.get_by_label("Sélectionner le canal").click()
    page.get_by_role("option", name="canal 1").click()

    
    page.locator('button.p-datepicker-trigger').click()
    page.locator(".p-datepicker").wait_for(state="visible")
    page.locator("span.p-element", has_text="21").click()
    
    
    page.get_by_label("Sélectionner Urgence").click()
    page.get_by_role("option", name="Urgent").click()
    
    
    deadline_input = page.locator("input[placeholder=''][aria-haspopup='dialog']").nth(1)
    deadline_input.wait_for(state="visible")
    deadline_input.fill("2025-05-28")
    
    
    page.get_by_label("Sélectionner la direction").click()
    page.get_by_role("option", name="Direction Audit").click()
    
    
    page.get_by_label("Sélectionner l'expediteur").click()
    page.get_by_role("option", name="Doha Doha").click()
    
    
    page.get_by_label("Sélectionner Destinataire").click()
    page.get_by_role("option", name="Test Test").click()
    
    
    page.get_by_label("Sélectionner la Categorie").click()
    page.get_by_role("option", name="categorie 6").click()

    
    page.get_by_label("Bordereau").click()
    page.get_by_role("option", name="dd").click()


    page.get_by_label("Description du courrier").fill("test")

    file_input = page.locator("#file-upload")
    file_path = r"C:\Users\dafallah\OneDrive\Desktop\Projects\Playwright test\Tests\image_tester.jpg"
    file_input.set_input_files(file_path)


    page.get_by_role("button", name="Enregistrer un Courrier").click()
    
    expect(page.get_by_text("Crée avec succès")).to_be_visible()
