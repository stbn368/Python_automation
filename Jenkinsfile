pipeline {
    agent any
    stages {
        stage('Preparar Entorno') {
            steps {
                script {
                    bat 'python -m venv venv'
                    bat 'call venv\\Scripts\\activate && pip install --upgrade pip setuptools'
                    bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                script {
                    bat 'call venv\\Scripts\\activate && behave --format=pretty'
                }
            }
        }
        stage('Publicar Resultados') {
            steps {
                // Publicar resultados aquí
            }
        }
    }
    post {
        always {
            script {
                bat 'rmdir /S /Q venv'
            }
        }
    }
}
