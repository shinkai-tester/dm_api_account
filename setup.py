from setuptools import setup

REQUIRES = [
    'requests>=2.31.0',
    'allure-pytest>=2.13.2',
    'pydantic>=2.3.0'
]

setup(
    name='dm_api_account',
    version='0.0.1',
    packages=['dm_api_account', 'dm_api_account.apis', 'dm_api_account.models'],
    url='https://github.com/shinkai-tester/dm_api_account.git',
    license='MIT',
    author='Aleksandra Klimantova',
    author_email='',
    install_requires=REQUIRES,
    description='Client for dm_api_account service'
)
