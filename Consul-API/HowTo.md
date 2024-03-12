
Overall overview: 

### 1. Create a GitHub Repository:
* Mirror the given repository as instructed, avoiding forking. This ensures your work remains independent and private.
<br> Please mirror this git repo using the instructions [here](https://help.github.com/articles/duplicating-a-repository). Then clone it locally. (Please DO NOT fork the repo)
___

### 2.Setup the Consul Server with Vagrant:

* Use Vagrant and VirtualBox to create a VM that runs Ubuntu.
* Configure the VM to start a Consul server, ensuring it's accessible from your machine for API calls.

1. Install Vagrant and VirtualBox:

    * Install VirtualBox: **sudo apt-get install virtualbox**
    * Install Vagrant: **sudo apt-get install vagrant**

2. Initialize Your Vagrant Project:

    * Create a new directory for your project and navigate into it: **mkdir consul_project && cd consul_project**
    * Initialize a new Vagrantfile with an Ubuntu 20.04 box: **vagrant init ubuntu/focal64**

    
3. Configure Vagrantfile:

    * Edit your Vagrantfile to install Consul on up. Add a shell provisioner block to install and configure Consul:
```
    Vagrant.configure("2") do |config|
        config.vm.box = "ubuntu/focal64"
        config.vm.network "forwarded_port", guest: 8500, host: 8500
        config.vm.provider "virtualbox" do |vb|
            vb.name = "ConsulDevServer"
        end
        config.vm.provision "shell", inline: <<-SHELL
            wget https://releases.hashicorp.com/consul/1.9.5/consul_1.9.5_linux_amd64.zip
            unzip consul_1.9.5_linux_amd64.zip
            sudo mv consul /usr/local/bin/
            consul agent -dev -ui -bind 0.0.0.0
        SHELL
    end

```
4. Start the VM:

* Use **vagrant up** to create and provision the VM.

error after command 
```
The box you're attempting to add doesn't support the provider
you requested. Please find an alternate box or use an alternate
provider. Double-check your requested provider to verify you didn't
simply misspell it.

If you're adding a box from HashiCorp's Vagrant Cloud, make sure the box is
released.

Name: ubuntu/focal64
Address: https://vagrantcloud.com/ubuntu/focal64
Requested provider: [:libvirt]
``` 
tried to start manually **sudo vagrant up --provider=virtualbox**
```
The provider 'virtualbox' that was requested to back the machine
'default' is reporting that it isn't usable on this system. The
reason is shown below:

VirtualBox is complaining that the installation is incomplete. Please
run `VBoxManage --version` to see the error message which should contain
instructions on how to fix this error.
```



<br> Failed to start LSB: VirtualBox Linux kernel module 







Port forwarding from the local machine to Consul WEB UI 
ssh -L 8500:localhost:8500 user@remote-server -p 22





















### 3. Build the API Service:

* Choose Python or Ruby as your programming language.
* Develop endpoints as specified, focusing on interactions with the Consul API to retrieve and display cluster information.

### 4. Dockerize the API Service:

* Create a Dockerfile that sets up environment, installs dependencies, and runs service, ensuring output is logged to the console.

### 5. Code and Commit Best Practices:

* Structure the code with clear organization and naming conventions.
* Maintain a meaningful commit history to demonstrate development progress.

### 6. Testing and Validation:

* Ensure Consul environment works as expected, with a functioning cluster and a known leader.
* Test API endpoints to verify they return the correct data.


### Usfull links 

* [Introduction to HashiCorp Consul with Armon Dadgar](https://www.youtube.com/watch?v=mxeMdl0KvBI&t=71s&ab_channel=HashiCorp)