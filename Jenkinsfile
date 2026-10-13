pipeline {
    agent any

    environment {
        PYTHONPATH = '.'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/2025tm93107-bits-Shifali/aceest-fitness-manager.git'
            }
        }

        stage('Setup Environment & Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests (Pytest)') {
            steps {
                sh '''
                    . .venv/bin/activate
                    PYTHONPATH=. pytest -v --junitxml=test-reports/results.xml
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}