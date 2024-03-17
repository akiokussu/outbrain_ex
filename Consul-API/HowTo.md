
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
        # -client "0.0.0.0": This option is set to allow connections from any IP address to the Consul client interface, 
        # useful for accessing the UI and API.
        #
        # -bind: This option tells Consul the address to bind server and client interfaces to. 
        #It's used for internal cluster communications.
        consul agent -server -ui -client=0.0.0.0 -bind=0.0.0.0
     SHELL
    end

```
4. Start the VM:

* Use **vagrant up** to create and provision the VM.

5. Check the SSH and UI
* Check SSH to VM: **vagrant ssh**
* Check UI to VM: **curl http://localhost:8500 -L** 

To access the Consul Web UI on a remote VM via SSH, set up an SSH tunnel for port forwarding from local machine. This allows secure, local browser access to the remote Consul Web UI.
<br>**ssh -i _key -L 8500:localhost:8500 user@remote-server -p 22**

### 3. Build the API Service:

* Choose Python or Ruby as  programming language.
* Develop endpoints as specified, focusing on interactions with the Consul API to retrieve and display cluster information.

### 4. Dockerize the API Service:

* 


### 5. Testing and Validation:

To verify that  API is working correctly after deploying it with Docker and Gunicorn, you can use curl to make requests to the API endpoints you've defined. Assuming  Docker container is running and mapped to port 6000 on  host machine, you can use the following curl commands to test each of the endpoints:

**Testing the /v1/api/consulCluster/status Endpoint**

```
curl http://localhost:6000/v1/api/consulCluster/status
```
Expected Output:
    ```
    {"status": 1, "message": "Consul server is running"}
    ```

**Testing the /v1/api/consulCluster/summary Endpoint**
```
curl http://localhost:6000/v1/api/consulCluster/summary
```

**Testing the /v1/api/consulCluster/members Endpoint**
```
curl http://localhost:6000/v1/api/consulCluster/members
```

**Testing the /v1/api/consulCluster/systemInfo Endpoint**
```
curl http://localhost:6000/v1/api/consulCluster/systemInfo
```
Expected Output
    ```
    {
    "vCpus": 4,
    "MemoryGB": 16,
    "CPU_Usage_Percent": 10.2,
    "Disk_Total_GB": 250,
    "Disk_Used_GB": 120,
    "Disk_Used_Percent": 48,
    "Swap_Memory_Total_GB": 1,
    "Swap_Memory_Used_GB": 0.1,
    "Swap_Memory_Used_Percent": 10
    }
    ```
