pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t checkout-api:jenkins .'
            }
        }
    }
}
