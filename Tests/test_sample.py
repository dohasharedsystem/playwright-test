import pytest
from playwright.sync_api import Page, expect


def test_homepage_title(page: Page):
    page.goto("http://courrier.sharedsystem.com/") 
    expect(page).to_have_title("Système de Courrier") 
    
def test_connexion_visible(page: Page):
    page.goto("http://courrier.sharedsystem.com/")

    
    expect(page.get_by_role("button", name="Connexion")).to_be_visible()