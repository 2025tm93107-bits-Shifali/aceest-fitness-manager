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
                    python3 -m venv /tmp/venv
                    /tmp/venv/bin/pip install --upgrade pip
                    /tmp/venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests (Pytest)') {
            steps {
                sh '''
                    PYTHONPATH=. /tmp/venv/bin/pytest -v --junitxml=test-reports/results.xml
                '''
            }
        }

        stage('SonarQube Code Analysis') {
            steps {
                sh '''
                    if [ ! -d "/tmp/sonar-scanner" ]; then
                        echo "Downloading SonarScanner CLI..."
                        curl -sSLo /tmp/sonar-scanner.zip https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
                        unzip -q /tmp/sonar-scanner.zip -d /tmp/
                        mv /tmp/sonar-scanner-*-linux /tmp/sonar-scanner
                    fi
                    
                    /tmp/sonar-scanner/bin/sonar-scanner \
                      -Dsonar.host.url=http://localhost:9000 \
                      -Dsonar.projectKey=aceest-fitness-manager \
                      -Dsonar.projectName="ACEest Fitness Manager" \
                      -Dsonar.sources=. \
                      -Dsonar.exclusions=.venv/**,tests/** \
                      -Dsonar.python.version=3
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