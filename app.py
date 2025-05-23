import streamlit as st
import base64

st.set_page_config(page_title="Vishal Girase | Portfolio", layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_base64 = get_base64_of_bin_file("azure_backround_logo.png")
bg_base64 = get_base64_of_bin_file("background.jpg")

# Style Definitions
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('data:image/jpeg;base64,{bg_base64}');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center center;
        background-attachment: fixed;
    }}
    .header-container {{
        background-color: rgba(0, 0, 0, 0.75);
        padding: 25px;
        border-radius: 12px;
        margin-top: 20px;
        color: white !important;
        width: 100%;
    }}
    .section-container {{
        background-color: rgba(0, 0, 0, 0.75);
        padding: 25px;
        border-radius: 12px;
        margin-bottom: 25px;
        color: white !important;
    }}
    .adf-project-bg {{
        background-image: url('data:image/png;base64,{img_base64}') !important;
        background-size: cover !important;
        background-repeat: no-repeat !important;
        background-position: center !important;
        background-color: rgba(230, 240, 250, 0.85) !important;
        box-shadow: 0 4px 6px rgba(0, 120, 212, 0.1) !important;
        color: #0b2e59 !important;
        font-weight: 500 !important;
        border-radius: 12px !important;
        padding: 25px !important;
        margin-bottom: 20px;
    }}
    .dark-section-text h3,
    .dark-section-text p,
    .dark-section-text ul,
    .dark-section-text li,
    .dark-section-text a {{
        color: #0b2e59 !important;
    }}
    .white-link {{
        color: white !important;
        text-decoration: none;
        font-weight: 500;
    }}
    .white-link:hover {{
        color: #add8e6 !important;
        text-decoration: underline;
    }}
    .dark-link {{
        color: #0b2e59 !important;
        text-decoration: none;
        font-weight: 500;
    }}
    .dark-link:hover {{
        color: #0078d4 !important;
        text-decoration: underline;
    }}
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {{
        font-size: 1rem;
    }}
    .project-tab {{
        background-color: rgba(0, 0, 0, 0.1);
    }}
    hr {{
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 30px 0;
    }}
    * {{
        color: white !important;
    }}
    </style>
""", unsafe_allow_html=True)

# Header Section
col1, col2 = st.columns([1.5, 2])

with col1:
    st.image("Vishal_Girase.jpg", width=350)

with col2:
    st.markdown("""
    <div class="header-container">
    <h1>👋 Hi, I'm Vishal Girase</h1>
    <p>📧 <a href="mailto:vishal1997girase@gmail.com" class="white-link">vishal1997girase@gmail.com</a> 
    💼 <a href="https://www.linkedin.com/in/vishal-girase/" target="_blank" class="white-link">LinkedIn</a></p>
    <p>North York, Toronto | +1 437 662 0424</p>
    <p><strong>Versatile Data Professional | Expert Data Engineer & Analyst</strong></p>
    <p>Proficient in ETL, SQL, Python, Azure(ADF | Databricks | Synpase) | Data Modeling & Visualization Enthusiast</p>
    </div>
    """, unsafe_allow_html=True)

# Profile Summary
with st.container():
    st.markdown("""
    <div class="section-container">
    <h2>🔍 Profile Summary</h2>
    <p>I am a versatile and accountable Data Engineer with over 4 years of industry experience, specializing in designing and building scalable data pipelines using PySpark, SQL, and Python. My expertise spans across data engineering, analytics, and visualization, with a solid foundation in cloud platforms such as Azure (ADF, Databricks, Synapse and key-vault).</p>
    <p>I have a proven track record of working in fast-paced environments, collaborating closely with cross-functional teams and clients to translate business needs into efficient data solutions. I'm highly proficient in ETL workflows, data modeling on pharma, real-estate and banking domain data.</p>
    <strong>Key Highlights:</strong>
    <ul>
    <li>Proficient in PySpark, SQL, Hive, and PL/SQL for end-to-end data engineering</li>
    <li>Experienced with Azure (ADF, Databricks, Delta Lake, Synapse)</li>
    <li>Adept at debugging, optimizing ETL pipelines, and building scalable data solutions</li>
    <li>Hands-on with analytics tools like Power BI, Tableau, and real-time data ingestion</li>
    <li>Strong communicator and collaborator with a client-focused mindset</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Work Experience
with st.container():
    st.markdown("""
    <div class="section-container">
    <h2>💼 Work Experience</h2>

    <strong>Data Engineer | Cognizant, India (07/2021 - 08/2023)</strong><br>
    <ul>
    <li>Worked on projects involving PySpark, Python, Kafka, Hive, Azure Data Lake, Azure Databricks, Azure DataFactory, Azure Synapse and Key-Vault</li>
    <li>Key achievements include building and maintaining ETL pipelines, automating data workflows, and managing data integration across platforms</li>
    </ul>

    <strong>Data Engineer | TCS, India (06/2019 - 06/2021)</strong><br>
    <ul>
    <li>Focused on SQL, PL/SQL, Python, and Databricks for data warehousing solutions (SCD type 1 and 2)</li>
    <li>Participated in Agile teams, created scripts, and developed documentation for large scale projects</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Projects Section
with st.container():
    st.markdown("""
    <div class="section-container">
    <h2>📁 Projects</h2>
    </div>
    """, unsafe_allow_html=True)

    project_tabs = st.tabs(["ADF Project", "PySpark Hands-on"])

    with project_tabs[0]:
        st.markdown(f"""
        <div class="adf-project-bg dark-section-text">
            <h3>Azure Data Factory (ADF) Project</h3>
            <p>GitHub Repo : <a href="https://github.com/VishalGirase/ADF/tree/Dev" target="_blank" class="dark-link">ADF Project</a></p>
            <p>ReadMe : <a href="https://github.com/VishalGirase/ADF/blob/Dev/README.md" target="_blank" class="dark-link">Project Explanation</a></p>
            <p>Developed an Azure Data Factory pipeline for automated data ingestion, transformation, and load</p>
            <ul>
                <li>Scheduled pipeline execution</li>
                <li>Integration with Azure Blob and SQL</li>
                <li>Monitoring and alerting setup</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with project_tabs[1]:
        st.markdown("""
        <div class="section-container">
            <h3>PySpark Hands-on</h3>
            <p><strong>GitHub Repo:</strong> <a href="https://github.com/VishalGirase/Pyspark_Handson/tree/main/Pyspark" target="_blank" class="white-link">Pyspark Handson</a></p>
            <p>Hands-on implementation of PySpark scripts for:</p>
            <ul>
                <li>Data wrangling and cleansing</li>
                <li>Joins, aggregations, and window functions</li>
                <li>Loading and transforming large datasets</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
