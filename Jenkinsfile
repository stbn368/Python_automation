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
                // Activar entorno virtual y ejecutar pruebas con reporte
                bat 'call venv\\Scripts\\activate && behave --format=html --outfile=reports/report.html'
            }
        }
        stage('Publicar Resultados') {
            steps {
                script {
                    // Verificar si existen capturas de pantalla antes de archivarlas
                    def screenshotsExist = fileExists('screenshots/*.png')
                    if (screenshotsExist) {
                        archiveArtifacts artifacts: 'screenshots/*.png', fingerprint: true
                    } else {
                        echo 'No se encontraron capturas de pantalla para archivar.'
                    }
                }
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Reporte de Pruebas'
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

