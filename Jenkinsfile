pipeline {
  agent any

  environment {
    IMAGE = 'yourdockerhubusername/contact-list'
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        bat 'docker build -t %IMAGE%:latest .'
      }
    }

    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
          bat '''
          echo %PASS% | docker login -u %USER% --password-stdin
          docker push %IMAGE%:latest
          '''
        }
      }
    }

    stage('Deploy to Kubernetes') {
      steps {
        withCredentials([file(credentialsId: 'kubeconfig-cred', variable: 'KUBECONFIG_FILE')]) {
          bat '''
          set KUBECONFIG=%KUBECONFIG_FILE%
          kubectl apply -f deployment.yaml
          kubectl apply -f service.yaml
          '''
        }
      }
    }
  }

  post {
    success {
      echo "✅ Deployment Successful!"
    }
    failure {
      echo "❌ Build Failed!"
    }
  }
}
