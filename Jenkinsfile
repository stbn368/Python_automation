pipeline {
    agent any
    stages {
        stage('Preparar Entorno') {
            steps {
                // Verificar la versión de Python
                bat 'python --version'
                // Crear entorno virtual e instalar dependencias
                bat 'python -m venv venv'
                bat '''
                    call venv\\Scripts\\activate ^
                    && venv\\Scripts\\python.exe -m pip install --upgrade pip setuptools wheel
                '''
                bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                // Activar entorno virtual y ejecutar pruebas con reporte Allure
                bat 'call venv\\Scripts\\activate && behave -f allure_behave.formatter:AllureFormatter -o allure-results'
            }
        }
        stage('Publicar Resultados de Allure') {
            steps {
                // Publicar los resultados de Allure en Jenkins
                allure([
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
    post {
        always {
            // Limpiar el entorno virtual
            bat 'rmdir /S /Q venv'
        }
    }
}
