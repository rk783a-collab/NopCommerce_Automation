
pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        timestamps()
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '''
                    if exist .venv rmdir /s /q .venv

                    python -m venv .venv
                    if errorlevel 1 exit /b 1

                    .venv\\Scripts\\python.exe -m pip install --upgrade pip
                    if errorlevel 1 exit /b 1

                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                    if errorlevel 1 exit /b 1

                    .venv\\Scripts\\python.exe -m playwright install chromium
                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('Run Playwright Tests') {
            steps {
                bat '''
                    .venv\\Scripts\\python.exe -m pytest -v -s tests -m smoke --junitxml=junit.xml
                    exit /b %ERRORLEVEL%
                '''
            }
        }
    }

    post {
        always {
            junit testResults: 'junit.xml', allowEmptyResults: true
        }
    }
}
