from setuptools import setup, find_packages

setup(
    name = 'django-vcs',
    version = '0.1',
    author = 'Alex Gaynor, Justin Lilly',
    author_email = 'alex.gaynor@gmail.com',
    description = "A pluggable django application to allow browsing of code repositories.",
    url = 'http://github.com/alex/django-vcs/',
    packages = find_packages(),
    package_data = {'django_vcs': ['templates/django_vcs/*.html'],},
    install_requires = ['pyvcs'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Version Control',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
