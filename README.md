# 💹 Financial Data Analysis and Predictive Modeling

## Table of Contents

- [Overview](#overview)
- [Technologies](#technologies)
- [Folder Organization](#folder-organization)
- [Setup](#setup)
- [Notes](#notes)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project is focused on analyzing financial data using both Natural Language Processing (NLP) and quantitative analysis techniques. The main objective is to explore the relationship between financial news sentiment and stock market movements, enhancing predictive analytics capabilities. The analysis involves sentiment scoring, correlation analysis, and the application of technical indicators to stock price data.

  ### Key functionalities include:

- **Sentiment Analysis**: Extract and quantify sentiment from financial news articles.

- **Correlation Analysis**: Identify and analyze correlations between news sentiment and stock market performance.

- **Technical Analysis**: Use TA-Lib to calculate indicators like Moving Averages, RSI, and MACD.

- **Visualization**: Visualize the impact of various indicators on stock prices.


## Technologies

This repository contains the backend code used to provide services to the client. It is written in Python and utilizes various libraries and frameworks for data analysis, technical indicators, and web application development. The project follows a modular structure with clear separation of concerns to ensure maintainability and scalability.

The set of technologies we utilized in this project:

1. **Programming Language**: [![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=yellow)](https://www.python.org/)
2. **Data Visualization**: [![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-3776AB?style=flat&logo=seaborn&logoColor=white)](https://seaborn.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4D8A?style=flat&logo=plotly&logoColor=white)](https://plotly.com/)
3. **Data Manipulation**: [![Pandas](https://img.shields.io/badge/Pandas-Data_Manipulation-150458?style=flat&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Data_Manipulation-013243?style=flat&logo=numpy&logoColor=white)](https://numpy.org/)
4. **Natural Language Processing**: [![NLTK](https://img.shields.io/badge/NLTK-NLP-5B2D5F?style=flat&logo=nltk&logoColor=white)](https://www.nltk.org/)
[![SpaCy](https://img.shields.io/badge/SpaCy-NLP-4A5C4D?style=flat&logo=spacy&logoColor=white)](https://spacy.io/)
5. **Technical Analysis**: [![TA-Lib](https://img.shields.io/badge/TA--Lib-Technical_Analysis-DAA520?style=flat&logo=tradingview&logoColor=white)](https://mrjbq7.github.io/ta-lib/)
### 6. **Financial Metrics**: [![PyPortfolioOpt](https://img.shields.io/badge/PyPortfolioOpt-Financial_Metrics-1D4D5D?style=flat&logo=python&logoColor=white)](https://pyportfolioopt.readthedocs.io/)
7. **Web Framework**: [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
8. **Version Control**: [![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=flat&logo=git&logoColor=white)](https://git-scm.com/)
9. **Data Hosting**: [![Google Drive](https://img.shields.io/badge/Google%20Drive-4285F4?style=flat&logo=googledrive&logoColor=white)](https://www.google.com/drive/)

## Folder Organization

```
📁.github
└──
    └── 📁workflows
         └── 📃blank.yml
└── 📁notebooks
         └── 📓Quantitative_analysis.ipynb
         └── 📓Stock_market_news_analysis.ipynb
└── 📁scripts
         └── 📃__init__.py
         └── 📃financialAnalyzer.py
         └── 📃nltk_sentiment.py
         └── 📃publication_analysis.py
         └── 📃publishing_time_series_analysis.py
         └── 📃time_series_anlysis.py
         └── 📃topicModeling.py
└── 💻src
    └── 📁dashboard-div
                    └── 📝app.py
└── ⌛tests
         └── 📃__init__.py
         
└── 📜.gitignore
└── 📰README.md
└── 🔋requirements.txt
└── 📇setup.py.py
└── 📇TA_Lib-0.4.29-cp312-cp312-win_amd64.whl
└── 📇templates.py

```

### Folder Structure: A Deep Dive

- **📁.github**: This folder contains GitHub-related configurations, including CI/CD workflows.

  - **📁workflows**: Contains the CI/CD pipeline definitions.
    - **📃blank.yml**: Configuration for Continuous Integration.
    - **📃unittests.yml**: Configuration for running unit tests.

- **📁notebooks**: This directory holds Jupyter notebooks and related Python files.
    - **📓Quantitative_analysis.ipynb**: A Quantitative data analysis in Stock price like.
                        -***using TA-Lib ***: technical analysis  
                        -***using PyFolio*** :  portfolio performance analysis 

    - **📓Stock_market_news_analysis.ipynb**: performs a lot of operatins from descriptive data analysis up to inferential data analysis . *** sentiment Analysiss and Topic Modeling are performed here ***

  - **📓**init**.ipynb**: Initialization notebook, potentially for setting up the environment or performing preliminary tasks.
  - **📃**init**.py**: Initialization Python file for the notebook module.
  - **📰README.md**: Documentation for the notebooks.

- **📁scripts**: Contains Python scripts used throughout the project.

  - **📃**init**.py**: Initialization file for the scripts module.
  - **📃**financialAnalyzer**.py**: the technical anlysis of the stock data class is here.
  - **📃**nltk_sentiment**.py**: a class for the sentiment analysis using NLTK vader is here.
  - **📃**publication_analysis**.py**: the publication pattern and related features to publicants are performed     using this package.
  - **📃**publishing_time_series_analysis**.py**: publicatin time anlysis is performed using this package/ module.
  - **📃**time_series_anlysis**.py**: the time series analysis for the news is built using this module.
  - **📃**topicModeling**.py**: differnt key words and topics are tried to discoverd using this class.
  - **📰README.md**: Documentation for the scripts.

- **💻src**: The main source code of the project, including the Streamlit dashboard and other related files.

  - **📁dashboard-div**: Holds the code for the dashboard.
    - **📝app.py**: Main application file for the dashboard.
    - **📝README.md**: Documentation specific to the dashboard component.

- **⌛tests**: Contains test files, including unit and integration tests.

  - ****init**.py**: Initialization file for the test module.

- **📜.gitignore**: Specifies files and directories to be ignored by Git.

- **📰README.md**: The main documentation for the entire project.

- **🔋requirements.txt**: Lists the Python dependencies required to run the project.

- **📇setup.py.py**: used to authenticate who the package writer is.

- **📇TA_Lib-0.4.29-cp312-cp312-win_amd64.whl**: A TA-lib library data used for installing in windows.

- **📇templates.py**: Contains templates used within the project, possibly for generating or processing data.

## Setup

1. Clone the repo

```bash
git clone https://github.com/Bereket-07/Financial-News-Sentiment-and-Stock-Market-Analysis.git
```
2. Change directory

```bash
cd Financial-News-Sentiment-and-Stock-Market-Analysis
```

3. Install all dependencies

```bash
pip install -r requirements.txt
```

4. change directory to run the streamlit app locally.

```bash
cd src\dashboard-div
```

5. Start the streamlit app

```bash
streamlit run app.py
```

## Contributing

We welcome contributions to this project! To get started, please follow these guidelines:

### How to Contribute

1. **Fork the repository**: Click the "Fork" button at the top right of this page to create your own copy of the repository.
2. **Clone your fork**: Clone the forked repository to your local machine.
   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
3. **Create a new branch**: Create a new branch for your feature or bugfix.
   ```bash
   git checkout -b feature/your-feature
   ```
4. **Make your changes**: Implement your feature or fix the bug. Ensure your code adheres to the project's coding standards and style.
5. **Commit your changes**: Commit your changes with a descriptive message.
   ```bash
   git add .
   git commit -m 'Add new feature or fix bug'
   ```
6. **Push your branch**: Push your branch to your forked repository.
   ```bash
   git push origin feature/your-feature
   ```
7. **Create a Pull Request**: Go to the repository on GitHub, switch to your branch, and click the `New Pull Request` button. Provide a detailed description of your changes and submit the pull request.

## Additional Information

- **Bug Reports**: If you find a bug, please open an issue in the repository with details about the problem.

- **Feature Requests**: If you have ideas for new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License

### Summary

The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). It is a simple and easy-to-understand license that places very few restrictions on reuse, making it a popular choice for open source projects.

By using this project, you agree to include the original copyright notice and permission notice in any copies or substantial portions of the software.
