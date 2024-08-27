pipeline {
  agent any

  stages {
    stage('Make CI/CV/CD output directory') {
      steps {
        script {
          // Check if the file exists
          sh 'rm -rf output'
          sh 'mkdir output'
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
    stage('Generate ROS Build Files') {
      when {
        expression { env.MOBILITY_REQ_EXISTS == "true" }
      }
      steps {
        script {
          def scriptOutput = sh(script: 'python3 JenkinsScripts/generate_ros_build_files.py', returnStdout: true).trim()
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
          if (fileExists('output/integrationResult.txt') && fileExists('output/integration.launch.py') && fileExists('output/setup.py')) {
              // Print the file contents using cat
              sh 'cat output/integrationResult.txt'
              sh 'cat output/integration.launch.py'
              sh 'cat output/setup.py'
          } else {
              echo "Output files do not exist."
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
