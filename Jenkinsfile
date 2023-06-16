pipeline {
    agent any
  
    triggers {
       pollSCM "H/5 * * * *"
    }
    
    stages {
        stage('Build') {
            steps {
                echo "Building ..."
                sh "python3 index.py"
            }
        }
        
        stage('Testing') {
            steps {
                echo "Testing ..."
                sh '''
                echo "Hello starting to test..."
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                echo "Deploying..."
                sh '''
                echo "Starting to deploy the build..."
                '''
            }
        }
    }
}
