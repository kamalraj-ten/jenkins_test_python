pipeline {
    agent any
  
    triggers {
       pollSCM "*/5 * * * *"
    }
    
    stages {
        stage('Build') {
            steps {
                echo "Building ..."
                sh '''
                echo "Hello this is build..."
                '''   
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
