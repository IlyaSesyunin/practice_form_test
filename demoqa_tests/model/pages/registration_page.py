from selene import browser, have, command, be

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
        browser.element('.react-datepicker__month-select').type(user.month)
        browser.element('.react-datepicker__year-select').type(user.year)
        browser.element(
            f'.react-datepicker__day--0{user.day}:not(.react-datepicker__day--outside-month)'
        ).click()
        browser.element('#subjectsInput').type(user.subjects).press_enter()
        browser.element('#subjectsInput').perform(command.js.scroll_into_view)
        if user.hobbies is 'Sports':
            browser.element(f'[for="hobbies-checkbox-1"]').click()
        elif user.hobbies is 'Reading':
            browser.element(f'[for="hobbies-checkbox-2"]').click()
        elif user.hobbies is 'Music':
            browser.element(f'[for="hobbies-checkbox-3"]').click()
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
            f'{user.day} {user.month},{user.year}',
            user.subjects,
            user.hobbies,
            user.photo,
            user.address,
            f'{user.state} {user.city}'
        )
        )


registration_page = RegistrationPage()
