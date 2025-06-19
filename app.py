import streamlit as st
import base64

st.set_page_config(page_title="Vishal Girase | Portfolio", layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_base64 = get_base64_of_bin_file("azure_backround_logo.png")
img_base_2_64 = get_base64_of_bin_file("databricks.jpeg")
img_base_3_64 = get_base64_of_bin_file("pyspark_1.png")
img_base_4_64 = get_base64_of_bin_file("azure-synapse-analytics.jpg")
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
    .databricks-project-bg {{
        background-image: url('data:image/png;base64,{img_base_2_64}') !important;
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
    .pyspark-project-bg {{
        background-image: url('data:image/png;base64,{img_base_3_64}') !important;
        background-size: cover !important;
        background-repeat: no-repeat !important;
        background-position: right !important;
        background-color: rgba(230, 240, 250, 0.5) !important;
        box-shadow: 0 4px 6px rgba(0, 120, 212, 0.1) !important;
        color: #0b2e59 !important;
        font-weight: 500 !important;
        border-radius: 12px !important;
        padding: 25px !important;
        margin-bottom: 20px;
    }}
    .azure-synapse-project-bg {{
        background-image: url('data:image/png;base64,{img_base_4_64}') !important;
        background-size: cover !important;
        background-repeat: no-repeat !important;
        background-position: right !important;
        background-color: rgba(230, 240, 250, 0.5) !important;
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

# with col1:
#     st.image("Vishal_Girase.jpg", width=350)

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
    <p>
    Highly experienced Azure Data Engineer, ETL Developer, Data Modeling and BI Developer with 6+ years 
    of IT experience in Database Development, ETL solutions, and building Data Warehouses, as well as 
    proven ability to produce results in a fast-paced environment with critical deadlines. Outgoing and 
    articulate communicator who gets along well with clients and coworkers at all levels. 
    I work well independently as well as collaboratively in a team environment.
    </p>
    <strong>Key Highlights:</strong>
    <ul>
    <li>
    Strong experience in SQL Server (2014/2016), T-SQL, and database design, including stored procedures, triggers, views, functions, and indexing.
    </li>
    <li>
    Developed and maintained Business Intelligence solutions using SSIS, DTS Packages, SSRS, and SSAS (OLAP Cubes, DAX, MDX).
    </li>
    <li>
    Built ETL workflows using SSIS, integrating data from Excel, CSV, Flat Files, Access, Oracle, DB2, Salesforce, and CRM by using multiple transformations provided by SSIS such as Data Conversion, Conditional Split, Bulk Insert, Derived Column, Merge, Merge Join, and Union all
    </li>
    <li>
    Migrated on-prem SQL Server databases to Azure SQL DB, Azure Data Lake, and Azure SQL Data Warehouse using Azure Data Factory.
    </li>
    <li>
    Experience in the Development of Structured Data, Data Analysis, Data Design, Documentation, and Implementation of Business Intelligence Applications.
    </li>
    <li>
    Good understanding of Azure Data Lake Store and created POCs for data movement from Flat Files and SQL Server.
    </li>
    <li>
    Created dashboards and interactive reports (drill-down, parameterized, matrix, chart) using SSRS and Power BI.
    </li>
    <li>
    Proficient in Data Warehousing concepts, dimensional modeling (Star & Snowflake schemas), and ETL pipelines.
    </li>
    <li>
    Optimized performance through query tuning and indexing; handled database access control and scheduled SSIS packages using SQL Agent.
    </li>
    <li>
    Designed and implemented CI/CD pipelines using Azure DevOps, Jenkins, and GitLab CI for automated data workflows.
    </li>
    <li>
    Experience with SQL Server MDS features such as hierarchies, granular security, versioning, and business rules.
    </li>
    <li>
    Strong communication, collaboration, and problem-solving abilities
    </li>
    <li>
    Experience working in both Agile and Waterfall environments.
    </li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Work Experience
with st.container():
    st.markdown("""
    <div class="section-container">
    <h2>💼 Work Experience</h2>

    <strong>Azure Data Engineer | Capital One, GTA - Canada (07/2024 - Currently Working)</strong> 
    <ul>
    Experienced Data Engineer with expertise in designing and executing end-to-end ETL pipelines using Azure Data Factory, Databricks, 
    SSIS, and PySpark across hybrid cloud environments (Azure, AWS). Skilled in data modeling, data lake architecture, and migrating 
    on-premise systems to Azure Synapse. Developed automated CI/CD pipelines using Git, Jenkins, and Python. Proficient in SQL Server development, 
    including SSRS dashboards, performance tuning, and advanced data transformation tasks. Built dynamic Power BI dashboards and SSIS packages integrating 
    data from multiple sources like Oracle, Teradata, and flat files. Actively collaborated in Agile environments, supporting business analysis and delivering 
    scalable data warehousing solutions.
    </ul>
    
    <strong>Data Engineer | <a href = "https://github.com/VishalGirase/experience-letter/blob/main/Cognizant_experience_letter/SeparationLetter_2037789.pdf">Cognizant</a>, India (07/2021 - 08/2023)</strong><br>
    <ul>
    Experienced Data Engineer with a strong focus on ETL development, data warehousing, and reporting solutions using SSIS, Power BI, and SQL Server. 
    Proficient in handling change requests, designing star schemas, and developing complex ETL pipelines with incremental loading, SCDs, and data scrubbing. 
    Automated data workflows using Azure DevOps, GitHub Actions, and Jenkins for CI/CD. Skilled in performance tuning, transactional replication, and database mirroring. 
    Integrated stored procedures and views into Power BI for dynamic dashboards and consistent metrics. 
    Worked extensively with Snowflake, Delta Lake, and external storage systems like S3 and Azure Blob. Managed sprints and issue resolution using Jira and Azure Boards while supporting cross-functional teams on data conversion strategies.
    </ul>

    <strong>Data Engineer | <a href = "https://github.com/VishalGirase/experience-letter/blob/main/TCS_experience_letter/1604206_Release_Letter.pdf">TCS</a>, India (06/2019 - 06/2021)</strong><br>
    <ul>
    Experienced Data Engineer with a strong background in designing OLAP models, ETL pipelines,
    and enterprise data warehouses using tools like Python, PySpark, SSIS, and PL/SQL. Skilled in data
    modeling (3NF, Star, Snowflake), SCD handling, and migrating data from Teradata to Hadoop with Hive and Spark SQL.
    Developed and deployed data-driven applications using Spring Boot, JSP, and RESTful services, with experience in data
    quality, governance, and reporting using Power BI. Proficient in working with stakeholders to define and validate ETL requirements,
    optimize performance, and ensure secure, scalable data solutions.
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

    project_tabs = st.tabs(["ADF Project", "PySpark Hands-on", "Azure Databricks Earthquake", "Azure Synpase Data pipeline"])

    with project_tabs[0]:
        st.markdown(f"""
        <div class="adf-project-bg dark-section-text">
            <h3>Azure Data Factory (ADF) Project</h3>
            <p>GitHub Repo : <a href="https://github.com/VishalGirase/ADF/tree/Dev" target="_blank" class="dark-link">ADF Project</a></p>
            <p>ReadMe : <a href="https://github.com/VishalGirase/ADF/blob/Dev/README.md" target="_blank" class="dark-link">Project Explanation</a></p>
            <p>ADF Pipeline Architecture : <a href="https://github.com/VishalGirase/ADF/blob/Dev/Images/1.png" target="_blank" class="dark-link">⛓️</a></p>        
            <p>Developed an Azure Data Factory pipeline for automated data ingestion, transformation, and load</p>
            <p>Demo : <a href = "https://youtu.be/lc4C7BPsrKs?si=qkMlQw7sHZ_FSDA4" target="_blank" class="dark-link">▶️</a></p>
            <ul>
                <li>Created Bronze | Silver | Gold Container under Gen2 data lake storage</li>
                <li>Using Lookup activity connect the SQL Server Management Studio(SSMS) tables to bronze</li>
                <li>Use for each and copy activity to snake case schema and store it to bronze container</li>
                <li>Use Databricks notebook to refine data to silver and gold gen2 containers</li>
                <li>Monitor the jobs</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with project_tabs[1]:
        st.markdown("""
        <div class="pyspark-project-bg dark-section-text">
            <h3>PySpark Hands-on</h3>
            <p>GitHub Repo: <a href="https://github.com/VishalGirase/Pyspark_Handson/tree/main/Pyspark" target="_blank" class="white-link">Pyspark Handson</a></p>
            <p>Hands-on implementation of PySpark scripts for:</p>
            <ul>
                <li>Data wrangling and cleansing</li>
                <li>Joins, aggregations, and window functions</li>
                <li>Loading and transforming large datasets</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with project_tabs[2]:
        st.markdown("""
        <div class="databricks-project-bg dark-section-text">
            <h3>Azure Databricks Automated Pipelines</h3>
            <p>GitHub Repo : <a href="https://github.com/VishalGirase/Azure_databricks_earthquake/tree/dev" target="_blank" class="white-link">Azure Databricks Earthquake Pipeline</a></p>
            <p>Workflow Architecture : <a href="https://github.com/VishalGirase/Azure_databricks_earthquake/blob/dev/Images/1.jpeg" target="_blank" class="dark-link">⛓️</a></p>
            <p>Developed an Databricks pipeline and Automated workflows on live data of earthquake:</p>
            <p>Demo : <a href = "https://youtu.be/Mp3Aq0pOLOY?si=gFCzaIByeqcCJAS-" target="_blank" class="dark-link">▶️</a></p>
            <ul>
                <li>Live EarthQuake Data Extraction from https://earthquake.usgs.gov/</li>
                <li>Clean the data and store the raw Parque files under Gen2 Data lake bronze container</li>
                <li>Defined run time parameters to fetch start date as current date and extract the data daily</li>
                <li>Created notebookes to refine data and to store parque file under silver and gold container</li>
                <li>Created the automated Workflow and schedule the pipeline daily</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with project_tabs[3]:
        st.markdown("""
        <div class="azure-synapse-project-bg dark-section-text">
            <h3>Azure Synapse Automated Pipelines</h3>
            <p>GitHub Repo : <a href="https://github.com/VishalGirase/Azure_synapse_data_warehouse_pipeline/tree/dev" target="_blank" class="white-link">Azure Synapse data warehousing Pipeline</a></p>
            <p>Synapse ARM Template that can be use to merge the code in Azure DEVOPS: <a href="https://github.com/VishalGirase/Azure_synapse_data_warehouse_pipeline/tree/workspace_publish" target="_blank" class="dark-link">ARM Template</a></p>
            <p>Synpase Pipeline Architecture : <a href="https://github.com/VishalGirase/Azure_synapse_data_warehouse_pipeline/blob/dev/images/synpase_pipeline.jpeg" target="_blank" class="dark-link">⛓️</a></p>
            <p>Developed Azure Synapse automated pipeline on gold(refined data):</p>
            <p>Demo : <a href = "https://youtu.be/lmTEzKlAeDw?si=j5Vh3nV90PaY1o1U" target="_blank" class="dark-link">▶️</a></p>
            <ul>
                <li>Data Extraction from gold gen2 container</li>
                <li>Created Pipeline using drag and drop activities. Such as copy data, lookup and foreach </li>
                <li>Within for each activity use procedure to convert tables to view</li>
                <li>Store the view in default SQL storage of Synapse</li>    
            </ul>
        </div>
        """, unsafe_allow_html=True)
