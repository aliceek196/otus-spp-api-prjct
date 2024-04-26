from api_testing.base_request import BaseRequest


class GeneralPublicAPIMethods:

    def __init__(self, base_url, header=None):
        self.base_request = BaseRequest(base_url, header)

    def get_task_by_id(self, task_id, expected_error_code=False, expected_error_message=None):
        return self.base_request.get(
            'tasks',
            task_id,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    def create_vm(self, location_id, image_id, cpu, ram_mb, volumes=None, networks=None, name=None,
                  ssh_key_ids=None, application_ids=None, tags=None, affinity_group_id=None, server_init_script=None,
                  expected_error_code=False, expected_error_message=None):
        data = {
            "location_id": location_id,
            "image_id": image_id,
            "cpu": cpu,
            "ram_mb": ram_mb,
            "volumes": volumes,
            "networks": networks,
            "name": name,
            "ssh_key_ids": ssh_key_ids,
            "application_ids": application_ids,
            "tags": tags,
            "affinity_group_id": affinity_group_id,
            "server_init_script": server_init_script
        }
        return self.base_request.post(
            'servers',
            '',
            data=data,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    def get_vm_by_id(self, vm_id, expected_error_code=False, expected_error_message=None):
        return self.base_request.get(
            'servers',
            vm_id,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    def change_all_vm_configuration(self, cpu, ram_mb, vm_id, expected_error_code=False, expected_error_message=None):
        data = {
            "cpu": cpu,
            "ram_mb": ram_mb
        }
        response = self.base_request.put(
            'servers',
            vm_id,
            data=data,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )
        return response

    def delete_vm(self, vm_id, expected_error_code=False, expected_error_message=None):
        return self.base_request.delete(
            'servers',
            vm_id,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    def shut_down_vm_via_os(self, vm_id, expected_error_code=False, expected_error_message=None):
        return self.base_request.post(
            'servers',
            vm_id+'/power/off',
            '',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    def power_on_vm(self, vm_id, expected_error_code=False, expected_error_message=None):
        return self.base_request.post(
            'servers',
            vm_id+'/power/on',
            '',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    def shut_down_vm_via_power_off(self, vm_id, expected_error_code=False, expected_error_message=None):
        return self.base_request.post(
            'servers',
            vm_id+'/power/shutdown',
            '',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    def soft_reboot_vm(self, vm_id, expected_error_code=False, expected_error_message=None):
        return self.base_request.post(
            'servers',
            vm_id+'/power/reboot',
            '',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    def hard_reboot_vm(self, vm_id, expected_error_code=False, expected_error_message=None):
        return self.base_request.post(
            'servers',
            vm_id+'/power/reset',
            '',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    def get_locations_list(self, expected_error_code=False, expected_error_message=None):
        return self.base_request.get(
            'locations',
            '',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    def get_images_list(self, expected_error_code=False, expected_error_message=None):
        return self.base_request.get(
            'images',
            '',
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )

    def add_volume(self, vm_id, name, size_mb, expected_error_code=False, expected_error_message=None):
        data = {
            "name": name,
            "size_mb": size_mb
        }
        response = self.base_request.post(
            'servers',
            vm_id + '/volumes',
            data=data,
            expected_error_code=expected_error_code,
            expected_error_message=expected_error_message
        )
        return response



