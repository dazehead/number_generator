docker build -t number-generator-app .
docker run -p 5000:5000 number-generator-app
------------------------------------------------
after creating the instance

ssh -i /path/to/your-key.pem ec2-user@<your-ec2-public-ip>
to connect to the instance
--------------------------------------------------

# Update package index
sudo dnf update -y

# Install Docker
sudo dnf install docker -y

# Start the Docker service
sudo systemctl start docker

# Enable Docker to start on boot
sudo systemctl enable docker

# Add ec2-user to the docker group (so you can run without sudo)
sudo usermod -aG docker ec2-user

# Apply the group change now (or just log out/in after this)
newgrp docker

-----------------------------------------------------
if copying the flask app from git then install git
sudo dnf update -y
sudo dnf install git -y


git clone https://github.com/yourusername/your-flask-repo.git
cd your-flask-repo
---------------------------------------------------------
buidl the docker
docker build -t flask-aws-app .
docker run -d -p 80:5000 flask-aws-app

----------------------------------------------------------
now type in the ip address and it should be running