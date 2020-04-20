from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ezs3",
    version="0.1.0",
    author="nchz",
    description="S3 wrapper built on top of `boto3`.",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=requirements,
)
