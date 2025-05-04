// DHEERAJ KRISHNA NAGULA
// G01448319 
// Akhilesh Dhavileswarapu
// G01472450
pipeline {
	agent any
	environment {
	DOCKERHUB_CREDENTIALS = credentials('docker-pass')
	BUILD_TIMESTAMP = "${new Date().format("yyyyMMdd-HHmmss")}"
	}
	
	stages {
		stage("Building the Student Survey Image") {
			steps{
				script {
					sh 'docker build -t dheerajkrishna141/extra_credit:$BUILD_TIMESTAMP .'
				}
			}	
		}
		
		stage("Login to Docker Hub"){
			steps{
				script{
					sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'

				}
			}
		}
		stage("Pushing Image to DockerHub") {
			steps {
				script {
					sh 'docker push dheerajkrishna141/extra_credit:$BUILD_TIMESTAMP'
					}
				}
			}
			
			
		stage("Deploying to Rancher") {
			steps {
				sh 'kubectl set image deployment/sweextracredit container-0=dheerajkrishna141/extra_credit:$BUILD_TIMESTAMP -n extracredit'
				sh 'kubectl rollout status deployment/sweextracredit -n extracredit'
			}
		}
		
		
	}
	
}