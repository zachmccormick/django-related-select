from setuptools import setup

setup(
    name='django-related-select',
    packages=['related_select'],  # this must be the same as the name above
    version='0.1',
    description='Class-based View and django form field for related select boxes',
    author='Zach McCormick',
    author_email='zach.mccormick@smilecareclub.com',
    url='https://github.com/CamelotVG/django-related-field',  # use the URL to the github repo
    download_url='https://github.com/CamelotVG/django-related-field/tarball/0.1',
    keywords=['django', 'related', 'dependent', 'forms'],
    classifiers=[],
    install_requires=[
        'django'
    ],
    test_suite='tests'
)
