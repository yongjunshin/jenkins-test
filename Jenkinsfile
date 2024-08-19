pipeline {
  agent any

  stages {
    stage('Delete previous CI/CV/CD results') {
      steps {
        script {
          // Check if the file exists
          if (fileExists('integrationResult.txt')) {
            // Delete the file using the shell command
            sh 'rm -f integrationResult.txt'
            echo "File integrationResult.txt has been deleted."
          } else {
            echo "File integrationResult.txt does not exist."
          }
        }
      }
    }
    stage('CI/CV/CD') {
      steps {
        echo "Performing CI/CV/CD ..."
        script {
          def scriptOutput = sh(script: 'python3 JenkinsScripts/integration_script.py', returnStdout: true).trim()
          env.MOBILITY_REQ_EXISTS = scriptOutput.contains("PROCEED") ? "true" : "false"
        }
      }
    }
    stage('Build') {
      when {
        expression { env.MOBILITY_REQ_EXISTS == "true" }
      }
      steps {
        echo "Performing Build ..."
        script {
          // Check if the file exists
          if (fileExists('integrationResult.txt')) {
              // Print the file contents using cat
              sh 'cat -v integrationResult.txt'
          } else {
              echo "File integrationResult.txt does not exist."
          }
          echo "Run build script."
        }
      }
    }
    stage('Alternative Path') {
      when {
        expression { env.MOBILITY_REQ_EXISTS == "false" }
      }
      steps {
        echo "mobilityReq.txt not found. Taking alternative path."
        // Add any steps you want to perform when mobilityReq.txt doesn't exist
      }
    }
  }
  post {
    always {
      echo "Pipeline completed."
    }
  }
}