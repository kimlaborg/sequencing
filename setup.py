from setuptools import setup, find_packages

setup(
    name='NGSKit',
    version='0.0.1',
    author='kimlab.org',
    author_email='carles.corbi@kimlab.org',
    url = "http://kimlab.org",
    description = ("Small kit of Tools for NGS data"),

    packages=[x for x in find_packages()],
    namespace_packages=['NGSKit'],
)