import requests
import psutil

CONSUL_BASE_URL = 'http://localhost:8500/v1'

def get_consul_status():
    try:
        response = requests.get(f'{CONSUL_BASE_URL}/agent/self')
        if response.ok:
            return {"status": 1, "message": "Consul server is running"}
        else:
            return {"status": 0, "message": "Failed to connect to Consul server"}
    except requests.exceptions.RequestException as e:
        return {"status": 0, "message": f"Consul server is down - {e}"}

def get_cluster_summary():
    try:
        nodes = requests.get(f'{CONSUL_BASE_URL}/catalog/nodes').json()
        services = requests.get(f'{CONSUL_BASE_URL}/catalog/services').json()
        leader = requests.get(f'{CONSUL_BASE_URL}/status/leader').text.strip('"')
        protocol = requests.get(f'{CONSUL_BASE_URL}/agent/self').json().get('Config', {}).get('ProtocolCur', 'N/A')
        return {
            "registered_nodes": len(nodes),
            "registered_services": len(services),
            "leader": leader,
            "cluster_protocol": protocol
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch cluster summary - {e}"}

def get_cluster_members():
    try:
        nodes = requests.get(f'{CONSUL_BASE_URL}/catalog/nodes').json()
        member_names = [node['Node'] for node in nodes]
        return {"registered_nodes": member_names}
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch cluster members - {e}"}

def get_system_info():
    return {
        "vCpus": psutil.cpu_count(logical=True),
        "MemoryGB": round(psutil.virtual_memory().total / (1024**3), 2),
        "CPU_Usage_Percent": psutil.cpu_percent(interval=1),
        "Disk_Total_GB": round(psutil.disk_usage('/').total / (1024**3), 2),
        "Disk_Used_GB": round(psutil.disk_usage('/').used / (1024**3), 2),
        "Disk_Used_Percent": psutil.disk_usage('/').percent,
        "Swap_Memory_Total_GB": round(psutil.swap_memory().total / (1024**3), 2),
        "Swap_Memory_Used_GB": round(psutil.swap_memory().used / (1024**3), 2),
        "Swap_Memory_Used_Percent": psutil.swap_memory().percent
    }
