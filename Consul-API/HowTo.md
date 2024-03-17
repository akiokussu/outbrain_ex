
Overall overview: 

### 1. Create a GitHub Repository:
* Mirror the given repository as instructed, avoiding forking. This ensures  work remains independent and private.
<br> Please mirror this git repo using the instructions [here](https://help.github.com/articles/duplicating-a-repository). Then clone it locally. (Please DO NOT fork the repo)

### 2.Setup the Consul Server with Vagrant:

* I will use Vagrant and VMware to create a VM that runs Ubuntu.
* Configure the VM to start a Consul server, ensuring it's accessible from  machine for API calls.

1. Download/Install Vagrant and VMware:

    * Install VMware: **brew install hashicorp/tap/hashicorp-vagrant**
    * Install Vagrant: **[VMware Fusion](https://www.vmware.com/go/getfusion)**
    * Install Vagrant VMware desktop plugin: **vagrant plugin install vagrant-vmware-desktop**

2. Initialize Vagrant Project:

    * Initialize a new Vagrantfile: **vagrant init**
    
3. Configure Vagrantfile:

    * Edit  Vagrantfile to install Consul server. 
    Add a shell provisioner block to install and configure Consul:
```

    Vagrant.configure("2") do |config|
        config.vm.box = "bento/ubuntu-20.04-arm64"
        config.vm.hostname = "consul-server"
        config.vm.network "forwarded_port", guest: 8500, host: 8500
        config.vm.provider :vmware_desktop do |vmware|
    end
    config.vm.provision "shell", inline: <<-SHELL
        sudo apt-get update
        sudo apt-get install -y unzip
        wget https://releases.hashicorp.com/consul/1.18.0/consul_1.18.0_linux_arm64.zip
        unzip consul_1.18.0_linux_arm64.zip
        sudo mv consul /usr/local/bin/
        rm consul_1.18.0_linux_arm64.zip
        # -client "0.0.0.0": This option is set to allow connections from any IP address to the Consul client interface, 
        # useful for accessing the UI and API.
        #
        # -bind: This option tells Consul the address to bind server and client interfaces to. 
        #It's used for internal cluster communications.
        consul agent -dev -ui -client=0.0.0.0 -bind=0.0.0.0
     SHELL
    end

```
4. Start the VM:

* Use **vagrant up** to create and provision the VM.

5. Check the SSH and UI
* Check SSH to VM: **vagrant ssh**
* Check UI to VM: **curl http://localhost:8500 -L** 

To access the Consul Web UI on a remote VM via SSH, set up an SSH tunnel for port forwarding from your local machine. This allows secure, local browser access to the remote Consul Web UI.
<br>**ssh -i your_key -L 8500:localhost:8500 user@remote-server -p 22**

### 3. Build the API Service:

* Choose Python or Ruby as  programming language.
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