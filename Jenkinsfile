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
                    python3 -m pip install --upgrade pip --user
                    python3 -m pip install -r requirements.txt --user
                '''
            }
        }

        stage('Run Unit Tests (Pytest)') {
            steps {
                sh '''
                    PYTHONPATH=. python3 -m pytest -v --junitxml=test-reports/results.xml
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