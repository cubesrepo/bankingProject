pipeline{
    agent any

    environment{
        PYTHON_VERSION = "3.11.9"
        VENV_DIR = "virtualenv"
        VENV_ACTIVATE = "${VENV_DIR}\\Scripts\\activate"
        ALLURE_REPORT = "reports/T1"
    }
    stages{
        stage("Checkout"){
            steps{
                git "https://github.com/cubesrepo/bankingProject.git"
            }
        }
        stage("Install dependencies and Setup"){
            steps{
                echo "Setting up python environment"
                bat """
                python -m venv ${VENV_DIR}
                call ${VENV_ACTIVATE} && pip install -r utilities/requirements.txt
                """
            }
        }
        stage("Run tests"){
            steps{
                echo "Running selenium tests"
                bat """
                call ${VENV_ACTIVATE} && pytest -v --alluredir=${ALLURE_REPORT} --headless
                """
            }
        }

    }
    post{
        always{
            echo "Generating Allure report"
            allure([
                includeProperties: false,
                jdk:'',
                results: [[path: "${ALLURE_REPORT}"]]
            ])
            echo "Cleaning up workspace"
            cleanWs()
        }
        success{
            echo "✅ Test passed successfully!"
        }
        failure{
            echo "❌ Tests failed!"
        }
    }

}