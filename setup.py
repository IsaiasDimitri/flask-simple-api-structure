from setuptools import setup, find_packages


def get_dependencies(file):
    return [dep.strip() for dep in open(file).readlines()]


setup(
    name="simple_api",
    version="0.1.0",
    description="A template to make API's.",
    packages=find_packages(exclude=".env"),
    include_package_data=True,
    install_requires=get_dependencies("requirements.txt"),
    extras_require={"dev": get_dependencies("requirements-dev.txt")},
)