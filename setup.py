from setuptools import setup, find_packages
import os

# Read the contents of README.md
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="electronicspy",
    version="0.1.1",
    author="Diego Chumpitaz Palomino",
    author_email="diegoruben3124@gmail.com",
    description=(
    "A curated collection of electronics, customer sales, and financial market datasets for "
    "data analysis, statistical modeling, and machine learning research. "
    "Includes electronics product data, customer purchase behavior and demographics, "
    "sales transactions, product types, and historical stock prices for Samsung Electronics, "
    "with data covering product analysis, consumer behavior, sales trends, financial analysis, "
    "and stock market forecasting."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/diegoruben3124-afk/electronicspy",
    project_urls={
        "Bug Tracker": "https://github.com/diegoruben3124-afk/electronicspy/issues",
        "Documentation": "https://github.com/diegoruben3124-afk/electronicspy",
        "Source Code": "https://github.com/diegoruben3124-afk/electronicspy",
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "electronicspy": [
            "data/*.csv",
        ],
    },
    classifiers=[
    "Development Status :: 4 - Beta",

    # Audience
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Intended Audience :: Science/Research",

    # License
    "License :: OSI Approved :: MIT License",

    # Topics
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Topic :: Software Development :: Libraries :: Python Modules",

    # Python Versions
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.14",

    # OS
    "Operating System :: OS Independent",

    # Language
    "Natural Language :: English",
],
    keywords=(
    "electronics, electronic products, datasets, sales, customer behavior, "
    "purchase behavior, consumer data, customer demographics, transactions, "
    "product types, retail, e-commerce, sales analysis, financial data, "
    "stock prices, stock market, Samsung Electronics, historical stock data, "
    "financial analysis, stock forecasting, trend analysis, data science, "
    "statistics, machine learning, data analysis, research"
),
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.5",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ],
        "docs": [
            "mkdocs",
            "mkdocs-material",
        ],
    },
    license="MIT License",
    zip_safe=False,
)