#-*-coding:utf-8-*-
from setuptools import setup, find_packages

setup(
    name='infobank_omni_sdk_python',
    version='1.0.2',
    description='인포뱅크 Omni Api 발송을 위한 Python SDK 입니다.',
    author='infobank',
    author_email='msgplatform@infobank.net',
    packages=find_packages(),
    install_requires=[
        'python-dateutil~=2.6.1',
        'pydantic~=1.9.2',
        'requests~=2.27.1',
        'typing-extensions~=4.1.0',
        'pytest==7.0.1'
    ],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Telephony",
    ],
)