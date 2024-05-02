import configparser
from allure import title, feature

from ui_testing.panel_elements.auth import AuthPage

config = configparser.ConfigParser()
config.read('config.ini')

# Read credentials from the config file
username = config['Credentials']['stage_username']
password = config['Credentials']['stage_password']


@feature("vStack Servers")
@title("Actions with volumes")
def test_volumes(browser):
    """Checking that the boot volume cannot be deleted or decreased, actions with volumes"""
    browser.get(browser.panel_url)
    panel_page = AuthPage(browser).login(username, password)
    servers_page = panel_page.click_vstack_servers()
    calculator_page = servers_page.click_create_vstack_server()
    calculator_page \
        .try_decrease_boot_disk_calculator() \
        .try_delete_boot_disk_calculator() \
        .adding_two_volumes("volume1", "volume2") \
        .check_max_count_disks_calculator() \



@feature("vStack Servers")
@title("Select images")
def test_images(browser):
    """Check that the selected image is displayed in the calculator footer"""
    browser.get(browser.panel_url)
    panel_page = AuthPage(browser).login(username, password)
    servers_page = panel_page.click_vstack_servers()
    calculator_page = servers_page.click_create_vstack_server()
    calculator_page \
        .select_ubuntu_image() \
        .select_debian_image() \
        .select_oracle_image() \
        .select_centos_image() \
        .select_fbsd_image() \
        .select_altlinux_image() \
        .select_almalinux_image() \
        .select_redos_image() \
        .select_windows_image() \
        .select_kalilinux_image()


@feature("vStack Servers")
@title("Select locations")
def test_locations(browser):
    """Check that the selected location is displayed in the calculator footer"""
    browser.get(browser.panel_url)
    panel_page = AuthPage(browser).login(username, password)
    servers_page = panel_page.click_vstack_servers()
    calculator_page = servers_page.click_create_vstack_server()
    calculator_page \
        .select_am2_location() \
        .select_nj3_location() \
        .select_ds1_location() \
        .select_kz_location() \
        .select_br_location() \
        .select_ca_location() \
        .select_trk_location()


@feature("vStack Servers")
@title("Check configuration")
def test_edit_configuration(browser):
    """Checking for server configuration changes"""
    browser.get(browser.panel_url)
    panel_page = AuthPage(browser).login(username, password)
    servers_page = panel_page.click_vstack_servers()
    calculator_page = servers_page.click_create_vstack_server()
    calculator_page \
        .change_cpu_calculator() \
        .change_ram_calculator() \



@feature("vStack Servers")
@title("Check fix configuration")
def test_fix_configuration(browser):
    """Checking for server fix configuration selected"""
    browser.get(browser.panel_url)
    panel_page = AuthPage(browser).login(username, password)
    servers_page = panel_page.click_vstack_servers()
    calculator_page = servers_page.click_create_vstack_server()
    calculator_page \
        .select_fix_configuration() \
        .select_second_fix_configuration() \
        .select_sixth_fix_configuration()


@feature("vStack Servers")
@title("Actions with networks")
def test_networks(browser):
    """Checking for changes in network interfaces, maximum number and summarising bandwidth in the footer"""
    browser.get(browser.panel_url)
    panel_page = AuthPage(browser).login(username, password)
    servers_page = panel_page.click_vstack_servers()
    calculator_page = servers_page.click_create_vstack_server()
    calculator_page \
        .check_default_public_nic() \
        .change_network_bandwidth() \
        .check_max_count_ifaces() \
        .delete_additional_ifaces() \



@feature("vStack Servers")
@title("OneClickApps check")
def test_one_click_apps(browser):
    """Check for available OneClickApps applications"""
    browser.get(browser.panel_url)
    panel_page = AuthPage(browser).login(username, password)
    servers_page = panel_page.click_vstack_servers()
    calculator_page = servers_page.click_create_vstack_server()
    calculator_page \
        .select_ubuntu_image() \
        .check_one_click_apps_available() \
        .select_windows_image() \
        .check_one_click_apps_unavailable() \
        .select_oracle_image() \
        .check_one_click_apps_available() \
        .delete_public_nic() \
        .check_one_click_apps_unavailable() \



@feature("vStack Servers")
@title("Multiple servers check")
def test_multiple_servers(browser):
    """Checking the creation of multiple servers"""
    browser.get(browser.panel_url)
    panel_page = AuthPage(browser).login(username, password)
    servers_page = panel_page.click_vstack_servers()
    calculator_page = servers_page.click_create_vstack_server()
    calculator_page \
        .input_vstack_server_name("multiple-servers") \
        .adding_maximum_servers() \
        .delete_additional_servers()


@feature("vStack Servers")
@title("Check API examples")
def test_api_examples(browser):
    """Checking the API example appeared"""
    browser.get(browser.panel_url)
    panel_page = AuthPage(browser).login(username, password)
    servers_page = panel_page.click_vstack_servers()
    calculator_page = servers_page.click_create_vstack_server()
    calculator_page.check_api_example()


@feature("vStack Servers")
@title("Check Tags actions")
def test_tags(browser):
    """Checking actions with tags"""
    browser.get(browser.panel_url)
    panel_page = AuthPage(browser).login(username, password)
    servers_page = panel_page.click_vstack_servers()
    calculator_page = servers_page.click_create_vstack_server()
    calculator_page\
        .input_tag("OTUS") \
        .input_tag("Selenium") \
        .input_tag("MyProject") \
        .delete_tag()


@feature("vStack Servers")
@title("Check authentication")
def test_authentication(browser):
    """Checking authentication options"""
    browser.get(browser.panel_url)
    panel_page = AuthPage(browser).login(username, password)
    servers_page = panel_page.click_vstack_servers()
    calculator_page = servers_page.click_create_vstack_server()
    calculator_page\
        .select_centos_image() \
        .select_ssh_authorization() \
        .select_login_authorization() \
        .select_windows_image() \
        .ssh_auth_unavailable()


@feature("vStack Servers")
@title("Check affinity-groups")
def test_affinity_groups(browser):
    """Checking affinity-groups options"""
    browser.get(browser.panel_url)
    panel_page = AuthPage(browser).login(username, password)
    servers_page = panel_page.click_vstack_servers()
    calculator_page = servers_page.click_create_vstack_server()
    calculator_page \
        .show_affinity_groups() \
        .select_anti_affinity_groups() \
        .add_new_group("anti-affinity") \
        .delete_group() \
        .select_affinity_groups() \
        .add_new_group("affinity") \
        .delete_group() \








