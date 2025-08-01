from setuptools import setup, find_packages

setup(
    name="nav",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'nav=nav.cli:main',  # CLI command: nav → nav/cli.py → main()
        ],
    },
    author="Jacob Sonne",
    description="Navigation shortcuts and fuzzy cd tool",
    keywords="navigation cd shortcut fuzzy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
