from setuptools import setup

setup (
    name="sa-modules",
    version = "0.1",
    author="NickRodriguez",
    author_email="nick@dashanddata.com",
    description = "Modules for social aggretator",
    packages=['sa_config','sa_models'],
    python_requires=">=3.8",
    )