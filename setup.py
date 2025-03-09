from setuptools import find_packages, setup

from nepali_datetime_field import __version__, __author__

with open("README.rst", encoding="utf-8") as readme_file:
    README = readme_file.read()

setup(
    name="django-nepali-datetime-field",
    version=__version__,
    description="Django nepali datetime fields and helpers.",
    long_description=README,
    long_description_content_type="text/x-rst",
    author=__author__,
    author_email="amitgaru2@gmail.com",
    url="https://github.com/amitgaru2/django-nepali-datetime-field",
    license="MIT",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Framework :: Django :: 5.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    include_package_data=True,
    packages=find_packages(exclude=("example_app", "example_app.*")),
    python_requires=">=3.6",
    install_requires=["Django >= 2.0", "nepali_datetime"],
)
