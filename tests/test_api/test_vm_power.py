from api_testing.api_funcs import PublicAPIFuncs
from allure import feature, title

power_vm_data = {
    "location_id": "am2",
    "image_id": "Ubuntu-22.04-X64",
    "cpu": 1,
    "ram_mb": 1024,
    "networks": [
        {
            "bandwidth_mbps": 50
        }
    ],
    "volumes": [
        {
            "name": "boot",
            "size_mb": 25600
        }
    ],
    "name": "test-power-vm",
    "tags": ["power"]
}


@feature("Public API: vStack server power")
@title("Powering off the server by OS tools")
def test_power_vm_via_os(public_api_client):
    """The test checks the method of server shutdown by OS tools"""
    create_vm_response = public_api_client.create_vm(**power_vm_data)
    create_vm_response_json = create_vm_response.json()
    assert create_vm_response is not None, 'Failed to create vm'
    task_id_value = create_vm_response_json['task_id']
    PublicAPIFuncs.wait_until_task_completed(public_api_client, task_id_value)
    vm_id = public_api_client.task_by_id(task_id_value)['task']['server_id']
    vm_details = public_api_client.get_vm_by_id(vm_id)['server']
    PublicAPIFuncs.assert_create_vm_data(vm_details, power_vm_data)
    power_off_response = public_api_client.shut_down_vm_via_os(vm_id)
    power_off_response_json = power_off_response.json()
    assert power_off_response is not None, 'Failed to power off vm via os'
    task_id_value = power_off_response_json['task_id']
    PublicAPIFuncs.wait_until_task_completed(public_api_client, task_id_value)
    vm_status = public_api_client.get_vm_by_id(vm_id)['server']['is_power_on']
    assert vm_status is False
    public_api_client.delete_vm(vm_id)
    public_api_client.get_vm_by_id(vm_id, 404)


@feature("Public API: vStack server power")
@title("Powering down the server")
def test_power_vm_power_off(public_api_client):
    """The test checks the method of powering down the server"""
    create_vm_response = public_api_client.create_vm(**power_vm_data)
    create_vm_response_json = create_vm_response.json()
    assert create_vm_response is not None, 'Failed to create vm'
    task_id_value = create_vm_response_json['task_id']
    PublicAPIFuncs.wait_until_task_completed(public_api_client, task_id_value)
    vm_id = public_api_client.task_by_id(task_id_value)['task']['server_id']
    power_off_response = public_api_client.shut_down_vm_via_power_off(vm_id)
    power_off_response_json = power_off_response.json()
    assert power_off_response is not None, 'Failed to power off vm via os'
    task_id_value = power_off_response_json['task_id']
    PublicAPIFuncs.wait_until_task_completed(public_api_client, task_id_value)
    vm_status = public_api_client.get_vm_by_id(vm_id)['server']['is_power_on']
    assert vm_status is False
    public_api_client.delete_vm(vm_id)
    public_api_client.get_vm_by_id(vm_id, 404)


@feature("Public API: vStack server power")
@title("Power rebooting the server")
def test_hard_reboot_vm(public_api_client):
    """The test checks the method of power rebooting the server"""
    create_vm_response = public_api_client.create_vm(**power_vm_data)
    create_vm_response_json = create_vm_response.json()
    assert create_vm_response is not None, 'Failed to create vm'
    task_id_value = create_vm_response_json['task_id']
    PublicAPIFuncs.wait_until_task_completed(public_api_client, task_id_value)
    vm_id = public_api_client.task_by_id(task_id_value)['task']['server_id']
    reboot_response = public_api_client.hard_reboot_vm(vm_id)
    reboot_response_json = reboot_response.json()
    assert reboot_response is not None, 'Failed to reboot vm'
    task_id_value = reboot_response_json['task_id']
    PublicAPIFuncs.wait_until_task_completed(public_api_client, task_id_value)
    vm_status = public_api_client.get_vm_by_id(vm_id)['server']['is_power_on']
    assert vm_status is True
    public_api_client.delete_vm(vm_id)
    public_api_client.get_vm_by_id(vm_id, 404)


@feature("Public API: vStack server power")
@title("Power reboot of the server using OS tools")
def test_soft_reboot_vm(public_api_client):
    """The test checks the method of server rebooting by OS tools"""
    create_vm_response = public_api_client.create_vm(**power_vm_data)
    create_vm_response_json = create_vm_response.json()
    assert create_vm_response is not None, 'Failed to create vm'
    task_id_value = create_vm_response_json['task_id']
    PublicAPIFuncs.wait_until_task_completed(public_api_client, task_id_value)
    vm_id = public_api_client.task_by_id(task_id_value)['task']['server_id']
    reboot_response = public_api_client.soft_reboot_vm(vm_id)
    reboot_response_json = reboot_response.json()
    assert reboot_response is not None, 'Failed to reboot vm'
    task_id_value = reboot_response_json['task_id']
    PublicAPIFuncs.wait_until_task_completed(public_api_client, task_id_value)
    vm_status = public_api_client.get_vm_by_id(vm_id)['server']['is_power_on']
    assert vm_status is True
    public_api_client.delete_vm(vm_id)
    public_api_client.get_vm_by_id(vm_id, 404)
