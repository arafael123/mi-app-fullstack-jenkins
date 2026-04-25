pipeline {
    agent any

    stages {

        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/arafael123/mi-app-fullstack-jenkins.git'
            }
        }

        stage('Instalar dependencias') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Pruebas') {
            steps {
                bat 'pytest'
            }
        }

        stage('Run App') {
            steps {
                bat 'python app.py'
            }
        }
    }
}