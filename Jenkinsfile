stage('Deploy to Azure VM') {
    steps {
        script {
            // Login to Azure
            withCredentials([azureServicePrincipal(credentialsId: 'azure-credentials')]) {
                sh 'az login --service-principal -u $AZURE_CLIENT_ID -p $AZURE_CLIENT_SECRET --tenant $AZURE_TENANT_ID'
                sh 'az account set --subscription $AZURE_SUBSCRIPTION_ID'
            }

            // Copy files to Azure VM
            withCredentials([sshUserPrivateKey(credentialsId: 'your-ssh-credentials-id')]) {
                sh 'scp -r . $SSH_USERNAME@your-vm-ip-address:/demo'
            }

            // Run Docker Compose on Azure VM
            withCredentials([sshUserPrivateKey(credentialsId: 'ssh-credentials')]) {
                sh 'ssh $SSH_USERNAME@40.87.68.160 "cd /demo && docker compose up -d"'
            }
        }
    }
}
