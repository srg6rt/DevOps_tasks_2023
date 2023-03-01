provider "aws" {
  # Configure the AWS Provider
  region = "eu-central-1"

}


# 1. Create vpc
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "production"
  }
}

# 2. Create Internet Gateway
resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id
}

# 3. Create Custom Route Table
resource "aws_route_table" "prod-route-table" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gw.id
  }

  route {
    ipv6_cidr_block = "::/0"
    gateway_id      = aws_internet_gateway.gw.id
  }

  tags = {
    Name = "Prod"
  }
}

# 4. Create a Subnet
resource "aws_subnet" "subnet_1" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "eu-central-1a"

  tags = {
    Name = "prod subnet"
  }

}

# 5. Associate subnet with Route Table
resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.subnet_1.id
  route_table_id = aws_route_table.prod-route-table.id
}

# 6. Create Securrity Group to allow port 22,80,443
resource "aws_security_group" "allow_web" {
  name        = "allow_web_traffic"
  description = "Allow Web inbound traffic"
  vpc_id      = aws_vpc.main.id

  ingress {
    description = "HTTPS from VPC"
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP from VPC"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH from VPC"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1" # Any protocol
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "allow_web"
  }
}

# 7. Create  a network interface with an ip in the subnet that was created in step 4
resource "aws_network_interface" "web-server-nic" {
  subnet_id       = aws_subnet.subnet_1.id
  private_ips     = ["10.0.1.50"]
  security_groups = [aws_security_group.allow_web.id]

}

# 8. Assign an elastic IP to the network interface created in step 7
resource "aws_eip" "one" {
  vpc                       = true
  network_interface         = aws_network_interface.web-server-nic.id
  associate_with_private_ip = "10.0.1.50"
  depends_on = [
    aws_internet_gateway.gw
  ]

}

# 9. Create Ubuntu server and install/enable apache2
resource "aws_instance" "web-server-instance" {
  ami               = "ami-08f13e5792295e1b2"
  instance_type     = "t2.micro"
  availability_zone = "eu-central-1a"
  key_name          = "frankfut-eu-central-1"

  network_interface {
    device_index         = 0
    network_interface_id = aws_network_interface.web-server-nic.id
  }


  user_data = <<-EOF
            #!/bin/bash
            sudo apt update -y
            sudo apt install apache2 -y
            sudo apt install apache2-dev -y
            sudo apt install libapache2-mod-wsgi-py3 -y
            sudo apt install python3-venv libexpat1 -y
            sudo apt install pip -y

            sudo systemctl start apache2

            sudo bash -c 'echo "Test web page" > /var/www/html/index.html'
            
            EOF

  connection {
    type        = "ssh"
    user        = "admin"
    private_key = file("/var/lib/jenkins/frankfut-eu-central-1.pem")
    host        = aws_instance.web-server-instance.public_ip

  }

  provisioner "remote-exec" {
    inline = [
      "echo 'Waiting for user data script to finish'",
      "cloud-init status --wait > /dev/null"
    ]

  }

  provisioner "file" {
      source      = "/var/lib/jenkins/workspace/terraform_git/AWS_projecto"
      destination = "/tmp/AWS_projecto"

  }

  provisioner "remote-exec" {
     inline = [ "echo 'copy Django project'",
                "sudo chmod 777 -R /tmp/AWS_projecto/*.*",
                "sudo cp -R /tmp/AWS_projecto/*.* /var/www/html/", 
                "sudo pip install -r /var/www/html/requirements.txt",
                "cd /var/www/html/",
                "sudo cp apache2.conf /etc/apache2/apache2.conf",
                "sudo cp ennvars /etc/apache2/ennvars",
                "sudo chmod 664 /var/www/html/aussichtsturm/db.sqlite3",
                "sudo chown :www-data /var/www/html/aussichtsturm/db.sqlite3",
                "sudo systemctl restart apache2"]
    # on_failure = continue

  }

  tags = {
    Name = "Web Server"
  }

}



output "server_public_ip" {
  value = aws_eip.one.public_ip
}

output "server_private_ip" {
  value = aws_instance.web-server-instance.private_ip
}
