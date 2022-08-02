from pathlib import Path
from setuptools import find_packages, setup
dependencies = []
# read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name='beard-portscan',
    version='0.1.5',
    description="Simple port scanning utility at terminal forked from Aperocky/PortScan",
    author="The Bearded Tek",
    author_email="kenny@beardedtek.com",
    url="https://github.com/beardedtek/PortScan",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    project_urls={
        "Bug Tracker": "https://github.com/beardedtek/PortScan/issues",
    },
    keywords=[
        "port",
        "scanner",
        "multithreading",
        "queue",
        "terminal",
        "utility",
    ],
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    install_requires=dependencies,
    py_modules=['portscan'],
    entry_points={
        'console_scripts': [
            "portscan=portscan:main"
        ],
    },
)
