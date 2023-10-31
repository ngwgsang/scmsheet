import setuptools


setuptools.setup(
    name="scmsheet",
    version="1.0",
    author="sangcamap",
    author_email="nguyenquangsang0709@gmail.com",
    description="Google Sheet Interactive tools",
    long_description="Google Sheet Interactive tools",
    url="https://github.com/sangcamap/scmsheet.git",
    packages=setuptools.find_packages(),
    install_requires=[
        'gspread', 
        'oauth2client', 
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: Apache 2.0",
        "Operating System :: OS Independent",
    ],
)