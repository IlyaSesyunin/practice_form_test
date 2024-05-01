import allure
from demoqa_tests.model.pages.registration_page import registration_page
from demoqa_tests.data.users import User


@allure.tag('web')
@allure.title('Successful fill form')
def test_correct_full_form():
    user_ivan = User(
        first_name='Ivan',
        last_name='Ivanov',
        email='ivan.ivanov@gmail.com',
        gender='Male',
        phone_number='1234567890',
        year='1995',
        month='August',
        day='01',
        subjects='Computer Science',
        hobbies='Sports',
        photo='image.png',
        address='address',
        state='Haryana',
        city='Karnal'
    )

    with allure.step('Open registration page'):
        registration_page.open()
    with allure.step('Fill in user data'):
        registration_page.register_user(user_ivan)
    with allure.step('Checking user data'):
        registration_page.assert_registered_info(user_ivan)
