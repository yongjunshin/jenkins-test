pipeline {
  agent any
  stages {
    stage('Check Environment') {
      steps {
        script {
            echo 'Listing files in the current directory:'
            sh 'ls -la'
            
            echo 'Checking Python 3 version:'
            sh 'python3 --version'
        }
      }
    }
    stage('Check Python Version') {
      steps {
        sh 'python3 --version'
      }
    }
    stage('integration') {
      steps {
        echo 'integration'
        sh 'python3 JenkinsScripts/integration_script.py'
      }
    }
    stage('validation') {
      steps {
        echo 'validation'
      }
    }
    stage('deployment') {
      steps {
        echo 'deployment'
      }
    }
    stage('clean-up') {
      steps {
        echo 'bye'
      }
    }
  }
}