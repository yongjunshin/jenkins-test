pipeline {
  agent any

  stages {
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
              // Read the file contents
              def fileContents = readFile('mobilityReq.txt')
              // Echo the file contents
              echo "Contents of mobilityReq.txt:"
              echo fileContents
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