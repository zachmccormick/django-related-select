from setuptools import setup

setup(
    name='django-related-select',
    packages=['related_select'],
    version='0.4',
    description='Class-based View and django form field for related select boxes',
    author='Zach McCormick',
    author_email='zach.mccormick@smilecareclub.com',
    url='https://github.com/CamelotVG/django-related-select',
    download_url='https://github.com/CamelotVG/django-related-select/tarball/0.4',
    keywords=['django', 'related', 'dependent', 'forms'],
    classifiers=[],
    install_requires=[
        'django'
    ],
    test_suite='tests'
)
