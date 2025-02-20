from setuptools import setup, find_packages

setup(
    name="test_automation_utils",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "selenium"
    ],
    author="Your Name",
    description="Common utilities for REST API and Selenium test automation"
)
