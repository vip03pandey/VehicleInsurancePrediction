
🚗 Vehicle Insurance Prediction - End-to-End MLOps Project

This project focuses on building an end-to-end Vehicle Insurance Prediction System using modern Machine Learning practices and MLOps tools. It covers everything from data ingestion to deployment using CI/CD, Docker, AWS, and MongoDB Atlas.

---

🔧 Problem Statement

Insurance companies want to predict whether a customer will opt for vehicle insurance, based on their past behavior and demographic profile. This helps in targeted marketing and resource optimization.


📂 Project Structure
vehicle-insurance-prediction/
│
├── .github/workflows/           GitHub Actions for CI/CD
├── artifact/                    Stores intermediate artifacts (ignored in Git)
├── docker/                      Docker and Dockerfile
├── notebook/                    Jupyter Notebooks (EDA, MongoDB push)
├── src/                         Core application code
│   ├── components/              Pipeline components (Ingestion, Validation, etc.)
│   ├── configuration/           MongoDB and AWS configurations
│   ├── data_access/             Data access layers for MongoDB
│   ├── entity/                  Config and Artifact entities
│   ├── utils/                   Utility scripts
│   ├── exception.py             Custom Exception Class
│   ├── logger.py                Custom Logger Class
│   └── app.py                   Flask application
│
├── static/, templates/          For Flask web app interface
├── requirements.txt             Required Python packages
├── pyproject.toml               Package configuration (PEP 518)
├── setup.py                     For installing as local package
├── README.md                    This file
└── .dockerignore, .gitignore
```

---

⚙️ Major Features

 ✅ 1. Data Pipeline

 Data Ingestion from MongoDB Atlas
 Data Validation using YAML scheme
 Data Transformation with custom transformers
 Model Training with automated evaluation
 Model saved/pushed to AWS S3 buck

 ✅ 2. Prediction Pipeline

 Flask-based web UI to input user details
 Trained model is loaded to generate predictions
 Deployed to AWS EC2 (port 5080)

 ✅ 3. CI/CD with GitHub Actions & AWS

 Docker image built & pushed to AWS ECR
 Deployed using self-hosted GitHub runner on EC2
 EC2 instance configured with Docker and SSH

---

🗃️ MongoDB Atlas Integration

 Secure cloud storage of dataset
 IP whitelisting and user/password auth
 Connection string handled via environment variables

--- ☁️ AWS Integration

S3: Used to store trained models
EC2: Hosts the deployed Flask app
ECR: Docker image repository
IAM: Used for secure access via access keys

---

🔄 CI/CD Workflow

1. Code is pushed to GitHub
2. GitHub Actions triggers:

    Docker image is built
    Pushed to AWS ECR
    SSH EC2 instance via self-hosted runner
    Pulls latest Docker image and runs the app

---

🧪 Local Setup Instructions

```bash
1. Clone the repo
git clone https://github.com/yourusername/VehicleInsurancePrediction.git

2. Create conda env
conda create -n vehicle python=3.10 -y
conda activate vehicle

3. Install dependencies
pip install -r requirements.txt

4. Set up MongoDB URL (bash)
export MONGODB_URL="mongodb+srv://<username>:<password>@cluster.mongodb.net/?..."

5. Run app locally
python src/app.py
```

---

🌐 Hosted App

Once deployed:

```
http://<EC2-public-ip>:5080/
```

---

📊 Sample Inputs (For Prediction)

| Feature        | Type        | Example  |
| -------------- | ----------- | -------- |
| Age            | Integer     | 35       |
| Gender         | Categorical | Male     |
| Annual Income  | Float       | 60000    |
| Vehicle Age    | Categorical | < 1 Year |
| Vehicle Damage | Binary      | Yes      |

---

🚀 Future Enhancements

 Integration with MLflow for experiment tracking
 Real-time monitoring using Prometheus + Grafana
 User authentication (JWT-based)
 Multiple model comparison with AutoML

---


