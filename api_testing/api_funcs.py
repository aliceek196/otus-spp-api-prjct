import time
from api_testing.base_request import BaseRequest


class PublicAPIFuncs(BaseRequest):

    @staticmethod
    def wait_until_task_completed(public_api_client, task_id_value):
        while True:
            task_details = public_api_client.get_task_by_id(task_id_value)
            task_status = task_details["task"]["is_completed"]
            if task_status == "Completed":
                break
            time.sleep(10)  # Check every 10 seconds
            if task_status == "Failed":
                raise ValueError(f'Task FAILED')

    def assert_create_vm_data(actual_vm_data, expected_vm_data):
        # Ignore 'id' and 'created' keys in 'volumes'
        expected_volumes = [{k: v for k, v in vol.items() if k not in ['id', 'created']} for vol in
                            expected_vm_data["volumes"]]
        actual_volumes = [{k: v for k, v in vol.items() if k not in ['id', 'created']} for vol in
                          actual_vm_data["volumes"]]
        # Ignore params in networks (nics)
        expected_networks = [{k: v for k, v in net.items() if
                              k not in ['id', 'network_id', 'network_type', 'mac', 'created', 'ip_address', 'mask',
                                        'gateway']} for net in
                             expected_vm_data["networks"]]
        actual_networks = [{k: v for k, v in net.items() if
                            k not in ['id', 'network_id', 'network_type', 'mac', 'created', 'ip_address', 'mask',
                                      'gateway']} for net in
                           actual_vm_data["nics"]]
        expected_vm_data["volumes"] = expected_volumes
        actual_vm_data["volumes"] = actual_volumes
        expected_vm_data["networks"] = expected_networks
        actual_vm_data["nics"] = actual_networks
        assert actual_vm_data["location_id"] == expected_vm_data["location_id"]
        assert actual_vm_data["image_id"] == expected_vm_data["image_id"]
        assert actual_vm_data["cpu"] == expected_vm_data["cpu"]
        assert actual_vm_data["ram_mb"] == expected_vm_data["ram_mb"]
        assert actual_vm_data["volumes"] == expected_vm_data["volumes"]
        assert actual_vm_data["nics"] == expected_vm_data["networks"]
        assert actual_vm_data["name"] == expected_vm_data["name"]
        assert actual_vm_data["tags"] == expected_vm_data["tags"]
        assert actual_vm_data["is_power_on"] == True
        assert actual_vm_data["login"] == "root" or "Administrator"
        assert actual_vm_data["state"] == "Active"


