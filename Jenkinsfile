pipeline {
    agent any
    stages {
        stage('Preparar Entorno') {
            steps {
                // Crear entorno virtual e instalar dependencias
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Ejecutar Pruebas') {
            steps {
                // Ejecutar pruebas
                sh '. venv/bin/activate && behave --format=pretty'
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
            sh 'rm -rf venv'
        }
    }
}
