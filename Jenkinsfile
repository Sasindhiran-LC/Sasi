
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
                bat '"C:\\Users\\Admin\\AppData\\Local\\Python\\bin\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run PyTest') {
            steps {
                bat '"C:\\Users\\Admin\\AppData\\Local\\Python\\bin\\python.exe" -m pytest -v -s --junitxml=pytest-results.xml'
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
