import os
from setuptools import setup, find_packages

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# Package dependencies
install_requires = [
]


setup(
    name='wagtail_grafl',
    version=__import__('wagtail_grafl').__version__,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='grafl.io integration for Wagtail CMS',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/cursive-works/wagtail-grafl',
    author='Martin Swarbrick',
    author_email='martin.swarbrick@cursive.works',
    keywords=['WAGTAIL', 'GRAFL', 'STREAMFIELD', 'WAGTAIL_GRAFL', 'WAGTAIL CMS'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
    ],
    install_requires=install_requires,
)
