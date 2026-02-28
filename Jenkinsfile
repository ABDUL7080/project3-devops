pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t project3-app .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop project3-container || true'
                sh 'docker rm project3-container || true'
            }
        }

        stage('Deploy New Container') {
            steps {
                sh 'docker run -d -p 8081:8080 --name project3-container project3-app'
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment Successful'
        }
        failure {
            echo '❌ Deployment Failed'
        }
    }
}