pipeline {
    agent any

    stages {

        stage('1. Checkout') {
            steps {
                // Jenkins descarga el codigo desde GitHub
                git branch: 'main',
                    url: 'https://github.com/ManuelC13/jenkins-demo'
            }
        }

        stage('2. Crear entorno virtual') {
            steps {
                // Crea una carpeta .venv aislada solo para este proyecto
                // pytest se instalara ahi adentro, no en tu PC
                sh 'python -m venv .venv'
            }
        }

        stage('3. Instalar dependencias') {
            steps {
                // Instala pytest DENTRO del entorno virtual
                sh '.venv/bin/pip install pytest'
            }
        }

        stage('4. Ejecutar pruebas') {
            steps {
                // Ejecuta las pruebas usando el pytest del entorno virtual
                sh '.venv/bin/pytest test_calculadora.py -v'
            }
        }

    }

    post {
        success { echo 'Todas las pruebas pasaron. Pipeline exitoso!' }
        failure { echo 'Alguna prueba fallo. Revisa el log.' }
    }
}
