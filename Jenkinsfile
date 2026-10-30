pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
    }

    stages {

        stage('Checkout from GitHub') {
            steps {
                checkout scm
            }
        }

        stage('Pull lightweight Python image') {
            steps {
                bat 'docker pull python:3.12-slim'
            }
        }

        stage('Build Docker image') {
            steps {
                bat 'docker build -t hello-mlops:latest .'
            }
        }

        stage('Run hello.py') {
            steps {
                bat 'docker run --rm hello-mlops:latest'
            }
        }

        stage('Run one pytest test') {
            steps {
                bat 'docker run --rm hello-mlops:latest python -m pytest -v test_hello.py'
            }
        }

        stage('Generate Evidently drift report') {
            steps {
                bat 'docker run --rm -v "%CD%:/app" hello-mlops:latest python monitor_data.py'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'data_drift_report.html',
                             allowEmptyArchive: true
        }
    }
}