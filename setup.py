from setuptools import setup, find_packages

setup(
    name="ETLtool_TianjiRao",
    version="0.1.0",
    description="ETLpipline",
    author="Tianji Rao",
    author_email="tianji.rao@duke.edu",
    packages=find_packages(),
    install_requires=[
        "databricks-sql-connector",
        "pandas",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "etl_query=main:main",
        ],
    },
)
