from selene import browser, be, have, command
import os


def test_correct_full_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').should(be.blank).type('Ivan')
    browser.element('#lastName').should(be.blank).type('Ivanov')
    browser.element('#userEmail').should(be.blank).type('ivan.ivanov@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('1234567890')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="7"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1995"]').click()
    browser.element('.react-datepicker__day.react-datepicker__day--001').click()
    browser.element('#subjectsInput').perform(command.js.scroll_into_view).should(be.blank).type('comp').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('sources/image.png'))
    browser.element('#currentAddress').should(be.blank).type('address')
    browser.element('#react-select-3-input').type('hary').press_enter()
    browser.element('#react-select-4-input').type('karn').press_enter()
    browser.element('#submit').click()

    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(
        have.exact_texts(
            'Ivan Ivanov',
            'ivan.ivanov@gmail.com',
            'Male',
            '1234567890',
            '01 August,1995',
            'Computer Science',
            'Music, Reading',
            'image.png',
            'address',
            'Haryana Karnal'
        )
    )