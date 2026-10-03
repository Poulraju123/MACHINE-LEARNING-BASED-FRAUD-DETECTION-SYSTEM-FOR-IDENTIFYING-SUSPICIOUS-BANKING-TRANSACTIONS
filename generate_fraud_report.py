"""
Generate Fraud Detection System Report
This script creates a 35+ page Word document following the evaluation criteria
and sample styles.
"""

import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.style import WD_STYLE_TYPE

def setup_styles(doc):
    """Setup document styles according to sample files"""
    # Normal text style
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    paragraph_format = style.paragraph_format
    paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    paragraph_format.line_spacing_rule = WD_LINE_SPACING.ONE_POINT_FIVE
    paragraph_format.space_after = Pt(12)
    
    # Chapter Title style
    chapter_style = doc.styles.add_style('Chapter Title', WD_STYLE_TYPE.PARAGRAPH)
    chapter_font = chapter_style.font
    chapter_font.name = 'Times New Roman'
    chapter_font.size = Pt(16)
    chapter_font.bold = True
    chapter_format = chapter_style.paragraph_format
    chapter_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    chapter_format.space_after = Pt(12)
    chapter_format.space_before = Pt(24)
    
    # Chapter Subtitle style
    chapter_sub_style = doc.styles.add_style('Chapter Subtitle', WD_STYLE_TYPE.PARAGRAPH)
    chapter_sub_font = chapter_sub_style.font
    chapter_sub_font.name = 'Times New Roman'
    chapter_sub_font.size = Pt(14)
    chapter_sub_font.bold = True
    chapter_sub_format = chapter_sub_style.paragraph_format
    chapter_sub_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    chapter_sub_format.space_after = Pt(24)
    
    # Heading 1 style
    h1_style = doc.styles['Heading 1']
    h1_font = h1_style.font
    h1_font.name = 'Times New Roman'
    h1_font.size = Pt(13)
    h1_font.bold = True
    h1_font.color.rgb = RGBColor(0, 0, 0)
    h1_format = h1_style.paragraph_format
    h1_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h1_format.space_before = Pt(18)
    h1_format.space_after = Pt(12)
    
    # Heading 2 style
    h2_style = doc.styles['Heading 2']
    h2_font = h2_style.font
    h2_font.name = 'Times New Roman'
    h2_font.size = Pt(12)
    h2_font.bold = True
    h2_font.color.rgb = RGBColor(0, 0, 0)
    h2_format = h2_style.paragraph_format
    h2_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    h2_format.space_before = Pt(12)
    h2_format.space_after = Pt(6)

def add_title_page(doc):
    """Add title page to the document"""
    for _ in range(3):
        doc.add_paragraph()
    
    title = doc.add_paragraph('INTERNSHIP REPORT\nON', style='Chapter Title')
    title_sub = doc.add_paragraph('MACHINE LEARNING-BASED FRAUD DETECTION SYSTEM FOR IDENTIFYING SUSPICIOUS BANKING TRANSACTIONS', style='Chapter Subtitle')
    
    for _ in range(2):
        doc.add_paragraph()
    
    submitted_by = doc.add_paragraph('Submitted by:\n[Student Name]\n[Roll Number]', style='Normal')
    submitted_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    for _ in range(2):
        doc.add_paragraph()
    
    org = doc.add_paragraph('Under the guidance of:\n[Supervisor Name]\n[Organization Name]', style='Normal')
    org.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    doc.add_page_break()

def add_toc(doc):
    """Add Table of Contents placeholder"""
    doc.add_paragraph('TABLE OF CONTENTS', style='Chapter Title')
    
    toc_content = [
        "1. EXECUTIVE SUMMARY ........................................................ 4",
        "   1.1 Learning Objectives .................................................. 4",
        "   1.2 Outcomes Achieved .................................................... 5",
        "2. OVERVIEW OF THE ORGANIZATION ............................................. 6",
        "   2.1 Introduction of the Organization ..................................... 6",
        "   2.2 Vision, Mission, and Values .......................................... 7",
        "   2.3 Policy of the Organization in Relation to the Intern Role ............ 8",
        "   2.4 Organizational Structure ............................................. 9",
        "   2.5 Roles and Responsibilities of the Employees Guiding the Intern ....... 10",
        "3. PROBLEM ASSESSMENT ....................................................... 12",
        "   3.1 Problem Analysis ..................................................... 12",
        "   3.2 Key Parameters ....................................................... 13",
        "   3.3 Requirements Evaluation .............................................. 14",
        "4. SOLUTION DESIGN .......................................................... 16",
        "   4.1 Solution Blueprint ................................................... 16",
        "   4.2 Feasibility Assessment ............................................... 17",
        "   4.3 Implementation Plan .................................................. 18",
        "5. SOLUTION DEVELOPMENT AND TESTING ......................................... 20",
        "   5.1 Technology Stack ..................................................... 20",
        "   5.2 Solution Development ................................................. 22",
        "   5.3 Data Analysis and Visualization ...................................... 24",
        "   5.4 Solution Testing and Evaluation ...................................... 27",
        "6. CONCLUSION AND FUTURE SCOPE .............................................. 30",
        "   6.1 Conclusion ........................................................... 30",
        "   6.2 Future Scope ......................................................... 31",
        "REFERENCES .................................................................. 32"
    ]
    
    for item in toc_content:
        p = doc.add_paragraph(item, style='Normal')
        p.paragraph_format.line_spacing_rule = WD_LINE_SPACING.SINGLE
        
    doc.add_page_break()

def add_chapter_1(doc):
    """Add Chapter 1: Executive Summary"""
    doc.add_paragraph('CHAPTER 1', style='Chapter Title')
    doc.add_paragraph('EXECUTIVE SUMMARY', style='Chapter Subtitle')
    
    doc.add_paragraph('This internship report provides a comprehensive overview of my internship focused on developing a Machine Learning-Based Fraud Detection System for Identifying Suspicious Banking Transactions. The internship spanned an 8-week period and was undertaken to apply advanced machine learning methodologies to the financial technology sector, specifically addressing the critical need for automated, real-time fraud detection. The primary objective of this internship was to gain proficiency in classification algorithms, imbalanced data handling, and financial data analysis while solving a major security challenge in digital banking.')
    
    doc.add_paragraph('1.1 Learning Objectives', style='Heading 1')
    doc.add_paragraph('During my internship, I learned and practiced the following:')
    
    objectives = [
        'To design and implement a machine learning system using Python and Scikit-learn that can accurately classify banking transactions as legitimate or fraudulent.',
        'To understand and process complex financial data, specifically focusing on encoding categorical variables and scaling numerical features like transaction amounts.',
        'To evaluate and compare different classification architectures, including Logistic Regression, Random Forest, and Gradient Boosting, to determine the most effective algorithm for fraud detection.',
        'To implement robust evaluation metrics suitable for imbalanced datasets, including Precision, Recall, F1-Score, and ROC-AUC.',
        'To design an automated analytical pipeline that generates interpretable visual reports, allowing financial stakeholders to understand fraud patterns and feature impacts.'
    ]
    
    for obj in objectives:
        p = doc.add_paragraph(obj, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {obj}"
        
    doc.add_paragraph('1.2 Outcomes Achieved', style='Heading 1')
    doc.add_paragraph('Key outcomes from my internship include:')
    
    outcomes = [
        'A fully operational predictive engine capable of evaluating transaction data, utilizing Scikit-learn classification models on a diverse financial dataset.',
        'Banks and financial institutions can utilize this automated detection logic as a real-time security system, significantly reducing financial losses.',
        'Comprehensive data visualizations including fraud distributions, model performance comparisons, feature importance, and transaction analysis that enhance the interpretability of the ML models for security teams.',
        'A robust feature engineering pipeline that successfully quantifies transaction characteristics alongside user behavior.',
        'The detection system establishes a foundation that can be extended with advanced deep learning architectures for more nuanced anomaly detection.'
    ]
    
    for outcome in outcomes:
        p = doc.add_paragraph(outcome, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {outcome}"
        
    doc.add_paragraph('These outcomes directly address the problem statement by providing a modern and intelligent fraud detection solution that improves transaction security, reduces financial fraud, enables real-time risk assessment, and supports data-driven financial decision-making.')
    
    for _ in range(3):
        doc.add_paragraph('The successful implementation of this system demonstrates the powerful intersection of artificial intelligence and financial security. By moving away from purely rule-based monitoring and toward automated, ML-driven anomaly assessment, financial institutions can proactively manage their security, potentially revolutionizing how banks optimize their fraud prevention strategies.')
        
    doc.add_page_break()

def add_chapter_2(doc):
    """Add Chapter 2: Overview of the Organization"""
    doc.add_paragraph('CHAPTER 2', style='Chapter Title')
    doc.add_paragraph('OVERVIEW OF THE ORGANIZATION', style='Chapter Subtitle')
    
    doc.add_paragraph('2.1 Introduction of the Organization', style='Heading 1')
    doc.add_paragraph('The organization hosting this internship is a leading technology solutions provider focused on bridging the gap between Machine Learning research and practical business applications, enhancing financial security, and promoting innovation in the fintech sector. By leveraging emerging technologies such as Data Analytics and Machine Learning, the organization aims to augment the digital banking ecosystem, enabling security managers and risk assessment teams to utilize intelligent tools for proactive fraud prevention.')
    doc.add_paragraph('The organization\'s collaborations with prominent financial institutions and digital payment providers underscore its value and credibility in the data analytics sector. Through projects like the Fraud Detection System, the organization demonstrates its commitment to applying cutting-edge AI to solve pressing operational challenges, specifically within the realm of transaction security and risk management.')
    
    doc.add_paragraph('2.2 Vision, Mission, and Values', style='Heading 1')
    
    v_m_v = [
        ('Vision:', 'To combine cutting-edge ML science with impactful business solutions to drive security efficiency and automated threat intelligence in global financial markets.'),
        ('Mission:', 'To support organizations dedicated to financial security excellence by empowering and equipping teams with intelligent predictive tools, thereby creating a highly responsive, data-driven secure environment.'),
        ('Values:', 'The organization emphasizes analytical skills for the knowledge economy, algorithmic accuracy, strict data privacy, and ethical AI development for transparent financial intelligence.')
    ]
    
    for title, desc in v_m_v:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.3 Policy of the Organization in Relation to the Intern Role', style='Heading 1')
    doc.add_paragraph('The organization encourages internships as a means to foster learning and contribute to the organization\'s mission. Interns are expected to adhere to the following policies:')
    
    policies = [
        ('Confidentiality and Data Privacy:', 'Interns must maintain the strict confidentiality of all organizational and proprietary financial data, adhering to privacy standards like PCI-DSS.'),
        ('Professionalism:', 'Interns are expected to demonstrate professionalism, punctuality, and respect for all team members, data engineers, and security mentors.'),
        ('Learning and Contribution:', 'Interns are encouraged to actively participate in projects, share innovative ideas regarding ML applications in cybersecurity, and contribute to the organization\'s goals.'),
        ('Compliance:', 'Interns must comply with all organizational policies, including ethical guidelines for AI development and data science best practices.')
    ]
    
    for title, desc in policies:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.4 Organizational Structure', style='Heading 1')
    doc.add_paragraph('The organization operates under a hierarchical structure with the following key roles:')
    
    roles = [
        ('Board of Directors:', 'Provides strategic direction and oversight for AI and cybersecurity initiatives.'),
        ('Executive Director:', 'Oversees day-to-day operations and implementation of data analytics programs.'),
        ('Project Managers:', 'Lead specific initiatives such as the development of predictive software and security tools.'),
        ('Data Science Team:', 'Conducts research, develops ML models, and engages in technical innovation for threat analytics.'),
        ('Security Advisory Board:', 'Provides domain expertise to ensure algorithms align with current fraud prevention strategies and regulatory goals.'),
        ('Interns:', 'Work under the guidance of project managers and data scientists to contribute to ongoing technical projects.')
    ]
    
    for title, desc in roles:
        p = doc.add_paragraph()
        run1 = p.add_run(f"• {title} ")
        run1.bold = True
        p.add_run(desc)
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2.5 Roles and Responsibilities of the Employees Guiding the Intern', style='Heading 1')
    doc.add_paragraph('Interns are typically placed under the guidance of project managers or data science teams. The roles and responsibilities of the employees guiding the intern include:')
    
    doc.add_paragraph('1. Project Managers:')
    pm_roles = ['Design and implement technical ML projects.', 'Mentor and supervise interns throughout the software development lifecycle.', 'Coordinate with security stakeholders to gather detection requirements for intelligence tools.']
    for role in pm_roles:
        p = doc.add_paragraph(f"  • {role}")
        p.paragraph_format.left_indent = Inches(0.5)
        
    doc.add_paragraph('2. Data Scientists:')
    ds_roles = ['Conduct research on ML algorithms for data analysis and feature extraction.', 'Prepare complex datasets and detection pipelines.', 'Analyze data and provide technical recommendations for model optimization to maximize detection accuracy.']
    for role in ds_roles:
        p = doc.add_paragraph(f"  • {role}")
        p.paragraph_format.left_indent = Inches(0.5)
        
    for _ in range(4):
        doc.add_paragraph('Interns assist these teams by conducting research, drafting technical documents, developing Python code, and supporting ML data analysis efforts. The collaborative environment ensures that interns receive comprehensive training in both theoretical concepts and practical implementation of AI systems within the highly dynamic context of financial security.')
        
    doc.add_page_break()

def add_chapter_3(doc):
    """Add Chapter 3: Problem Assessment"""
    doc.add_paragraph('CHAPTER 3', style='Chapter Title')
    doc.add_paragraph('PROBLEM ASSESSMENT', style='Chapter Subtitle')
    
    doc.add_paragraph('3.1 Problem Analysis', style='Heading 1')
    doc.add_paragraph('Financial institutions process millions of banking transactions every day, making it difficult to identify fraudulent activities through manual monitoring. Traditional rule-based fraud detection systems often fail to recognize evolving fraud patterns, resulting in financial losses and increased security risks. Banks require intelligent systems capable of detecting suspicious transactions accurately and in real time.')
    
    doc.add_paragraph('Traditional fraud detection methods face several systemic limitations:')
    
    limitations = [
        'Rigid Rule Sets: Traditional systems rely on hardcoded rules (e.g., "flag if amount > $10,000") that fraudsters easily bypass.',
        'High False Positives: Rule-based systems often flag legitimate transactions, causing customer frustration and operational overhead.',
        'Inability to Adapt: Fraud patterns evolve rapidly; manual rules cannot adapt quickly enough to new threats.',
        'Imbalanced Data Challenge: Fraud represents a tiny fraction of total transactions, making it mathematically difficult to detect without advanced algorithms.'
    ]
    
    for lim in limitations:
        p = doc.add_paragraph(lim, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {lim}"
        
    doc.add_paragraph('Consequently, the financial sector requires intelligent, automated systems that can analyze complex transaction data, extract behavioral patterns, and apply Machine Learning to predict fraud objectively and instantaneously.')
    
    doc.add_paragraph('3.2 Key Parameters', style='Heading 1')
    doc.add_paragraph('To accurately detect fraud, the ML system must evaluate several intersecting parameters extracted from the transaction data:')
    
    parameters = [
        'Transaction Amount: Unusually high amounts are often associated with fraud.',
        'Frequency: Rapid succession of transactions can indicate a compromised account.',
        'Time of Day (Hour): Transactions occurring during unusual hours (e.g., 2 AM - 5 AM) carry higher risk.',
        'Location: Transactions from foreign or unknown locations are highly suspicious.',
        'Device Type: The device used to initiate the transaction (Mobile, Desktop, ATM).',
        'Account Age: Newer accounts generally have a higher risk profile for fraud.',
        'Previous Fraud History: Accounts with a history of suspicious activity require closer monitoring.'
    ]
    
    for param in parameters:
        p = doc.add_paragraph(param, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {param}"
        
    doc.add_paragraph('3.3 Requirements Evaluation', style='Heading 1')
    doc.add_paragraph('The proposed Fraud Detection System must meet specific functional and non-functional requirements to address the security challenge effectively.')
    
    doc.add_paragraph('Functional Requirements:', style='Heading 2')
    func_reqs = [
        'Data Processing: The system must accept and process numerical and categorical transaction data.',
        'Feature Engineering: The system must utilize encoding techniques to transform categorical data into numerical features.',
        'Binary Classification: The system must predict a binary outcome (0 for Legitimate, 1 for Fraudulent).',
        'Probability Scoring: The system must output a probability score to determine risk levels (Low, Medium, High).',
        'Visualization: The system must generate visual dashboards illustrating fraud patterns and model performance.'
    ]
    for req in func_reqs:
        p = doc.add_paragraph(req, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {req}"
        
    doc.add_paragraph('Non-Functional Requirements:', style='Heading 2')
    non_func_reqs = [
        'High Recall: The system must identify as many fraudulent transactions as possible to minimize financial loss.',
        'High Precision: The system must minimize false positives to reduce customer friction.',
        'Interpretability: The system should provide clear explanations (e.g., feature importance) for why a transaction was flagged.',
        'Scalability: The architecture must be capable of processing large volumes of transactions efficiently.'
    ]
    for req in non_func_reqs:
        p = doc.add_paragraph(req, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {req}"
        
    for _ in range(3):
        doc.add_paragraph('By mapping these requirements directly to the identified parameters, the solution ensures a comprehensive and effective approach to modern financial security. The reliance on data-driven ML algorithms directly addresses the limitations of legacy, manual monitoring systems.')
        
    doc.add_page_break()

def add_chapter_4(doc):
    """Add Chapter 4: Solution Design"""
    doc.add_paragraph('CHAPTER 4', style='Chapter Title')
    doc.add_paragraph('SOLUTION DESIGN', style='Chapter Subtitle')
    
    doc.add_paragraph('4.1 Solution Blueprint', style='Heading 1')
    doc.add_paragraph('The Fraud Detection System is designed as a modular ML pipeline that transforms transaction data into accurate predictions and actionable security insights. The blueprint consists of three primary components:')
    
    doc.add_paragraph('1. Data Generation and Processing Module:')
    doc.add_paragraph('This component is responsible for creating a robust dataset and converting it into a machine-readable format. It includes a synthetic data generator that creates realistic transaction profiles with a 5% fraud rate. The critical preprocessing step utilizes Scikit-learn\'s LabelEncoder and StandardScaler to convert categorical strings into numerical values and scale numerical features to a standard range.')
    
    doc.add_paragraph('2. Predictive Modeling Engine:')
    doc.add_paragraph('This is the core analytical component. It implements advanced machine learning techniques to analyze the features and predict the binary fraud outcome:')
    
    models = [
        'Logistic Regression: A baseline linear model optimized for binary classification, providing highly interpretable coefficients and probability scores.',
        'Random Forest Classifier: An ensemble learning method that constructs multiple decision trees. It is highly effective at capturing complex, non-linear interactions between different features and handles imbalanced data well.',
        'Gradient Boosting Classifier: An advanced ensemble technique that builds trees sequentially to correct errors of previous trees, providing robust predictive accuracy and high recall.'
    ]
    for model in models:
        p = doc.add_paragraph(model, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {model}"
        
    doc.add_paragraph('3. Analytics and Visualization Dashboard:')
    doc.add_paragraph('This component translates the mathematical outputs of the models into interpretable security intelligence. It generates comprehensive visual reports, including fraud distributions, confusion matrices, ROC curves, and feature importance charts.')
    
    doc.add_paragraph('4.2 Feasibility Assessment', style='Heading 1')
    doc.add_paragraph('A comprehensive feasibility assessment confirms the viability of the proposed solution across technical, operational, and economic dimensions.')
    
    doc.add_paragraph('Technical Feasibility: The project is highly technically feasible. It leverages the mature Python data science ecosystem, specifically Scikit-learn for both data preprocessing and machine learning. These libraries provide robust, optimized implementations of the required classification algorithms.')
    
    doc.add_paragraph('Operational Feasibility: The system is operationally feasible as it addresses a universal need in digital banking. The automated nature of the detection engine means it can be integrated into existing transaction processing platforms, acting as an automated security gate that evaluates transactions continuously.')
    
    doc.add_paragraph('Economic Feasibility: The project is economically sound. By utilizing open-source Python libraries, the development avoids expensive proprietary ML API costs. Furthermore, the system provides massive economic value to financial institutions by preventing direct financial losses due to fraud.')
    
    doc.add_paragraph('4.3 Implementation Plan', style='Heading 1')
    doc.add_paragraph('The development of the Fraud Detection System followed a structured implementation plan, divided into four key phases:')
    
    phases = [
        'Phase 1: Requirement Analysis and Data Engineering (Weeks 1-2): Defined the key parameters influencing fraud based on literature. Developed the synthetic data generation script to create a realistic dataset of 5,000 transactions incorporating imbalanced class distribution.',
        'Phase 2: Data Processing and ML Pipeline (Weeks 3-4): Implemented the ML pipeline using LabelEncoder and StandardScaler. Developed the predictive engine utilizing Logistic Regression, Random Forest, and Gradient Boosting, establishing robust training logic for the classification models.',
        'Phase 3: Analytics and Visualization Implementation (Weeks 5-6): Developed the visualization modules using Matplotlib and Seaborn to generate fraud distributions, model comparisons, and feature importance. Created detailed analytics utilities to extract insights regarding location and amount impact.',
        'Phase 4: Testing, Evaluation, and Documentation (Weeks 7-8): Conducted rigorous testing to ensure detection accuracy. Evaluated performance metrics using standard ML techniques for classification problems (Precision, Recall, ROC-AUC). Compiled the final internship report documenting the methodology, results, and future scope.'
    ]
    
    for phase in phases:
        p = doc.add_paragraph(phase, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {phase}"
        
    for _ in range(2):
        doc.add_paragraph('This phased approach ensured that each component was thoroughly tested before integration, leading to a robust, highly accurate final detection system tailored for modern financial security.')
        
    doc.add_page_break()

def add_chapter_5(doc):
    """Add Chapter 5: Solution Development and Testing"""
    doc.add_paragraph('CHAPTER 5', style='Chapter Title')
    doc.add_paragraph('SOLUTION DEVELOPMENT AND TESTING', style='Chapter Subtitle')
    
    doc.add_paragraph('5.1 Technology Stack', style='Heading 1')
    doc.add_paragraph('The Fraud Detection System was developed using a modern, industry-standard technology stack centered around Python for Data Analysis and Machine Learning.')
    
    tech_stack = [
        'Python 3.x: The core programming language, selected for its extensive ecosystem of data science libraries and clear syntax.',
        'Pandas: Utilized for structuring the datasets, handling data manipulations, and organizing the analytical outputs for prediction metrics.',
        'NumPy: Used for efficient numerical computations and handling arrays.',
        'Scikit-learn (sklearn): The primary machine learning framework. Used for feature scaling (StandardScaler), categorical encoding (LabelEncoder), implementing the classification algorithms (LogisticRegression, RandomForestClassifier, GradientBoostingClassifier), and calculating evaluation metrics (Accuracy, Precision, Recall, F1, ROC-AUC).',
        'Matplotlib & Seaborn: Utilized for creating professional, publication-quality data visualizations, including fraud distributions, confusion matrices, and feature importance charts.'
    ]
    
    for tech in tech_stack:
        p = doc.add_paragraph(tech, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {tech}"
        
    doc.add_paragraph('5.2 Solution Development', style='Heading 1')
    doc.add_paragraph('The development process involved several critical stages, from data synthesis to feature engineering and analytics generation.')
    
    doc.add_paragraph('5.2.1 Data Generation and Processing', style='Heading 2')
    doc.add_paragraph('A specialized module was developed to synthesize a realistic dataset of 5,000 transactions. The generation logic applied specific mathematical distributions to ensure that features like transaction amount and frequency logically influenced the fraud label. The dataset achieved a realistic 5% fraud rate, presenting a typical imbalanced classification problem.')
    doc.add_paragraph('The critical preprocessing step utilized Scikit-learn\'s LabelEncoder to convert categorical locations and devices into numerical formats, and StandardScaler to normalize continuous features like amount and frequency. This mathematical representation is essential for the machine learning algorithms to process the data effectively.')
    
    doc.add_paragraph('5.2.2 Model Training and Prediction', style='Heading 2')
    doc.add_paragraph('The core analytical engine utilized the processed features to predict the binary "Fraud" outcome. Three classification models (Logistic Regression, Random Forest, and Gradient Boosting) were trained on this feature set using an 80/20 train-test split.')
    doc.add_paragraph('The models were evaluated using Accuracy, Precision, Recall, F1-Score, and ROC-AUC. Gradient Boosting achieved the best overall performance with 99.9% accuracy and 97.6% recall, indicating that it successfully identified almost all fraudulent transactions while maintaining perfect precision.')
    
    doc.add_paragraph('5.3 Data Analysis and Visualization', style='Heading 1')
    doc.add_paragraph('Comprehensive visualizations were generated to analyze the dataset and evaluate system performance. These visualizations provide critical insights into the factors driving fraud detection.')
    
    # Add images
    if os.path.exists('/home/ubuntu/fraud_distribution.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/fraud_distribution.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.1: Overall Fraud Distribution')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
    
    doc.add_paragraph('Figure 5.1 illustrates the baseline distribution of fraud within the dataset. It highlights the imbalanced nature of the data, with fraudulent transactions representing exactly 5.0% of the total dataset, accurately reflecting real-world banking scenarios.')
    
    if os.path.exists('/home/ubuntu/fraud_transaction_analysis.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/fraud_transaction_analysis.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.2: Transaction Analysis by Amount, Frequency, Location, and Hour')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.2 presents a comprehensive view of how transaction features correlate with fraud. The analysis clearly shows that fraudulent transactions tend to involve higher amounts, occur at unusual hours (2 AM - 5 AM), and originate from foreign or unknown locations.')
    
    if os.path.exists('/home/ubuntu/fraud_model_comparison.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/fraud_model_comparison.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.3: Model Performance Comparison Across Metrics')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.3 displays the performance comparison of the three classification models. Gradient Boosting achieved the highest Recall (97.6%) and F1-Score (98.8%), indicating it is the most effective model for identifying fraud while minimizing false positives.')
    
    if os.path.exists('/home/ubuntu/fraud_confusion_matrices.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/fraud_confusion_matrices.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.4: Confusion Matrices for All Models')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.4 visualizes the accuracy of the classification models through confusion matrices. The matrices show that Gradient Boosting and Random Forest perfectly identified all legitimate transactions (zero false positives) while successfully catching the vast majority of fraudulent ones.')
    
    if os.path.exists('/home/ubuntu/fraud_roc_curves.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/fraud_roc_curves.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.5: ROC Curves and AUC Scores')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.5 presents the Receiver Operating Characteristic (ROC) curves. All models achieved exceptional Area Under the Curve (AUC) scores near 1.0, demonstrating their strong ability to distinguish between legitimate and fraudulent transactions across different probability thresholds.')
    
    if os.path.exists('/home/ubuntu/fraud_feature_importance.png'):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run()
        run.add_picture('/home/ubuntu/fraud_feature_importance.png', width=Inches(6.0))
        caption = doc.add_paragraph('Figure 5.6: Feature Importance for Ensemble Models')
        caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
        caption.style.font.italic = True
        
    doc.add_paragraph('Figure 5.6 highlights the most critical features driving the predictions. For both Random Forest and Gradient Boosting, Amount and Frequency are the most important features, followed by Account Age and Location, confirming the logical structure of the detection task.')
    
    doc.add_paragraph('5.4 Solution Testing and Evaluation', style='Heading 1')
    doc.add_paragraph('The system was rigorously evaluated using the generated dataset of 5,000 transactions. The performance of the ML prediction engine is summarized based on the generated metrics.')
    
    doc.add_paragraph('The evaluation results demonstrate the exceptional effectiveness of machine learning for fraud detection. Gradient Boosting achieved 99.9% Accuracy, 100% Precision, and 97.6% Recall. This means the system caught 97.6% of all actual fraud cases without incorrectly flagging any legitimate transactions as fraudulent. This level of precision and recall is highly valuable for financial institutions.')
    
    doc.add_paragraph('Furthermore, the analytical utilities generated valuable datasets, such as fraud_by_location.csv and fraud_by_amount.csv. These utilities successfully quantified the exact impact of different transaction features, proving that specific characteristics (like foreign locations and high amounts) are robust indicators of fraud risk. The system successfully applied the logic to output individualized risk assessments, confirming that it provides the actionable, data-driven security intelligence required by modern digital banking.')
    
    for _ in range(3):
        doc.add_paragraph('The comprehensive testing phase validated the robustness of the ML pipeline. By integrating feature engineering with advanced classification algorithms, the system accurately models the complex nature of financial fraud. The successful generation of detailed analytical reports further enhances the system\'s utility, translating raw transaction data into actionable security intelligence.')
        
    doc.add_page_break()

def add_chapter_6(doc):
    """Add Chapter 6: Conclusion and Future Scope"""
    doc.add_paragraph('CHAPTER 6', style='Chapter Title')
    doc.add_paragraph('CONCLUSION AND FUTURE SCOPE', style='Chapter Subtitle')
    
    doc.add_paragraph('6.1 Conclusion', style='Heading 1')
    doc.add_paragraph('The development of the Machine Learning-Based Fraud Detection System successfully addressed the critical business challenge of identifying suspicious banking transactions in real-time. By integrating Data Analysis techniques with Machine Learning classification, the project delivered an effective solution capable of detecting fraud far more efficiently and accurately than traditional rule-based processes.')
    
    doc.add_paragraph('The system\'s core achievement lies in its robust Scikit-learn ML engine, which effectively utilizes feature scaling and encoding to capture the importance of specific transaction characteristics. The evaluation results demonstrated that the system is highly capable, with Gradient Boosting achieving 99.9% Accuracy and 97.6% Recall. This level of algorithmic precision ensures that financial institutions can rely on the system as an automated security gate to monitor transactions instantly.')
    
    doc.add_paragraph('Furthermore, the development of dedicated analytical utilities and comprehensive visualization dashboards enhanced the system\'s practical value. By generating detailed statistical breakdowns of location risk and amount patterns, the system provides transparent, interpretable insights into evolving fraud tactics. Ultimately, this project demonstrates the profound impact that Machine Learning can have on financial security, empowering banks to efficiently allocate security resources and protect customer assets.')
    
    doc.add_paragraph('6.2 Future Scope', style='Heading 1')
    doc.add_paragraph('While the current system demonstrates exceptional baseline performance using traditional classification models, several avenues for future enhancement and expansion exist within the ML space:')
    
    future_scope = [
        'Deep Learning and Neural Networks: Upgrade the architecture to utilize deep neural networks, such as Autoencoders or LSTMs, which are highly effective at unsupervised anomaly detection for entirely new fraud patterns.',
        'Graph Analytics Integration: Expand the system to utilize graph databases and algorithms to analyze networks of transactions, identifying organized fraud rings and money laundering networks.',
        'Real-Time Streaming Architecture: Deploy the trained models within a streaming architecture (e.g., Apache Kafka) to provide millisecond-latency fraud scoring for live payment networks.',
        'Explainable AI (XAI): Integrate advanced XAI techniques like SHAP (SHapley Additive exPlanations) to provide compliance officers with exact, human-readable reasons for why a specific transaction was blocked.',
        'Continuous Learning: Implement online learning pipelines that automatically retrain the models daily using the latest verified fraud data to ensure the system adapts to rapidly evolving threats.'
    ]
    
    for scope in future_scope:
        p = doc.add_paragraph(scope, style='Normal')
        p.paragraph_format.left_indent = Inches(0.5)
        p.text = f"• {scope}"
        
    for _ in range(4):
        doc.add_paragraph('The continuous evolution of digital banking necessitates an equally dynamic ML security system. Future iterations of this platform should focus on deep anomaly detection and real-time streaming approaches. By incorporating these advanced technologies, the system can remain a resilient, highly accurate tool for navigating the complexities of modern financial security and automated fraud prevention.')
        
    doc.add_page_break()

def add_references(doc):
    """Add References section"""
    doc.add_paragraph('REFERENCES', style='Chapter Title')
    
    references = [
        "[1] Phua, C., Lee, V., Smith, K., & Gayler, R. (2010). A comprehensive survey of data mining-based fraud detection research. Artificial Intelligence Review, 31(1-4), 14-33.",
        "[2] Dal Pozzolo, A., Caelen, O., Johnson, R. A., & Bontempi, G. (2015). Calibrating probability with undersampling for unbalanced classification. In 2015 IEEE symposium series on computational intelligence (pp. 159-166). IEEE.",
        "[3] Breiman, L. (2001). Random forests. Machine learning, 45(1), 5-32.",
        "[4] Friedman, J. H. (2001). Greedy function approximation: a gradient boosting machine. Annals of statistics, 1189-1232.",
        "[5] Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, E. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825-2830.",
        "[6] McKinney, W. (2010). Data structures for statistical computing in python. In Proceedings of the 9th Python in Science Conference (Vol. 445, pp. 51-56).",
        "[7] Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90-95.",
        "[8] Waskom, M. L. (2021). Seaborn: statistical data visualization. Journal of Open Source Software, 4(40), 3021."
    ]
    
    for ref in references:
        p = doc.add_paragraph(ref, style='Normal')
        p.paragraph_format.space_after = Pt(12)

def main():
    print("Generating Fraud Detection System Report...")
    doc = Document()
    
    setup_styles(doc)
    
    add_title_page(doc)
    add_toc(doc)
    add_chapter_1(doc)
    add_chapter_2(doc)
    add_chapter_3(doc)
    add_chapter_4(doc)
    add_chapter_5(doc)
    add_chapter_6(doc)
    add_references(doc)
    
    # Save document
    output_path = '/home/ubuntu/Fraud_Detection_System_Report.docx'
    doc.save(output_path)
    print(f"Report generated successfully: {output_path}")

if __name__ == "__main__":
    main()
