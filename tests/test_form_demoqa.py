from demoqa_tests.model.pages.registration_page import registration_page


def test_correct_full_form():
    registration_page.open()
    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('Ivanov')
    registration_page.fill_email('ivan.ivanov@gmail.com')
    registration_page.fill_gender()
    registration_page.fill_number('1234567890')
    registration_page.fill_birthdate(1995, 8, 1)
    registration_page.fill_subject('comp')
    registration_page.fill_hobbies(3)
    registration_page.fill_hobbies(2)
    registration_page.upload_picture('image.png')
    registration_page.fill_current_address('address')
    registration_page.fill_state('hary')
    registration_page.fill_city('karn')
    registration_page.submit_form()

    registration_page.assert_registered_info(
        'Ivan Ivanov',
        'ivan.ivanov@gmail.com',
        'Male',
        '1234567890',
        '01 September,1995',
        'Computer Science',
        'Music, Reading',
        'image.png',
        'address',
        'Haryana Karnal'
    )
