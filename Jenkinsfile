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
    stage('Integration') {
      steps {
        script {
          def scriptOutput = sh(script: 'python3 JenkinsScripts/integration_script.py', returnStdout: true).trim()
          env.MOBILITY_REQ_EXISTS = scriptOutput.contains("PROCEED") ? "true" : "false"
        }
      }
    }
    stage('Validation') {
      when {
        expression { env.MOBILITY_REQ_EXISTS == "true" }
      }
      steps {
        echo "Performing validation..."
        // Add your validation steps here
        script {
          // Check if the file exists
          if (fileExists('mobilityReq.txt')) {
              // Print the file contents using cat
              sh 'cat mobilityReq.txt'
          } else {
              echo "File mobilityReq.txt does not exist."
          }
        }
      }
    }

    stage('Deployment') {
      when {
        expression { env.MOBILITY_REQ_EXISTS == "true" }
      }
      steps {
        echo "Performing deployment..."
        // Add your deployment steps here
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