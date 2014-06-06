'''
Created by tklarryonline on Jun 05, 2014.
'''
import sure
from lettuce import step, world
from lettuce_setup.functions import default_user, visit
from lettuce_setup.selenium_shortcuts import browser
from qnote_api.tests.factories.quote_factory import QuoteFactory


@step(u'I visit "([^"]*)"')
def i_visit_url(step, url):
    visit(url)

@step(u'there are "([^"]*)" quotes in the system')
def there_are_number_of_quotes_in_the_system(step, quotes_number):
    quotes_number = int(quotes_number)
    for i in range(0, quotes_number):
        QuoteFactory(user=default_user())
    world.quotes_number = quotes_number

@step(u'I should see a list of quotes')
def i_should_see_a_list_of_quotes(step):
    quotes = browser().find_elements_by_css_selector('#quotes-list .quote')
    assert len(quotes).should.equal(world.quotes_number)
