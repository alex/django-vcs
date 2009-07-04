from setuptools import setup, find_packages

setup(
    name = 'django-vcs',
    version = '0.1',
    packages = find_packages('django_vcs'),
    package_dir = {'': 'django_vcs'},
    install_requires = ['setuptools'],
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
