from selene.support.shared import browser
from selene import be, have, command
import os

'''
Тест на проверку заполенения формы валидными значениями
'''


def test_validation_form(open_website):
    browser.element('[id="firstName"]').type('Иван')
    browser.element('[id="lastName"]').type('Иванов')
    browser.element('[id="userEmail"]').type('ivan@ivanov.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.execute_script("window.scrollBy(0, 500)")
    browser.element('[id="userNumber"]').type('9152635845')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="5"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="1992"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--016"]').click()
    browser.element('#subjectsInput').type('eng').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/picture.jpg')
    browser.element('#fixedban').perform(command.js.remove)
    browser.element('[id="currentAddress"]').type('Чехова 8')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Karnal').press_enter()
    browser.element('[id="submit"]').click()

    browser.element('[id = "example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))
    browser.element('//tbody/tr[1]/td[2]').should(have.text('Иван Иванов'))
    browser.element('//tbody/tr[2]/td[2]').should(have.text('ivan@ivanov.ru'))
    browser.element('//tbody/tr[3]/td[2]').should(have.text('Male'))
    browser.element('//tbody/tr[4]/td[2]').should(have.text('9152635845'))
    browser.element('//tbody/tr[5]/td[2]').should(have.text('16 June,1992'))
    browser.element('//tbody/tr[6]/td[2]').should(have.text('English'))
    browser.element('//tbody/tr[7]/td[2]').should(have.text('Reading'))
    browser.element('//tbody/tr[8]/td[2]').should(have.text('picture.jpg'))
    browser.element('//tbody/tr[9]/td[2]').should(have.text('Чехова 8'))
    browser.element('//tbody/tr[10]/td[2]').should(have.text('Haryana Karnal'))
