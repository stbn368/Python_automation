pipeline {
    agent any
    stages {
        stage('Preparar Entorno') {
            steps {
                // Crear entorno virtual e instalar dependencias
                bat 'python -m venv venv'
                bat 'call venv\\Scripts\\activate && pip install --upgrade pip setuptools'
                bat 'call venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                // Activar entorno virtual y ejecutar pruebas
                bat 'call venv\\Scripts\\activate && behave --format=pretty'
            }
        }
        stage('Publicar Resultados') {
            steps {
                // Archivar capturas de pantalla y reportes
                archiveArtifacts artifacts: 'screenshots/*.png', fingerprint: true
                publishHTML([allowMissing: false,
                             alwaysLinkToLastBuild: true,
                             keepAll: true,
                             reportDir: 'reports',
                             reportFiles: 'report.html',
                             reportName: 'Reporte de Pruebas'])
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
