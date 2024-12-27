pipeline {
    agent any
    stages {
        stage('Preparar Entorno') {
            steps {
                // Configurar entorno virtual e instalar dependencias
                bat 'python --version'
                bat 'python -m venv venv'
                bat '''
                    call venv\\Scripts\\activate ^
                    && venv\\Scripts\\python.exe -m pip install --upgrade pip setuptools wheel ^
                    && pip install -r requirements.txt
                '''
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                // Ejecutar pruebas con Allure
                bat '''
                    call venv\\Scripts\\activate ^
                    && behave -f allure_behave.formatter:AllureFormatter -o allure-results
                '''
            }
        }
        stage('Publicar Resultados') {
            steps {
                // Generar el reporte de Allure
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
