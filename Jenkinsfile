pipeline {
  agent any
  stages {
    stage('init') {
      steps {
        sh 'echo "sms-provider starting..."'
      }
    }
    stage('pull source') {
      steps {
        sh 'echo "pull source from github"'
      }
    }
    stage('configuration') {
      steps {
        sh 'echo "change config to adjust environment"'
      }
    }
    stage('deploy') {
      steps {
        sh 'echo "launching module!"'
      }
    }
  }
}