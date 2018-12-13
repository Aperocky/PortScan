try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="portscan",
    version="0.2.1",
    description="Simple port scanning utility at terminal",
    author="Rocky Li",
    author_email="aperocky@gmail.com",
    license="MIT",
    url="https://github.com/Aperocky/PortScan",
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
    install_requires=[],
    py_modules=['portscan'],
    entry_points={
        'console_scripts': [
            "portscan=portscan:main",
        ],
    },
)
