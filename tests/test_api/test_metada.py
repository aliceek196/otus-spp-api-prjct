import pytest
from allure import feature, title


@feature("Public API: Meta-information for vStack servers")
@title("Getting a list of available locations")
@pytest.mark.parametrize("expected_location_id",
                         ["am2", "nj3", "br", "kz", "ca"])
def test_locations_list(expected_location_id, public_api_client):
    """The test checks that the specified locations are
    available for creating resources in them"""
    locations_response = public_api_client.get_locations_list()
    received_location_ids = [location["id"]
                             for location in locations_response["locations"]]
    assert expected_location_id in received_location_ids, \
        f"Expected location '{expected_location_id}' not found"


@feature("Public API: Meta-information for vStack servers")
@title("Getting a list of available images")
@pytest.mark.parametrize("expected_image", [
    "Windows-Server 2022-X64",
    "Ubuntu-22.04-X64",
    "CentOS-7.9-X64",
    "Debian-11.6-X64",
    "Oracle-9.3-X64"
])
def test_images_list(expected_image, public_api_client):
    """The test checks that the specified images are available for creation"""
    images_response = public_api_client.get_images_list()
    received_images_ids = [images["id"]
                           for images in images_response["images"]]
    assert expected_image in received_images_ids, \
        f"Expected image '{expected_image}' not found"
