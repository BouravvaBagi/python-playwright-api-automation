pipeline {
    agent any

    environment {
        PLAYWRIGHT_BROWSERS_PATH = 'C:\\pw-browsers'
        REQRES_API_KEY = credentials('reqres-api-key')
    }

    stages {
        stage('Check Environment') {
            steps {
                dir('C:\\aasignment') {
                    bat '''
                        echo Checking Python...
                        .venv\\Scripts\\python.exe --version

                        echo Checking Java...
                        java -version

                        echo Checking Allure...
                        "C:\\Users\\abc\\Downloads\\allure-2.46.1\\allure-2.46.1\\bin\\allure.bat" --version
                    '''
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                dir('C:\\aasignment') {
                    bat '''
                        .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                        .venv\\Scripts\\python.exe -m pip install pytest-html allure-pytest
                    '''
                }
            }
        }

        stage('Check API Credential') {
            steps {
                dir('C:\\aasignment') {
                    bat '''
                        if defined REQRES_API_KEY (
                            echo API credential is configured.
                        ) else (
                            echo API credential is missing.
                            exit /b 1
                        )
                    '''
                }
            }
        }

        stage('Run Automation Tests') {
            steps {
                dir('C:\\aasignment') {
                    bat '''
                        if not exist reports mkdir reports
                        if not exist allure-results mkdir allure-results

                        .venv\\Scripts\\python.exe -m pytest tests -v --html=reports/report.html --self-contained-html --alluredir=allure-results
                    '''
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                dir('C:\\aasignment') {
                    bat '''
                        "C:\\Users\\abc\\Downloads\\allure-2.46.1\\allure-2.46.1\\bin\\allure.bat" generate allure-results --clean -o allure-report
                    '''
                }
            }
        }
    }

    post {
        always {
            dir('C:\\aasignment') {
                archiveArtifacts(
                    artifacts: 'reports/report.html,allure-results/**',
                    allowEmptyArchive: true
                )

                publishHTML(target: [
                    reportName: 'Pytest HTML Report',
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: true
                ])

                archiveArtifacts(
                    artifacts: 'allure-report/**',
                    allowEmptyArchive: true
                )

                allure(
                    results: [[path: 'allure-results']],
                    reportBuildPolicy: 'ALWAYS'
                )
            }
        }
    }
}