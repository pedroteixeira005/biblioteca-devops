pipeline {
    agent any
 
    options {
        timestamps()
    }
 
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
 
        stage('Verificar ambiente') {
            steps {
                sh 'git --version'
                sh 'python3 --version'
            }
        }
 
        stage('Instalar dependências') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install pytest
                '''
            }
        }
 
        stage('Testes') {
            steps {
                sh '.venv/bin/python -m pytest -v'
            }
        }
    }
 
    post {
        success {
            echo 'Pipeline concluído com sucesso!'
        }
        failure {
            echo 'Falha no pipeline. Consulte os logs.'
        }
        always {
            echo 'Execução finalizada.'
        }
    }
}
	
	stage('Build') {
    steps {
        sh 'python3 -m compileall -q src tests'
    }
}
