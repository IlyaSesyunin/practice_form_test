from selene import browser, have, command

from demoqa_tests import resource


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def register_user(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        browser.element('#userEmail').type(user.email)
        browser.element('[for="gender-radio-1"]').click()
        browser.element('#userNumber').type(user.phone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element(f'option[value="{user.month}"]').click()
        browser.element('.react-datepicker__year-select').click().element(f'option[value="{user.year}"]').click()
        browser.element(f'.react-datepicker__day.react-datepicker__day--00{user.day}').click()
        browser.element('#subjectsInput').type(user.subjects).press_enter()
        browser.element('#subjectsInput').perform(command.js.scroll_into_view)
        browser.element(f'[for="hobbies-checkbox-{user.hobbies}"]').click()
        browser.element('#uploadPicture').set_value(resource.path(user.photo))
        browser.element('#currentAddress').type(user.address)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()
        browser.element('#submit').click()

    def assert_registered_info(self, user):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.phone_number,
            '01 September,1995',
            user.subjects,
            'Sports',
            user.photo,
            user.address,
            f'{user.state} {user.city}'
        )
        )


registration_page = RegistrationPage()
