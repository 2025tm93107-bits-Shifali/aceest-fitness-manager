pipeline {
    agent any
    triggers {
        pollSCM('H/2 * * * *')
    }
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
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Running automated tests'
                sh '''
                    .venv/bin/python -m pytest -q --junitxml=test-reports/results.xml
                '''
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
                    sh '''
                        echo "Running SonarQube analysis..."
                        if ! command -v sonar-scanner &> /dev/null; then
                            wget -q https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-5.0.1.3006-linux.zip
                            unzip -q sonar-scanner-cli-5.0.1.3006-linux.zip
                            export PATH=$PWD/sonar-scanner-5.0.1.3006-linux/bin:$PATH
                        fi
                        sonar-scanner \
                          -Dsonar.projectKey=ACEest-Fitness-Manager \
                          -Dsonar.projectName="ACEest Fitness Manager" \
                          -Dsonar.sources=. \
                          -Dsonar.exclusions=.venv/**,tests/** \
                          -Dsonar.host.url=http://localhost:9000 \
                          -Dsonar.token=$SONAR_TOKEN
                    '''
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying application'
                sh '''
                    mkdir -p /tmp/aceest-fitness-manager
                    cp -r app.py templates static requirements.txt /tmp/aceest-fitness-manager/
                    cd /tmp/aceest-fitness-manager
                    python3 -m venv .venv
                    .venv/bin/pip install -r requirements.txt
                    if [ -f app.pid ]; then
                        kill $(cat app.pid) 2>/dev/null || true
                    fi
                    nohup .venv/bin/python app.py > app.log 2>&1 &
                    echo $! > app.pid
                '''
            }
        }
    }
    post {
        success {
            echo 'CI/CD pipeline completed successfully with SonarQube analysis'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}