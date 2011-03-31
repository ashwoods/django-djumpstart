from selenium import selenium
import unittest, time, re

class test_simpletest(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", "http://127.0.0.1:8000/")
        self.selenium.start()
    
    def test_test_simpletest(self):
        sel = self.selenium
        sel.open("/admin")
        sel.type("id_username", "admin")
        sel.type("id_password", "admin")
        sel.click("//input[@value='Log in']")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Site administration | Django site admin", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=Polls")
        sel.wait_for_page_to_load("30000")
        sel.click("link=Add poll")
        sel.wait_for_page_to_load("30000")
        sel.type("id_question", "What is the answer to life the universe and everything")
        sel.type("id_choice_set-0-choice", "42")
        sel.type("id_choice_set-1-choice", "god")
        sel.type("id_choice_set-2-choice", "spaguetti-monster")
        sel.click("link=Today")
        sel.click("link=Now")
        sel.type("id_choice_set-0-votes", "5")
        sel.type("id_choice_set-1-votes", "4")
        sel.type("id_choice_set-2-votes", "3")
        sel.click("_save")
        sel.wait_for_page_to_load("30000")
        try: self.failUnless(sel.is_text_present("The poll \"Poll object\" was added successfully."))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=Log out")
        sel.wait_for_page_to_load("30000")
        try: self.assertEqual("Logged out | Django site admin", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
