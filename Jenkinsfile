pipeline {
    agent any

    environment {
        IMAGE_NAME = "project3-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
        CONTAINER_NAME = "project3-container"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Stop Old Container') {
            steps {
                sh "docker stop ${CONTAINER_NAME} || true"
                sh "docker rm ${CONTAINER_NAME} || true"
            }
        }

        stage('Deploy New Container') {
            steps {
                sh """
                docker run -d \
                -p 8001:8000 \
                --name ${CONTAINER_NAME} \
                -e APP_VERSION=${IMAGE_TAG} \
                ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }

        stage('Verify Deployment') {
            steps {
                sh "sleep 5"
                sh "curl http://localhost:8001/info"
            }
        }
    }

    post {
        success {
            echo "✅ Deployment Successful"
        }
        failure {
            echo "❌ Deployment Failed"
        }
    }
}