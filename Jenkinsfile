pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                // Add your build steps here
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                // Add your test steps here
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                // Add your deployment steps here
            }
        }
    }
}
