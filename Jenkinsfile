pipeline {
    agent any

    environment {
        IMAGE_NAME = "project3-app"
        IMAGE_TAG = "${BUILD_NUMBER}"
        CONTAINER_NAME = "project3-container"
    }

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/YOUR_USERNAME/YOUR_REPO.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Stop Old Container') {
            steps {
                bat "docker stop %CONTAINER_NAME% || exit 0"
                bat "docker rm %CONTAINER_NAME% || exit 0"
            }
        }

        stage('Deploy New Container') {
            steps {
                bat """
                docker run -d ^
                -p 8001:8000 ^
                --name %CONTAINER_NAME% ^
                -e APP_VERSION=%IMAGE_TAG% ^
                %IMAGE_NAME%:%IMAGE_TAG%
                """
            }
        }

        stage('Verify Deployment') {
            steps {
                bat "timeout /t 5"
                bat "curl http://localhost:8001/info"
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