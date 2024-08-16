pipeline {
  agent any
  stages {
    // stage('Install Python3') {
    //   steps {
    //     sh '''
    //         apt-get update
    //         apt-get install -y python3 python3-pip
    //         sh 'python3 --version'
    //     '''
    //   }
    // }
    stage('Check Python Version') {
      steps {
        sh 'python --version'
      }
    }
    stage('integration') {
      steps {
        echo 'integration'
        sh 'python JenkinsScripts/integration_script.py'
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