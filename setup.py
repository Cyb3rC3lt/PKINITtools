from setuptools import setup

setup(
    name="PKINITtools",
    version="0.1.0",
    description="A collection of tools for PKINIT and Kerberos ticket manipulation",
    author="Dirkjan Mollema",
    py_modules=[
        "getnthash",
        "gettgtpkinit",
        "gets4uticket",
    ],
    install_requires=[
        "impacket",
        "minikerberos",
    ],
    entry_points={
        "console_scripts": [
            "getnthash = getnthash:main",
            "gettgtpkinit = gettgtpkinit:main",
            "gets4uticket = gets4uticket:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
