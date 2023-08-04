import hudson.model.Result as Result

def notifyGhcUrls = "https://chat.googleapis.com/v1/spaces/AAAAMALGnVM/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=ZuiOaogTrPoZp_0lGSwp-o2poPlpcfQDk9ijkzN8oz4"
def dontNotify = false
def notifyEmailAddresses = "kamalrajdhanakodi@gmail.com"
def previousBuildResult = getPreviousBuildResult()

Result getPreviousBuildResult() {
    previousBuild = currentBuild.getPreviousBuild()
    if ( previousBuild ) {
        return Result.fromString(previousBuild.result)
    }
    return Result.SUCCESS
}

pipeline {
    agent any
  
    triggers {
       pollSCM "H/5 * * * *"
    }

    environment {
        PREV_CHANGE = ""
    }
    
    stages {
        stage('Build') {
            steps {
                echo "Building ..."
                script {
                    BUILD_RES = sh (script: "python3 index.py", returnStatus: true)
                    echo "Return status : ${BUILD_RES}"
                    if (BUILD_RES == 2) {
                        dontNotify = true
                        currentBuild.result = "ABORTED"
                        sh "exit 1"
                    } else if (BUILD_RES == 1) {
                        currentBuild.result = "FAILURE"
                        sh "exit 1"
                    }
                }
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
                echo "This is the change number: ${params.Change}"
                // check the previous build change env variable
                PREV_CHANGE = currentBuild.buildVariables["PREV_CHANGE"]
                echo "Printing previous changenum"
                echo "${PREV_CHANGE}"
                echo "Previous step result: ${previousBuildResult}"
                echo "${Result.ABORTED}"
                isBetter = Result.ABORTED == "ABORTED"
                echo "is better ? ${isBetter}"
                
                RESULT = sh(
                    script: "python3 getSomeOutput.py",
                    returnStdout: true ).trim()
                echo "${RESULT}"
//                 if (dontNotify) {
//                     echo "Dont Notify"
//                 } else {
//                     echo "Notify"
//                 }
                
//                 // trying to get the result of post.py
//                 RESULT = sh( script:"python3 post.py", returnStdout:true ).trim()
//                 echo "The return value of post.py is ${RESULT}"
                
//                 if (notifyGhcUrls != "" && !dontNotify) {
//                     googlechatnotification url: "${notifyGhcUrls}",
//                                            message: "${env.JOB_NAME} - #${env.BUILD_NUMBER} notification build result ${BUILD_RES} (<${env.BUILD_URL}|Open>)"
//                 }
                
                if (notifyEmailAddresses != "" && !dontNotify) {
                    mail to: "${notifyEmailAddresses}",
                         subject: "Jenkins: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                        body: "See ${env.BUILD_URL} and notify value is ${!dontNotify}"
                }

            }
        }
    }
}
