def notifyGhcUrls = "https://chat.googleapis.com/v1/spaces/AAAAMALGnVM/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=ZuiOaogTrPoZp_0lGSwp-o2poPlpcfQDk9ijkzN8oz4"
def dontNotify = false

pipeline {
    agent any
  
    triggers {
       pollSCM "H/5 * * * *"
    }
    
    stages {
        stage('Build') {
            steps {
                echo "Building ..."
                script {
                    BUILD_RES = sh (script: "python3 index.py", returnStatus: true)
                    if (BUILD_RES == 2) {
                        dontNotify = true
                        currentBuild.result = "FAILURE"
                        sh "exit 1"
                    } else if (BUILD_RES == 1) {
                        currentBuild.result = "FAILURE"
                        sh "exit 1"
                    }
                }
                echo "Return status : ${BUILD_RES}"
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
    
    post {
        always {
            script {
                if (dontNotify) {
                    echo "Dont Notify"
                } else {
                    echo "Notify"
                }
                if (notifyGhcUrls != "" && !dontNotify) {
                    googlechatnotification url: "${notifyGhcUrls}",
                                           message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} notification build result ${BUILD_RES} (<${env.BUILD_URL}|Open>)"
                }
            }
        }
    }
}
