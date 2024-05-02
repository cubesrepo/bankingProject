pipeline{
    agent any
    stages{
        stage("Check out"){
            steps{
                git 'https://github.com/cubesrepo/bankingProject.git'
            }
        }
        stage("Install dependencies and setup"){
            steps{
                bat 'python -m venv bankingProjectVENV'
                bat 'bankingProjectVENV\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage("Run tests"){
            steps{
                bat 'bankingProjectVENV\\Scripts\\activate && pytest -v --html=report.html --headless'
            }
        }
    }
}
