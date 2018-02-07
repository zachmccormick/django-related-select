from setuptools import setup

setup(
    name='django-related-select',
    packages=['related_select'],
    version='0.9',
    description='Class-based View and django form field for related select boxes',
    author='Zach McCormick',
    author_email='zachary.tyler.mccormick@gmail.com',
    url='https://github.com/zachmccormick/django-related-select',
    keywords=['django', 'related', 'dependent', 'forms'],
    classifiers=[],
    install_requires=[
        'django'
    ],
    test_suite='tests',
    include_package_data=True
)
