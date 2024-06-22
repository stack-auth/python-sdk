from setuptools import setup, find_packages

setup(
    name='stack_auth_sdk',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests>=2.0.0',
    ],
    description='Python SDK for accessing the Stack Auth API',
    url='https://github.com/stack-auth/python-sdk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
