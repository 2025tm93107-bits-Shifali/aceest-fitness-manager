pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'shifali23/aceest-fitness'
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Unit Test with Pytest') {
            steps {
                sh '''
                    python3 -m venv /tmp/ci-venv
                    /tmp/ci-venv/bin/pip install --upgrade pip
                    /tmp/ci-venv/bin/pip install -r requirements.txt
                    PYTHONPATH=. /tmp/ci-venv/bin/pytest -v
                '''
            }
        }

        stage('Build & Push Docker Image') {
            steps {
                sh '''
                    docker build -t ${DOCKER_HUB_REPO}:v${IMAGE_TAG} -t ${DOCKER_HUB_REPO}:latest .
                    docker push ${DOCKER_HUB_REPO}:v${IMAGE_TAG}
                    docker push ${DOCKER_HUB_REPO}:latest
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl apply -f k8s/
                    kubectl get pods,svc
                '''
            }
        }
    }
}
