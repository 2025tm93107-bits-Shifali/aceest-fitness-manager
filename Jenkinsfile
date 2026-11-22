pipeline {
  agent any

  environment {
    DOCKER_HUB_REPO = 'shifali23/aceest-fitness'
    IMAGE_TAG = "${BUILD_NUMBER}"
    SONAR_PROJECT_KEY = 'aceest-fitness-manager'
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

    stage('Code Quality (SonarQube)') {
      steps {
        sh '''
          /tmp/ci-venv/bin/pip install -q flake8 || true
          /tmp/ci-venv/bin/flake8 app tests --max-line-length=120 || true
        '''
        withCredentials([string(credentialsId: 'sonar-token', variable: 'SONAR_TOKEN')]) {
          sh '''
            docker run --rm --network host \
              -e SONAR_HOST_URL="http://localhost:9000" \
              -e SONAR_TOKEN="${SONAR_TOKEN}" \
              -v "$(pwd):/usr/src" \
              sonarsource/sonar-scanner-cli \
              -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
              -Dsonar.sources=. \
              -Dsonar.exclusions="venv/**,.venv/**,.pytest_cache/**,**/__pycache__/**"
          '''
        }
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
  }
}
