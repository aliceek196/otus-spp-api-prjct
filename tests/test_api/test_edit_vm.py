import pytest
from api_testing.api_funcs import PublicAPIFuncs

edit_vm_data = {
    "location_id": "am2",
    "cpu": 2,
    "ram_mb": 4096,
    "image_id": "FreeBSD-14.0-X64",
    "name": "test-edit-vm",
    "networks": [
        {
            "bandwidth_mbps": 50
        }
    ],
    "volumes": [
        {
            "name": "boot",
            "size_mb": 102400
        },
        {
            "name": "vol1",
            "size_mb": 40960
        }
    ],
    "tags": ["edit"]
}


@pytest.mark.parametrize("cpu, ram_mb, expected_cpu, expected_ram_mb, expected_error_code, expected_error_message", [
    ('3', '2048', 3, 2048, None, None),
    ('1', '8192', 1, 8192, None, None),
    ('0', '2048', None, None, 400,
     'Unable to process current configuration. Change the number of CPU cores or the RAM capacity.'),
    ('1', '200', None, None, 400,
     'Unable to process current configuration. Change the number of CPU cores or the RAM capacity.')
])
def test_edit_vm_configuration(public_api_client, cpu, ram_mb, expected_cpu, expected_ram_mb, expected_error_code,
                               expected_error_message):
    create_vm_response = public_api_client.create_vm(**edit_vm_data)
    create_vm_response_json = create_vm_response.json()
    assert create_vm_response is not None, 'Failed to create vm'
    task_id_value = create_vm_response_json['task_id']
    PublicAPIFuncs.wait_until_task_completed(public_api_client, task_id_value)
    vm_id = public_api_client.get_task_by_id(task_id_value)['task']['server_id']
    vm_details = public_api_client.get_vm_by_id(vm_id)['server']
    PublicAPIFuncs.assert_create_vm_data(vm_details, edit_vm_data)
    change_vm_response = public_api_client.change_all_vm_configuration(cpu, ram_mb, vm_id, expected_error_code,
                                                                       expected_error_message)
    change_vm_response_json = change_vm_response.json()
    if expected_error_code is not None:
        assert change_vm_response.status_code == expected_error_code, 'Expected error code does not match'
        assert change_vm_response_json['errors'][0][
                   'message'] == expected_error_message, 'Expected error message does not match'
    else:
        assert change_vm_response is not None, 'Failed to change vm'
        task_id_value = change_vm_response_json['task_id']
        PublicAPIFuncs.wait_until_task_completed(public_api_client, task_id_value)
        changed_vm_details = public_api_client.get_vm_by_id(vm_id)['server']
        assert changed_vm_details['cpu'] == expected_cpu
        assert changed_vm_details['ram_mb'] == expected_ram_mb
    public_api_client.delete_vm(vm_id)
    public_api_client.get_vm_by_id(vm_id, 404)


add_volume_vm_data = {
    "location_id": "am2",
    "cpu": 3,
    "ram_mb": 1024,
    "image_id": "Debian-12-X64",
    "name": "test-add-vm-volume",
    "tags": [
        "voumes"
    ],
    "networks": [],
    "volumes": [
    {
      "name": "boot",
      "size_mb": 25600
    }
    ]
}


@pytest.mark.parametrize("name, size_mb, expected_name, expected_size_mb, expected_error_code, expected_error_message",
                         [
                             ('valid', '30720', 'valid', 30720, None, None),
                             ('non_10', '22528', None, None, 400, 'Volume size is not supported'),
                             ('to_small', '2048', None, None, 400, 'The volume is too small'),
                             ('to_big', '2048000', None, None, 400, 'Volume size limit exceeded'),
                             ('zero', '0', None, None, 400, 'Volume size is not supported')
                         ])
def test_add_vm_volume(public_api_client, name, size_mb, expected_name, expected_size_mb, expected_error_code,
                       expected_error_message):
    create_vm_response = public_api_client.create_vm(**add_volume_vm_data)
    assert create_vm_response is not None, 'Failed to create vm'
    create_vm_response_json = create_vm_response.json()
    task_id_value = create_vm_response_json['task_id']
    PublicAPIFuncs.wait_until_task_completed(public_api_client, task_id_value)
    vm_id = public_api_client.get_task_by_id(task_id_value)['task']['server_id']
    vm_details = public_api_client.get_vm_by_id(vm_id)['server']
    PublicAPIFuncs.assert_create_vm_data(vm_details, add_volume_vm_data)
    add_volume_response = public_api_client.add_volume(vm_id, name, size_mb, expected_error_code, expected_error_message)
    add_volume_response_json = add_volume_response.json()
    if expected_error_code is not None:
        assert add_volume_response.status_code == expected_error_code, 'Expected error code does not match'
        assert add_volume_response_json['errors'][0][
                   'message'] == expected_error_message, 'Expected error message does not match'
    else:
        assert add_volume_response is not None, 'Failed to change vm'
        task_id_value = add_volume_response_json['task_id']
        PublicAPIFuncs.wait_until_task_completed(public_api_client, task_id_value)
        added_volume_details = public_api_client.get_vm_by_id(vm_id)['server']['volumes'][1]
        assert added_volume_details['name'] == expected_name
        assert added_volume_details['size_mb'] == expected_size_mb
    public_api_client.delete_vm(vm_id)
    public_api_client.get_vm_by_id(vm_id, 404)
