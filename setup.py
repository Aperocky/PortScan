try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("readme.md", encoding='utf-8') as f:
    readme = f.read()

setup(
    name="portscan",
    version="1.0.1.post2",
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
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    install_requires=[],
    py_modules=['portscan'],
    long_description=readme,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            "portscan=portscan:main",
        ],
    },
)
