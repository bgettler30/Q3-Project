import sqlite3

def add_question(course, question_text, choice_a, choice_b, choice_c, choice_d, correct_answer, feedback):
    connection = sqlite3.connect("quiz_bowl.db")
    cursor = connection.cursor()
    
    cursor.execute(f"""
    INSERT OR IGNORE INTO {course} (question_text, choice_a, choice_b, choice_c, choice_d, correct_answer, feedback)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (question_text, choice_a, choice_b, choice_c, choice_d, correct_answer, feedback))

    connection.commit()
    connection.close()
    print(f"Question added to {course} (if not already present).")

def remove_question(course, question_text):
    connection = sqlite3.connect("quiz_bowl.db")
    cursor = connection.cursor()

    cursor.execute(f"DELETE FROM {course} WHERE question_text = ?", (question_text,))
    connection.commit()
    connection.close()
    print(f"Question removed from {course}.")

def fetch_questions(course):
    connection = sqlite3.connect("quiz_bowl.db")
    cursor = connection.cursor()
    
    cursor.execute(f"SELECT * FROM {course}")
    questions = cursor.fetchall()
    connection.close()
    return questions

add_question(
    'Intermediate_Financial_Management',
    'What is the main purpose of capital budgeting?',
    'Maximizing revenue',
    'Minimizing costs',
    'Maximizing shareholder wealth',
    'Improving liquidity',
    'C',
    'The primary purpose of capital budgeting is to maximize shareholder wealth.'
)

add_question(
    'Intermediate_Financial_Management',
    'What is Free Cash Flow (FCF) primarily used for?',
    'Debt repayment',
    'Expansion of assets',
    'Determining company value',
    'Dividend distribution',
    'C',
    'Free Cash Flow is often used to determine a company\'s valuation.'
)

add_question(
    'Intermediate_Financial_Management',
    'Which metric is used to evaluate a project’s potential profitability?',
    'Payback period',
    'Internal Rate of Return (IRR)',
    'Gross profit margin',
    'Current ratio',
    'B',
    'The Internal Rate of Return (IRR) measures project profitability.'
)

add_question(
    'Intermediate_Financial_Management',
    'What does NPV stand for in capital budgeting?',
    'Net Potential Value',
    'Nominal Present Value',
    'Net Present Value',
    'Non-Projected Value',
    'C',
    'NPV stands for Net Present Value, used in project valuation.'
)

add_question(
    'Intermediate_Financial_Management',
    'Which of the following is a measure of a project\'s risk?',
    'Standard deviation',
    'NPV',
    'Accounts payable',
    'Fixed costs',
    'A',
    'Standard deviation is commonly used to measure risk.'
)

add_question(
    'Intermediate_Financial_Management',
    'What does WACC stand for?',
    'Weighted Average Capital Cost',
    'Weighted Average Cost of Capital',
    'Weighted Asset Cost of Capital',
    'Working Asset Capital Cost',
    'B',
    'WACC stands for Weighted Average Cost of Capital.'
)

add_question(
    'Intermediate_Financial_Management',
    'Which of the following best describes capital structure?',
    'Proportion of assets financed by equity and debt',
    'Proportion of assets financed by profits',
    'Assets financed by short-term debt',
    'Assets financed by retained earnings',
    'A',
    'Capital structure refers to how a company finances assets with debt and equity.'
)

add_question(
    'Intermediate_Financial_Management',
    'Which of the following would increase a company\'s FCF?',
    'Increase in inventory',
    'Decrease in operating expenses',
    'Increase in long-term debt',
    'Decrease in revenue',
    'B',
    'A decrease in operating expenses would increase Free Cash Flow (FCF).'
)

add_question(
    'Intermediate_Financial_Management',
    'Which of the following is NOT included in the calculation of FCF?',
    'Operating expenses',
    'Capital expenditures',
    'Dividends paid',
    'Depreciation',
    'C',
    'Dividends paid are not included in Free Cash Flow (FCF) calculation.'
)

add_question(
    'Intermediate_Financial_Management',
    'What is a common tool used for capital budgeting decisions?',
    'Equity ratio',
    'Break-even analysis',
    'Payback period',
    'Debt service coverage ratio',
    'C',
    'The payback period is commonly used in capital budgeting decisions.'
)

questions = fetch_questions('Intermediate_Financial_Management')
for question in questions:
    print(question)

add_question(
    'Fundamentals_of_Investment',
    'What is the primary purpose of the Sharpe Ratio?',
    'Measure portfolio returns',
    'Assess risk-adjusted return',
    'Compare stocks to bonds',
    'Calculate dividends',
    'B',
    'The Sharpe Ratio is used to assess risk-adjusted returns.'
)

add_question(
    'Fundamentals_of_Investment',
    'What does a high beta indicate about a stock?',
    'Low risk',
    'High volatility',
    'Stable growth',
    'High dividends',
    'B',
    'A high beta indicates high volatility relative to the market.'
)

add_question(
    'Fundamentals_of_Investment',
    'Alpha in investing refers to:',
    'Portfolio diversification',
    'Risk-free rate of return',
    'Excess return over a benchmark',
    'Expected inflation',
    'C',
    'Alpha measures the excess return over a benchmark index.'
)

add_question(
    'Fundamentals_of_Investment',
    'Which portfolio theory focuses on maximizing returns for a given level of risk?',
    'Efficient market hypothesis',
    'Modern portfolio theory',
    'Behavioral finance theory',
    'Random walk theory',
    'B',
    'Modern portfolio theory seeks to maximize returns for a set level of risk.'
)

add_question(
    'Fundamentals_of_Investment',
    'What is the main purpose of diversification in a portfolio?',
    'Increase returns',
    'Reduce taxes',
    'Spread risk',
    'Increase volatility',
    'C',
    'Diversification helps to spread and reduce risk.'
)

add_question(
    'Fundamentals_of_Investment',
    'Which of the following represents a risk-free investment?',
    'Corporate bonds',
    'Government bonds',
    'Stocks',
    'Real estate',
    'B',
    'Government bonds, especially U.S. Treasury bonds, are considered risk-free.'
)

add_question(
    'Fundamentals_of_Investment',
    'What is a commonly used measure to assess the performance of an investment?',
    'P/E ratio',
    'Return on investment (ROI)',
    'Risk-adjusted return',
    'Dividends',
    'B',
    'Return on Investment (ROI) measures an investment\'s performance.'
)

add_question(
    'Fundamentals_of_Investment',
    'What is considered an optimal risky portfolio?',
    'A portfolio with the highest return',
    'A portfolio with the lowest risk',
    'A portfolio with the best risk-return balance',
    'A portfolio with no stocks',
    'C',
    'An optimal risky portfolio balances risk and return most efficiently.'
)

add_question(
    'Fundamentals_of_Investment',
    'The CAPM model primarily assesses which type of risk?',
    'Systematic risk',
    'Unsystematic risk',
    'Credit risk',
    'Inflation risk',
    'A',
    'The CAPM model assesses systematic (market) risk.'
)

add_question(
    'Fundamentals_of_Investment',
    'What is the purpose of the Efficient Frontier in investing?',
    'Shows the best portfolios for risk and return',
    'Tracks stock price movements',
    'Forecasts market trends',
    'Measures asset correlation',
    'A',
    'The Efficient Frontier shows the best portfolios for balancing risk and return.'
)

questions = fetch_questions('Fundamentals_of_Investment')
for question in questions:
    print(question)

add_question(
    'Computer_Forensics',
    'What is the primary goal of computer forensics?',
    'To secure computers from hackers',
    'To extract and preserve digital evidence',
    'To create new software',
    'To build faster computers',
    'B',
    'The main goal of computer forensics is to extract and preserve digital evidence for legal cases.'
)

add_question(
    'Computer_Forensics',
    'Which of the following is a popular tool used in computer forensics?',
    'Microsoft Excel',
    'FTK (Forensic Toolkit)',
    'Adobe Photoshop',
    'AutoCAD',
    'B',
    'FTK is widely used in computer forensics to analyze digital evidence.'
)

add_question(
    'Computer_Forensics',
    'What does the term "chain of custody" refer to in computer forensics?',
    'Steps to clean a device',
    'The procedure of handling and documenting evidence',
    'The programming of antivirus software',
    'The technique of data encryption',
    'B',
    'Chain of custody is the procedure of handling and documenting evidence from collection to presentation.'
)

add_question(
    'Computer_Forensics',
    'Which file format is commonly used to store disk images in computer forensics?',
    'JPEG',
    'PNG',
    'E01',
    'MP3',
    'C',
    'E01 is a common file format used for disk images in computer forensics.'
)

add_question(
    'Computer_Forensics',
    'What is the main purpose of hashing in computer forensics?',
    'To compress files',
    'To verify data integrity',
    'To encrypt data',
    'To format disks',
    'B',
    'Hashing is used to verify the integrity of digital data in forensics.'
)

add_question(
    'Computer_Forensics',
    'Which type of analysis involves examining the metadata of files?',
    'File system analysis',
    'Registry analysis',
    'Network analysis',
    'Metadata analysis',
    'D',
    'Metadata analysis focuses on examining the metadata of files.'
)

add_question(
    'Computer_Forensics',
    'In which scenario would computer forensics be used?',
    'To create a computer virus',
    'To recover lost email evidence',
    'To develop new programming languages',
    'To optimize computer hardware',
    'B',
    'Computer forensics is often used to recover digital evidence, such as lost emails.'
)

add_question(
    'Computer_Forensics',
    'Which of the following refers to hidden data on a digital device?',
    'Source code',
    'Metadata',
    'Steganography',
    'Firmware',
    'C',
    'Steganography is the technique of hiding data within other files or media.'
)

add_question(
    'Computer_Forensics',
    'What is a key challenge in handling digital evidence?',
    'Ensuring data remains confidential',
    'Maintaining integrity and authenticity',
    'Optimizing computer speed',
    'Creating backups',
    'B',
    'Maintaining data integrity and authenticity is critical when handling digital evidence.'
)

add_question(
    'Computer_Forensics',
    'Which protocol is commonly examined in network forensics?',
    'HTTP',
    'FTP',
    'TCP/IP',
    'SMTP',
    'C',
    'TCP/IP is a foundational protocol often examined in network forensics.'
)
questions = fetch_questions('Computer_Forensics')
for question in questions:
    print(question)

add_question(
    'Business_Analytics',
    'Which software is commonly used for data analysis in business analytics?',
    'Photoshop',
    'Excel',
    'AutoCAD',
    'Illustrator',
    'B',
    'Excel is widely used for data analysis in business analytics.'
)

add_question(
    'Business_Analytics',
    'What is the main purpose of data modeling?',
    'To create 3D visuals',
    'To structure data for analysis',
    'To develop websites',
    'To create presentations',
    'B',
    'Data modeling structures data in a way that is useful for analysis.'
)

add_question(
    'Business_Analytics',
    'What does a pivot table in Excel allow you to do?',
    'Create presentations',
    'Run simulations',
    'Summarize and analyze data',
    'Format text',
    'C',
    'A pivot table helps summarize and analyze large data sets in Excel.'
)

add_question(
    'Business_Analytics',
    'Which of the following is a common data visualization technique?',
    'Binary coding',
    'Network configuration',
    'Histogram',
    'Audio mixing',
    'C',
    'A histogram is a popular data visualization technique to show frequency distributions.'
)

add_question(
    'Business_Analytics',
    'In Excel, what function is used to calculate the average of a range of cells?',
    'SUM',
    'COUNT',
    'AVERAGE',
    'MAX',
    'C',
    'The AVERAGE function is used to calculate the mean value of a range in Excel.'
)

add_question(
    'Business_Analytics',
    'Which statistical measure shows the middle value in a data set?',
    'Mean',
    'Median',
    'Mode',
    'Range',
    'B',
    'The median is the middle value of an ordered data set.'
)

add_question(
    'Business_Analytics',
    'What is the primary use of regression analysis in business analytics?',
    'Designing websites',
    'Predicting future trends',
    'Securing data',
    'Creating presentations',
    'B',
    'Regression analysis is primarily used to predict future trends based on historical data.'
)

add_question(
    'Business_Analytics',
    'In a scatter plot, what does each point represent?',
    'A summary of data',
    'An individual data point',
    'A text annotation',
    'An image',
    'B',
    'In a scatter plot, each point represents an individual data observation.'
)

add_question(
    'Business_Analytics',
    'What type of chart is commonly used to display data distribution?',
    'Line chart',
    'Pie chart',
    'Bar chart',
    'Histogram',
    'D',
    'A histogram is commonly used to display data distribution.'
)

add_question(
    'Business_Analytics',
    'Which Excel feature allows you to automate repetitive tasks?',
    'Formulas',
    'Macros',
    'Graphs',
    'Sorting',
    'B',
    'Macros are used in Excel to automate repetitive tasks.'
)
questions = fetch_questions('Business_Analytics')
for question in questions:
    print(question)

add_question(
    'Business_Application_Development',
    'Which programming language is commonly taught for business application development?',
    'Java',
    'Python',
    'C++',
    'Ruby',
    'B',
    'Python is widely used for business applications due to its versatility and ease of use.'
)

add_question(
    'Business_Application_Development',
    'What is an IDE?',
    'Integrated Data Environment',
    'Internal Development Ecosystem',
    'Integrated Development Environment',
    'Internal Debugging Engine',
    'C',
    'IDE stands for Integrated Development Environment, a tool for coding and debugging.'
)

add_question(
    'Business_Application_Development',
    'Which of the following is a popular Python library for data analysis?',
    'NumPy',
    'Bootstrap',
    'React',
    'TensorFlow',
    'A',
    'NumPy is a popular Python library used for data analysis and numerical computation.'
)

add_question(
    'Business_Application_Development',
    'What does "API" stand for in programming?',
    'Application Programming Interface',
    'Automated Processing Integration',
    'Analytical Program Interface',
    'Applied Processing Intelligence',
    'A',
    'API stands for Application Programming Interface, which allows communication between software applications.'
)

add_question(
    'Business_Application_Development',
    'Which of the following is a version control system?',
    'FTP',
    'Git',
    'JSON',
    'SQL',
    'B',
    'Git is a version control system commonly used for tracking code changes.'
)

add_question(
    'Business_Application_Development',
    'What is the purpose of a function in Python?',
    'To store data',
    'To execute a specific task',
    'To visualize data',
    'To retrieve data from a database',
    'B',
    'A function is used to execute a specific task or set of instructions in code.'
)

add_question(
    'Business_Application_Development',
    'Which keyword is used to define a function in Python?',
    'define',
    'func',
    'def',
    'function',
    'C',
    'The "def" keyword is used to define a function in Python.'
)

add_question(
    'Business_Application_Development',
    'What is the main purpose of exception handling in Python?',
    'To handle code documentation',
    'To prevent syntax errors',
    'To manage runtime errors',
    'To speed up the code',
    'C',
    'Exception handling is used to manage runtime errors in Python programs.'
)

add_question(
    'Business_Application_Development',
    'Which Python library is commonly used for creating web applications?',
    'NumPy',
    'Flask',
    'Pandas',
    'Matplotlib',
    'B',
    'Flask is a popular Python library for developing web applications.'
)

add_question(
    'Business_Application_Development',
    'What does JSON stand for?',
    'JavaScript Object Notation',
    'Java Standard Output',
    'Joint System Operation Network',
    'Jupyter Script Output Notation',
    'A',
    'JSON stands for JavaScript Object Notation, a format for structuring data.'
)

questions = fetch_questions('Business_Application_Development')
for question in questions:
    print(question)


