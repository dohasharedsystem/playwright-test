import pytest
from playwright.sync_api import Page


@pytest.fixture
def page_logged_in(page: Page):
    page.goto("http://courrier.sharedsystem.com/")
    page.get_by_placeholder("Nom d'utilisateur").fill("yassine")
    page.get_by_placeholder("Mot de passe").fill("yassine1")
    page.get_by_role("button", name="connexion").click()
    return page