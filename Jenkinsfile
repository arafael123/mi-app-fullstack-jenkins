pipeline {
    agent any

    stages {

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
    }
}