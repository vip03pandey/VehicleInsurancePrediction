Graphene-Based THz Biosensors ML Pipeline
Overview
This project implements a machine learning pipeline for processing and analyzing data from graphene-based nanoscale THz biosensors, aimed at detecting biomolecules with high sensitivity. The pipeline includes data ingestion from MongoDB, data validation, transformation, model training, evaluation, and deployment on AWS EC2 using a CI/CD workflow with GitHub Actions. The project demonstrates expertise in MLOps, cloud infrastructure, and advanced biosensing applications.
Project Structure

src/: Core source code for the pipeline components (data ingestion, validation, transformation, model training, evaluation, and prediction).
notebook/: Jupyter notebooks for EDA, feature engineering, and MongoDB data push (mongoDB_demo.ipynb).
static/ & template/: Frontend assets for the Flask app.
requirements.txt: Project dependencies.
Dockerfile & .dockerignore: For containerization and deployment.
.github/workflows/aws.yml: GitHub Actions workflow for CI/CD.
.gitignore: Ignores artifacts and sensitive directories.
app.py: Flask app for prediction and training routes.
demo.py: Script to test logging, exceptions, and pipeline execution.

Setup Instructions
1. Project Template Creation

Execute template.py to generate the project structure:python template.py



2. Local Package Configuration

setup.py and pyproject.toml are configured to import local packages. Refer to crashcourse.txt for details on their structure.
Example configurations:
setup.py: Defines package metadata and dependencies.
pyproject.toml: Specifies build system and project metadata.



3. Virtual Environment Setup

Create and activate a Conda environment, then install dependencies:conda create -n vehicle python=3.10 -y
conda activate vehicle
pip install -r requirements.txt


Verify installed packages:pip list


Required modules (e.g., pymongo, pandas, scikit-learn) are added to requirements.txt.

4. MongoDB Setup (Atlas)

Sign up for MongoDB Atlas and create a new project.
Create an M0 cluster with default settings.
Set up a database user with a username and password.
Configure network access to allow connections from anywhere (0.0.0.0/0).
Obtain the connection string (Driver: Python, Version: 3.6 or later) and replace the password:mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority


Set the connection string as an environment variable:export MONGODB_URL="mongodb+srv://<username>:<password>..."
echo $MONGODB_URL

On Windows (PowerShell):$env:MONGODB_URL="mongodb+srv://<username>:<password>..."
echo $env:MONGODB_URL


Create a notebook/ directory, add datasets, and push data to MongoDB using mongoDB_demo.ipynb (select kernel: vehicle).
Verify data in MongoDB Atlas under "Database > Browse Collections."

5. Logging and Exception Handling

Logger: Implemented in logger.py and tested in demo.py for structured logging.
Exception Handling: Custom exceptions defined in exception.py and tested in demo.py.

6. EDA and Feature Engineering

Performed in notebook/eda_feature_engg.ipynb to preprocess THz biosensor data (e.g., refractive index changes, resonance shifts).

Pipeline Components
7. Data Ingestion

Constants: Define variables in constants/__init__.py (e.g., database names, collection names).
MongoDB Connection: Implement connection logic in configuration/mongo_db_connections.py.
Data Access: Fetch data from MongoDB and convert to DataFrame in data_access/proj1_data.py.
Entity Classes:
entity/config_entity.py: Add DataIngestionConfig class.
entity/artifact_entity.py: Add DataIngestionArtifact class.


Component: Implement ingestion logic in components/data_ingestion.py.
Pipeline: Integrate into training_pipeline.py.
Run demo.py after setting MONGODB_URL.

8. Data Validation

Utils: Add helper functions in utils/main_utils.py.
Schema: Define dataset schema in config/schema.yaml (e.g., column types, ranges for THz sensor data).
Follow the same workflow as Data Ingestion for component setup.

9. Data Transformation

Add estimator.py to entity/ for transformation logic.
Implement in components/data_transformation.py.

10. Model Trainer

Extend estimator.py with model training classes.
Implement in components/model_trainer.py.

AWS Setup for Model Evaluation and Deployment
11. AWS Configuration

IAM User: Create a user (firstproj) with AdministratorAccess.
Access Keys: Generate and download access keys, then set as environment variables:export AWS_ACCESS_KEY_ID="..."
export AWS_SECRET_ACCESS_KEY="..."


Constants: Add keys and region (us-east-1) to constants/__init__.py:MODEL_EVALUATION_CHANGED_THRESHOLD_SCORE = 0.02
MODEL_BUCKET_NAME = "my-model-mlopsproj"
MODEL_PUSHER_S3_KEY = "model-registry"


S3 Bucket: Create a bucket (my-model-mlopsproj) in us-east-1, uncheck "Block all public access."
AWS Connection: Implement S3 interaction in configuration/aws_connection.py.
S3 Estimator: Add model pull/push logic in entity/s3_estimator.py and aws_storage/.

12. Model Evaluation and Pusher

Implement components/model_evaluation.py and components/model_pusher.py.

13. Prediction Pipeline

Set up app.py for Flask-based prediction and training routes.
Add static/ and template/ directories for frontend assets.

CI/CD Pipeline
14. Docker Setup

Create Dockerfile and .dockerignore for containerization.

15. GitHub Actions Workflow

Add CI/CD workflow in .github/workflows/aws.yml.
IAM User for CI/CD: Create a user (usvisa-user) with access keys.
ECR Repository: Create a repository (vehicleproj) in AWS ECR and note the URI.
EC2 Instance: Launch an Ubuntu server (vehicledata-machine, T2 Medium, 30GB storage) with HTTP/HTTPS traffic enabled.
Docker on EC2:sudo apt-get update -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker


Self-Hosted Runner:
Add a runner in GitHub (OS: Linux, name: self-hosted).
Run setup commands on EC2 and start the runner (./run.sh).


GitHub Secrets:
Add AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_DEFAULT_REGION, and ECR_REPO.



16. Deploy and Access

Trigger the CI/CD pipeline with a commit.
Open port 5080 on EC2:
Security Groups > Edit Inbound Rules > Add Custom TCP (Port 5080, Source: 0.0.0.0/0).


Access the app at <EC2-Public-IP>:5080.
Train models at /training route.

Key Features

Scalable Pipeline: Modular components for data ingestion, validation, transformation, and model training.
Cloud Integration: AWS S3 for model storage, EC2 for deployment, and ECR for Docker images.
CI/CD Automation: GitHub Actions with self-hosted runners for seamless deployment.
Data Management: MongoDB Atlas for storing and retrieving THz biosensor data.
Robust Logging: Custom logging and exception handling for debugging.

Technologies Used

Python, Flask, Pandas, Scikit-learn, PyMongo
MongoDB Atlas
AWS (S3, EC2, ECR, IAM)
Docker, GitHub Actions
Jupyter Notebooks

Future Improvements

Optimize model performance using hyperparameter tuning.
Add real-time monitoring for the CI/CD pipeline.
Integrate advanced graphene sensor data preprocessing techniques.

Contact
For inquiries, please reach out to [Your Name] at [your-email@example.com].
