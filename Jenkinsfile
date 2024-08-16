pipeline {
  agent any
  stages {
    stage('Debug') {
      steps {
        sh 'pwd'
        sh 'ls -R'
      }
    } 
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
    stage('Integration') {
      steps {
        script {
          def scriptOutput = sh(script: 'python3 JenkinsScripts/integration_script.py', returnStdout: true).trim()

          if (scriptOutput.contains("TERMINATE")) {
              error("mobilityReq.txt not found. Pipeline terminated.")
          }
        }
      }
    }
    stage('validation') {
      when {
          expression { 
              return fileExists('integrationResult.txt')
          }
      }
      steps {
          echo "Performing validation..."
          // Add your validation steps here
      }
    }
    stage('deployment') {
      when {
          expression { 
              return fileExists('integrationResult.txt')
          }
      }
      steps {
          echo "Performing deployment..."
          // Add your deployment steps here
      }
    }
  }
}