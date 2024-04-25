pipeline {
    agent any

    stages {
        stage('Deploy to Azure VM') {
            steps {
                script {
                    // Debug credential binding
                    echo "Azure Client ID: $AZURE_CLIENT_ID"
                    echo "Azure Client Secret: $AZURE_CLIENT_SECRET"
                    echo "Azure Tenant ID: $AZURE_TENANT_ID"
                    echo "Azure Subscription ID: $AZURE_SUBSCRIPTION_ID"
                    echo "SSH Username: $SSH_USERNAME"

                    // Login to Azure
                    withCredentials([azureServicePrincipal(credentialsId: 'azure-credentials')]) {
                        sh 'az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID'
                        sh 'az account set --subscription $AZURE_SUBSCRIPTION_ID'
                    }

                    // Copy files to Azure VM
                    withCredentials([sshUserPrivateKey(credentialsId: 'ssh-credentials')]) {
                        sh 'scp -r . $SSH_USERNAME@40.87.68.160:/demo'
                    }

                    // Run Docker Compose on Azure VM
                    withCredentials([sshUserPrivateKey(credentialsId: 'ssh-credentials')]) {
                        sh 'ssh $SSH_USERNAME@40.87.68.160 "cd /demo && docker compose up -d"'
                    }
                }
            }
        }
    }
}
