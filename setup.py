from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ezs3",
    version="0.2.0",
    author="nchz",
    url="https://github.com/nchz/ezs3",
    description="S3 wrapper built on top of `boto3`.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=requirements,
)
