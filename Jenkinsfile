pipeline {
    agent any

    stages {

        stage('Clonar repositorio') {
            steps {
                git 'https://github.com/TU-USUARIO/mi-app-fullstack.git'
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