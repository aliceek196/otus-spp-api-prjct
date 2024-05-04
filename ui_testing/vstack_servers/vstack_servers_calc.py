from selenium.webdriver.common.by import By
from ui_testing.base_page import BasePage
from allure import step


class VstackServersCalculatorPage(BasePage):
    CREATE_SERVER_BUTTON = (By.XPATH, "//*[text()='Создать сервер']")
    LOGIN_AUTHORIZATION = (By.XPATH, "//*[text()='Логин / пароль']")
    SSH_AUTHORIZATION = (By.XPATH, "//*[text()='SSH-ключи']")
    INPUT_VSTACK_SERVER_NAME = (By.XPATH, "//input[contains(@placeholder, "
                                          "'Введите название сервера')]")
    INPUT_GROUP_NAME = (By.XPATH, "//input[contains(@placeholder, "
                                  "'Введите название группы')]")
    CREATE_GROUP_BUTTON = (By.XPATH, "//button[@role='submit-btn']")
    CREATE_BUTTON = (By.XPATH, "//*[text()='Создать']")
    UBUNTU_IMAGE = (By.XPATH, "//*[text()='Ubuntu']")
    UBUNTU_IMAGE_FOOTER = (By.XPATH, "//span[@role='os-name' "
                                     "and contains(text(), 'Ubuntu')]")
    ORACLE_IMAGE = (By.XPATH, "//*[text()='Oracle Linux']")
    ORACLE_IMAGE_FOOTER = (By.XPATH, "//span[@role='os-name' "
                                     "and contains(text(), 'Oracle')]")
    CENTOS_IMAGE = (By.XPATH, "//*[text()='CentOS']")
    CENTOS_IMAGE_FOOTER = (By.XPATH, "//span[@role='os-name' "
                                     "and contains(text(), 'CentOS')]")
    FBSD_IMAGE = (By.XPATH, "//*[text()='FreeBSD']")
    FBSD_IMAGE_FOOTER = (By.XPATH, "//span[@role='os-name' "
                                   "and contains(text(), 'FreeBSD')]")
    ALTLINUX_IMAGE = (By.XPATH, "//*[text()='AltLinux']")
    ALTLINUX_IMAGE_FOOTER = (By.XPATH, "//span[@role='os-name' "
                                       "and contains(text(), 'AltLinux')]")
    ALMALINUX_IMAGE = (By.XPATH, "//*[text()='AlmaLinux']")
    ALMALINUX_IMAGE_FOOTER = (By.XPATH, "//span[@role='os-name' "
                                        "and contains(text(), 'AlmaLinux')]")
    REDOS_IMAGE = (By.XPATH, "//*[text()='RedOS']")
    REDOS_IMAGE_FOOTER = (By.XPATH, "//span[@role='os-name' "
                                    "and contains(text(), 'RedOS')]")
    WINDOWS_IMAGE = (By.XPATH, "//*[text()='Windows']")
    WINDOWS_IMAGE_FOOTER = (By.XPATH, "//span[@role='os-name' "
                                      "and contains(text(), 'Windows')]")
    DEBIAN_IMAGE = (By.XPATH, "//*[text()='Debian']")
    DEBIAN_IMAGE_FOOTER = (By.XPATH, "//span[@role='os-name' "
                                     "and contains(text(), 'Debian')]")
    KALILINUX_IMAGE = (By.XPATH, "//*[text()='KaliLinux']")
    KALILINUX_IMAGE_FOOTER = (By.XPATH, "//span[@role='os-name' "
                                        "and contains(text(), 'KaliLinux')]")
    FIX_CONFIGURATION = (By.XPATH, "//*[text()='Фиксированные конфигурации']")
    SECOND_FIX_CONFIG = (By.XPATH, "(//div[@class='vue-radio-block "
                                   "fixed-config-item'])[2]")
    DELETE_FIRST_NIC = (By.XPATH, "//button[@class='vue-button "
                                  "vue-button--big reverse danger "
                                  "vue-remove-btn server-configuration-flex-"
                                  "networks-list-item-actions-delete']")
    NO_PUBLIC_NIC_MESSAGE = (By.XPATH, "//*[text()='Виртуальный сервер будет "
                                       "создан без подключения к "
                                       "публичной сети']")
    ONE_CLICK_APPS = (By.XPATH, "//div[@class='vstack-block applications']")
    INPUT_TAG = (By.XPATH, "//input[contains(@placeholder, "
                           "'Выберите тег или введите новый')]")
    API_BUTTON = (By.XPATH, "//*[text()=' API ']")
    API_CODE = (By.XPATH, "//div[@class='code vstack-automatization"
                          "-api-code']")
    POPUP_CLOSE_BUTTON = (By.XPATH, "//div[@class='vue-popup-close']")
    INCREASE_CPU = (By.XPATH, "(//button[@class='vue-counter__btn vue-counter"
                              "__btn--plus'])[1]")
    INCREASE_RAM = (By.XPATH, "(//button[@class='vue-counter__btn vue-counter"
                              "__btn--plus'])[2]")
    DECREASE_BOOT_DISK = (By.XPATH, "(//div[@class='configuration-grid with-"
                                    "control']//following::button[@class="
                                    "'vue-counter__btn vue-counter__btn--"
                                    "minus'])[1]")
    DISABLED_DELETE_BOOT_DISK = (By.XPATH, "//button[@class='vue-button vue-"
                                           "button--big disabled reverse "
                                           "danger vue-remove-btn disabled "
                                           "server-configuration-flex-disks-"
                                           "list-item-actions-delete']")
    BOOT_DISK_TOOLTIP = (By.XPATH, "//*[text()='Нельзя удалить "
                                   "загрузочный диск']")
    BOOT_DISK_SIZE_COUNTER = (By.XPATH, "(//div[@class='server-configuration"
                                        "-item server-configuration-flex-disks"
                                        "-list-item-control']//following::span"
                                        "[@class='vue-counter__value'])[1]")
    ADD_VOLUME_BUTTON = (By.XPATH, "//*[text()='Добавить том']")
    INPUT_FIRST_ADD_DISK_NAME = (By.XPATH, "(//input[contains(@placeholder, "
                                           "'Название тома')])[2]")
    INCREASE_FIRST_ADD_DISK = (By.XPATH, "(//div[@class='configuration-grid "
                                         "with-control']//following::button"
                                         "[@class='vue-counter__btn vue-"
                                         "counter__btn--plus'])[2]")
    INPUT_SECOND_ADD_DISK_NAME = (By.XPATH, "(//input[contains(@placeholder, "
                                            "'Название тома')])[3]")
    INCREASE_SECOND_ADD_DISK = (By.XPATH, "(//div[@class='configuration-grid "
                                          "with-control']//following::button"
                                          "[@class='vue-counter__btn vue-"
                                          "counter__btn--plus'])[3]")
    CHECK_DISKS_SUM_CALC = (By.XPATH, "//span[@role='ssd-value' "
                                      "and text()='125 ГБ']")
    ADD_VOLUME_DISABLED = (By.XPATH, "//button[@class='vue-button vue-button"
                                     "--small disabled vue-add-btn "
                                     "disabled add-item-main']")
    DELETE_THIRD_ADD_DISK = (By.XPATH, "(//button[@class='vue-button vue-butto"
                                       "n--big reverse danger vue-remove-btn "
                                       "server-configuration-flex-disks-list-"
                                       "item-actions-delete'])[3]")
    DEFAULT_PUBLIC_NIC = (By.XPATH, "//*[text()='Публичная сеть']")
    AMSTERDAM = (By.XPATH, "//*[text()='Амстердам']")
    AMSTERDAM_FOOTER = (By.XPATH, "//span[@role='location' "
                                  "and contains(text(), 'Амстердам')]")
    NEW_JERSEY = (By.XPATH, "//*[text()='Нью-Джерси']")
    NEW_JERSEY_FOOTER = (By.XPATH, "//span[@role='location' "
                                   "and contains(text(), 'Нью-Джерси')]")
    MOSCOW = (By.XPATH, "//*[text()='Москва']")
    MOSCOW_FOOTER = (By.XPATH, "//span[@role='location' "
                               "and contains(text(), 'Москва')]")
    ALMATY = (By.XPATH, "//*[text()='Алматы']")
    ALMATY_FOOTER = (By.XPATH, "//span[@role='location' "
                               "and contains(text(), 'Алматы')]")
    ISTANBUL = (By.XPATH, "//*[text()='Стамбул']")
    ISTANBUL_FOOTER = (By.XPATH, "//span[@role='location' "
                                 "and contains(text(), 'Стамбул')]")
    TORONTO = (By.XPATH, "//*[text()='Торонто']")
    TORONTO_FOOTER = (By.XPATH, "//span[@role='location' "
                                "and contains(text(), 'Торонто')]")
    SAO_PAULO = (By.XPATH, "//*[text()='Сан-Паулу']")
    SAO_PAULO_FOOTER = (By.XPATH, "//span[@role='location' "
                                  "and contains(text(), 'Сан-Паулу')]")
    CPU_VALUE_FOOTER = (By.XPATH, "//span[@role='cpu-value' and text()='3']")
    DECREASE_CPU = (By.XPATH, "(//button[@class='vue-counter__btn "
                              "vue-counter__btn--minus'])[1]")
    RAM_VALUE_FOOTER = (By.XPATH, "//span[@role='ram-value' "
                                  "and text()='4 ГБ']")
    DECREASE_RAM_BUTTON = (By.XPATH, "(//button[@class='vue-counter__btn "
                                     "vue-counter__btn--minus'])[2]")
    SECOND_FIX_CPU_FOOTER = (By.XPATH, "//span[@role='cpu-value' "
                                       "and text()='1']")
    SECOND_FIX_RAM_FOOTER = (By.XPATH, "//span[@role='ram-value' "
                                       "and text()='2 ГБ']")
    SECOND_FIX_SSD_FOOTER = (By.XPATH, "//span[@role='ssd-value' "
                                       "and text()='50 ГБ']")
    SECOND_FIX_BANDWIDTH_FOOTER = (By.XPATH, "//span[@role='bandwidth-value' "
                                             "and text()='50 Мбит/с']")
    SIXTH_FIX_CONFIG = (By.XPATH, "(//div[@class='vue-radio-block "
                                  "fixed-config-item'])[5]")
    SIXTH_FIX_CPU_FOOTER = (By.XPATH, "//span[@role='cpu-value' "
                                      "and text()='3']")
    SIXTH_FIX_RAM_FOOTER = (By.XPATH, "//span[@role='ram-value' "
                                      "and text()='1 ГБ']")
    SIXTH_FIX_SSD_FOOTER = (By.XPATH, "//span[@role='ssd-value' "
                                      "and text()='60 ГБ']")
    SIXTH_FIX_BANDWIDTH_FOOTER = (By.XPATH, "//span[@role='bandwidth-value' "
                                            "and text()='50 Мбит/с']")
    INCREASE_BANDWIDTH = (By.XPATH, "(//button[@class='vue-counter__btn "
                                    "vue-counter__btn--plus'])[4]")
    DECREASE_BANDWIDTH = (By.XPATH, "(//button[@class='vue-counter__btn "
                                    "vue-counter__btn--minus'])[4]")
    NETWORK_VALUE_FOOTER = (By.XPATH, "//span[@role='bandwidth-value' "
                                      "and text()='80 Мбит/с']")
    ADD_NETWORK_BUTTON = (By.XPATH, "//*[text()='Добавить сеть']")
    ADD_NETWORK_DISABLED = (By.XPATH, "//button[@class='vue-button vue-button"
                                      "--small disabled vue-add-btn disabled "
                                      "server-configuration-empty-btn']")
    DELETE_NETWORK = (By.XPATH, "(//span[@class='vue-remove-btn-icon'])[4]")
    NETWORK_SUM_VALUE_FOOTER = (By.XPATH, "//span[@role='bandwidth-value' "
                                          "and text()='180 Мбит/с']")
    ADD_SERVER_BUTTON = (By.XPATH, "//div[@class='vue-counter__btn "
                                   "vue-counter__btn--plus']")
    SERVER_MAXIMUM_WARNING = (By.XPATH, "//*[text()='Одновременно можно "
                                        "создать не более 5 серверов.']")
    DELETE_SERVER_BUTTON = (By.XPATH, "//div[@class='vue-counter__btn "
                                      "vue-counter__btn--minus']")
    DELETE_TAG_BUTTON = (By.XPATH, "(//span[@class='vue-tags-item-remove "
                                   "v-popper--has-tooltip'])[1]")
    SHOW_AFFINITY = (By.XPATH, "//button[@class='vue-button vue-button--small "
                               "reverse more vstack-groups-show-button']")
    ADD_NEW_GROUP_BUTTON = (By.XPATH, "//*[text()='Добавить новую группу']")
    ANTI_AFFINITY_GROUPS = (By.XPATH, "//*[text()='Anti-Affinity']")
    AFFINITY_GROUPS = (By.XPATH, "//*[text()='Affinity']")
    GROUP_IN_LIST = (By.XPATH, "//div[@role='groups-available']")
    GROUP_MENU = (By.XPATH, "//div[@class='vstack-groups-list-radio-menu']")
    DELETE_GROUP_BUTTON = (By.XPATH, "//button[@role='remove-btn']")

    @step("Select login auth in server calculator page")
    def select_login_authorization(self):
        self.scroll_and_get_element(self.LOGIN_AUTHORIZATION).click()
        return self

    @step("Input vStack server name in calculator page")
    def input_vstack_server_name(self, name):
        self.scroll_and_get_element(self.INPUT_VSTACK_SERVER_NAME)
        self.input_value(self.INPUT_VSTACK_SERVER_NAME, name)
        return self

    @step("Select Ubuntu image in server calculator page")
    def select_ubuntu_image(self):
        self.get_element(self.UBUNTU_IMAGE).click()
        assert self.get_element(self.UBUNTU_IMAGE_FOOTER)
        return self

    @step("Select Oracle image in server calculator page")
    def select_oracle_image(self):
        self.get_element(self.ORACLE_IMAGE).click()
        assert self.get_element(self.ORACLE_IMAGE_FOOTER)
        return self

    @step("Select Centos image in server calculator page")
    def select_centos_image(self):
        self.get_element(self.CENTOS_IMAGE).click()
        assert self.get_element(self.CENTOS_IMAGE_FOOTER)
        return self

    @step("Select FreeBSD image in server calculator page")
    def select_fbsd_image(self):
        self.get_element(self.FBSD_IMAGE).click()
        assert self.get_element(self.FBSD_IMAGE_FOOTER)
        return self

    @step("Select AltLinux image in server calculator page")
    def select_altlinux_image(self):
        self.get_element(self.ALTLINUX_IMAGE).click()
        assert self.get_element(self.ALTLINUX_IMAGE_FOOTER)
        return self

    @step("Select AlmaLinux image in server calculator page")
    def select_almalinux_image(self):
        self.get_element(self.ALMALINUX_IMAGE).click()
        assert self.get_element(self.ALMALINUX_IMAGE_FOOTER)
        return self

    @step("Select RedOS image in server calculator page")
    def select_redos_image(self):
        self.get_element(self.REDOS_IMAGE).click()
        assert self.get_element(self.REDOS_IMAGE_FOOTER)
        return self

    @step("Select Windows image and check no "
          "ssh auth in server calculator page")
    def select_windows_image(self):
        self.get_element(self.WINDOWS_IMAGE).click()
        assert self.element_disappeared(self.SSH_AUTHORIZATION)
        assert self.get_element(self.WINDOWS_IMAGE_FOOTER)
        return self

    @step("SSH auth unavailable")
    def ssh_auth_unavailable(self):
        assert self.element_disappeared(self.SSH_AUTHORIZATION)
        return self

    @step("Select Debian image in server calculator page")
    def select_debian_image(self):
        self.get_element(self.DEBIAN_IMAGE).click()
        assert self.get_element(self.DEBIAN_IMAGE_FOOTER)
        return self

    @step("Select KaliLinux image in server calculator page")
    def select_kalilinux_image(self):
        self.get_element(self.KALILINUX_IMAGE).click()
        assert self.get_element(self.KALILINUX_IMAGE_FOOTER)
        return self

    @step("Select fix configuration in server calculator page")
    def select_fix_configuration(self):
        self.get_element(self.FIX_CONFIGURATION).click()
        self.scroll_and_get_element(self.SECOND_FIX_CONFIG).click()
        return self

    @step("Select second fix configuration")
    def select_second_fix_configuration(self):
        self.scroll_and_get_element(self.SECOND_FIX_CONFIG).click()
        assert self.get_element(self.SECOND_FIX_CPU_FOOTER)
        assert self.get_element(self.SECOND_FIX_RAM_FOOTER)
        assert self.get_element(self.SECOND_FIX_SSD_FOOTER)
        assert self.get_element(self.SECOND_FIX_BANDWIDTH_FOOTER)
        return self

    @step("Select sixth fix configuration")
    def select_sixth_fix_configuration(self):
        self.scroll_and_get_element(self.SIXTH_FIX_CONFIG).click()
        assert self.get_element(self.SIXTH_FIX_CPU_FOOTER)
        assert self.get_element(self.SIXTH_FIX_RAM_FOOTER)
        assert self.get_element(self.SIXTH_FIX_SSD_FOOTER)
        assert self.get_element(self.SIXTH_FIX_BANDWIDTH_FOOTER)
        return self

    @step("Change CPU in server calculator")
    def change_cpu_calculator(self):
        self.repeat_action(self.INCREASE_CPU, 5)
        self.repeat_action(self.DECREASE_CPU, 3)
        assert self.get_element(self.CPU_VALUE_FOOTER)
        return self

    @step("Change RAM in server calculator")
    def change_ram_calculator(self):
        self.repeat_action(self.INCREASE_RAM, 7)
        self.repeat_action(self.DECREASE_RAM_BUTTON, 4)
        assert self.get_element(self.RAM_VALUE_FOOTER)
        return self

    @step("Checking for 1ClickApps in server calculator page")
    def check_one_click_apps_available(self):
        self.get_element(self.ONE_CLICK_APPS)
        return self

    @step("Delete public NIC in server calculator page")
    def delete_public_nic(self):
        self.scroll_and_get_element(self.DELETE_FIRST_NIC)
        assert self.scroll_and_get_element(self.NO_PUBLIC_NIC_MESSAGE)
        return self

    @step("Checking for 1ClickApps NOT in server calculator page")
    def check_one_click_apps_unavailable(self):
        assert self.element_disappeared(self.ONE_CLICK_APPS)
        return self

    @step("Input tag in server calculator page")
    def input_tag(self, tag):
        self.scroll_and_get_element(self.INPUT_TAG)
        self.input_value(self.INPUT_TAG, tag)
        self.click_enter(self.INPUT_TAG)
        return self

    @step("Delete first tag in server calculator page")
    def delete_tag(self):
        self.get_element(self.DELETE_TAG_BUTTON)
        return self

    @step("Checking for API example in server calculator page")
    def check_api_example(self):
        self.scroll_and_get_element(self.API_BUTTON)
        assert self.get_element(self.API_CODE)
        self.get_element(self.POPUP_CLOSE_BUTTON).click()
        return self

    @step("Select ssh-key auth in server calculator page")
    def select_ssh_authorization(self):
        self.scroll_and_get_element(self.SSH_AUTHORIZATION).click()
        return self

    @step("Trying to delete a boot disk in server calculator")
    def try_delete_boot_disk_calculator(self):
        self.scroll_and_get_element(self.DISABLED_DELETE_BOOT_DISK).click()
        self.get_element(self.BOOT_DISK_TOOLTIP)
        return self

    @step("Trying to decrease a boot disk in server calculator")
    def try_decrease_boot_disk_calculator(self):
        initial_disk_size = self.scroll_and_get_element(
            self.BOOT_DISK_SIZE_COUNTER).text
        self.get_element(self.DECREASE_BOOT_DISK).click()
        current_disk_size = self.get_element(self.BOOT_DISK_SIZE_COUNTER).text
        if initial_disk_size == current_disk_size:
            print("Test passed: "
                  "Boot disk size remains unchanged")
        else:
            print("Test failed: "
                  "Boot disk size changed after attempting to shrink")
        return self

    @step("Adding two additional disks in the server calculator")
    def adding_two_volumes(self, first_disk_name, second_disk_name):
        self.scroll_and_get_element(self.ADD_VOLUME_BUTTON)
        self.input_value(self.INPUT_FIRST_ADD_DISK_NAME, first_disk_name)
        self.repeat_action(self.INCREASE_FIRST_ADD_DISK, 3)
        self.scroll_and_get_element(self.ADD_VOLUME_BUTTON)
        self.input_value(self.INPUT_SECOND_ADD_DISK_NAME, second_disk_name)
        self.repeat_action(self.INCREASE_SECOND_ADD_DISK, 5)
        self.get_element(self.CHECK_DISKS_SUM_CALC)
        return self

    @step("Checking the maximum number of disks in the calculator "
          "and the sum of all disks in the footer")
    def check_max_count_disks_calculator(self):
        self.repeat_action(self.ADD_VOLUME_BUTTON, 4)
        self.get_element(self.ADD_VOLUME_DISABLED)
        self.repeat_action(self.DELETE_THIRD_ADD_DISK, 2)
        self.get_element(self.CHECK_DISKS_SUM_CALC)
        return self

    @step("Checking default public address in server calculator")
    def check_default_public_nic(self):
        self.scroll_and_get_element(self.DEFAULT_PUBLIC_NIC)
        return self

    @step("Select Amsterdam location")
    def select_am2_location(self):
        self.get_element(self.AMSTERDAM).click()
        assert self.get_element(self.AMSTERDAM_FOOTER)
        return self

    @step("Select New Jersy location")
    def select_nj3_location(self):
        self.get_element(self.NEW_JERSEY).click()
        assert self.get_element(self.NEW_JERSEY_FOOTER)
        return self

    @step("Select Moscow location")
    def select_ds1_location(self):
        self.get_element(self.MOSCOW).click()
        assert self.get_element(self.MOSCOW_FOOTER)
        return self

    @step("Select Almaty location")
    def select_kz_location(self):
        self.get_element(self.ALMATY).click()
        assert self.get_element(self.ALMATY_FOOTER)
        return self

    @step("Select Istanbul location")
    def select_trk_location(self):
        self.get_element(self.ISTANBUL).click()
        assert self.get_element(self.ISTANBUL_FOOTER)
        return self

    @step("Select Toronto location")
    def select_ca_location(self):
        self.get_element(self.TORONTO).click()
        assert self.get_element(self.TORONTO_FOOTER)
        return self

    @step("Select Sao Paulo location")
    def select_br_location(self):
        self.get_element(self.SAO_PAULO).click()
        assert self.get_element(self.SAO_PAULO_FOOTER)
        return self

    @step("Change network bandwidth")
    def change_network_bandwidth(self):
        self.repeat_action(self.INCREASE_BANDWIDTH, 7)
        self.repeat_action(self.DECREASE_BANDWIDTH, 4)
        assert self.get_element(self.NETWORK_VALUE_FOOTER)
        return self

    @step("Checking the maximum number of ifaces in the calculator")
    def check_max_count_ifaces(self):
        self.repeat_action(self.ADD_NETWORK_BUTTON, 4)
        assert self.get_element(self.ADD_NETWORK_DISABLED)
        return self

    @step("Checking the delete additional ifaces")
    def delete_additional_ifaces(self):
        self.repeat_action(self.DELETE_NETWORK, 2)
        assert self.get_element(self.NETWORK_SUM_VALUE_FOOTER)
        return self

    @step("Checking to add the maximum number of server")
    def adding_maximum_servers(self):
        self.repeat_action(self.ADD_SERVER_BUTTON, 4)
        assert self.scroll_and_get_element(self.SERVER_MAXIMUM_WARNING)
        return self

    @step("Checking to delete the maximum number of server")
    def delete_additional_servers(self):
        self.repeat_action(self.DELETE_SERVER_BUTTON, 4)
        assert self.element_disappeared(self.SERVER_MAXIMUM_WARNING)
        return self

    @step("Show affinity groups")
    def show_affinity_groups(self):
        self.scroll_and_get_element(self.SHOW_AFFINITY).click()
        self.click(self.SHOW_AFFINITY)
        assert self.get_element(self.ADD_NEW_GROUP_BUTTON)
        return self

    @step("Select anti-affinity groups")
    def select_anti_affinity_groups(self):
        self.get_element(self.ANTI_AFFINITY_GROUPS).click()
        return self

    @step("Add new group")
    def add_new_group(self, name):
        self.get_element(self.ADD_NEW_GROUP_BUTTON).click()
        self.input_value(self.INPUT_GROUP_NAME, name)
        self.get_element(self.CREATE_GROUP_BUTTON).click()
        assert self.get_element(self.GROUP_IN_LIST)
        return self

    @step("Delete group")
    def delete_group(self):
        self.get_element(self.GROUP_IN_LIST).click()
        self.get_element(self.GROUP_MENU).click()
        self.get_element(self.DELETE_GROUP_BUTTON).click()
        assert self.element_disappeared(self.GROUP_IN_LIST)
        return self

    @step("Select affinity groups")
    def select_affinity_groups(self):
        self.get_element(self.AFFINITY_GROUPS).click()
        return self
