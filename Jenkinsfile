pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run PyTest') {
            steps {
                bat 'python -m pytest -v -s --junitxml=pytest-results.xml'
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true,
                  testResults: 'pytest-results.xml'
        }
    }
}
