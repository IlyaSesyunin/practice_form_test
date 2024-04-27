from demoqa_tests.model.pages.registration_page import registration_page
from demoqa_tests.data.users import User


def test_correct_full_form():
    user_ivan = User(
        first_name='Ivan',
        last_name='Ivanov',
        email='ivan.ivanov@gmail.com',
        gender='Male',
        phone_number='1234567890',
        year='1995',
        month='8',
        day='1',
        subjects='Computer Science',
        hobbies='1',
        photo='image.png',
        address='address',
        state='Haryana',
        city='Karnal'
    )

    registration_page.open()
    registration_page.register_user(user_ivan)
    registration_page.assert_registered_info(user_ivan)
