pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code'
                checkout scm
            }
        }
        stage('Build') {
            steps {
                echo 'Installing Python dependencies'
                sh '''
                    python3 -m venv /tmp/venv
                    /tmp/venv/bin/pip install --upgrade pip
                    /tmp/venv/bin/pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Running automated tests'
                sh '''
                    PYTHONPATH=. /tmp/venv/bin/pytest -v --junitxml=test-reports/results.xml
                '''
            }
        }
    }
    post {
        success {
            echo 'Basic CI/CD pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}