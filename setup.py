from setuptools import setup, find_packages

setup(
    name = 'django-vcs',
    version = '0.1',
    author = 'Alex Gaynor, Justin Lilly',
    author_email = 'alex.gaynor@gmail.com',
    description = "A Django application to interface with a VCS using the pyvcs library.",
    url = 'http://github.com/alex/django-vcs/',
    packages = find_packages('django_vcs'),
    package_data = {
        'django_vcs': 'templates/django_vcs/*.html',
    }
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Version Control',
        'Framework :: Django',
    ],
)
