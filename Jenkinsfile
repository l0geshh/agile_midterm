pipeline {
    agent any
    parameters {
        string(name: 'WORD_TO_TEST', defaultValue: 'racecar', description: 'Enter a word to check if it is a palindrome')
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Run Palindrome Check') {
            steps {
                // Jenkins will execute this Windows batch command
                bat "python logesh.py %WORD_TO_TEST%"
            }
        }
    }
}