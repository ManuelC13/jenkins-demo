pipeline {
    agent any

    stages {

        stage('1. Crear entorno virtual') {
            steps {
                // Crea una carpeta .venv aislada solo para este proyecto
                // pytest se instalara ahi adentro, no en tu PC
                sh 'python3 -m venv .venv'
            }
        }

        stage('2. Instalar dependencias') {
            steps {
                // Instala pytest DENTRO del entorno virtual
                sh '.venv/bin/pip install pytest'
            }
        }

        stage('3. Ejecutar pruebas') {
            steps {
                // Ejecuta las pruebas usando el pytest del entorno virtual
                sh '.venv/bin/pytest tests/test_calculadora.py -v'
            }
        }

        stage('4. Desplegar a producción') {
            steps {
                // Solo se ejecuta si todas las pruebas pasaron
                sh 'echo "Desplegando a producción..."'
            }
        }

    }

    post {
        success { echo 'Todas las pruebas pasaron. Pipeline exitoso!' }
        failure { echo 'Alguna prueba fallo. Revisa el log.' }
    }
}
