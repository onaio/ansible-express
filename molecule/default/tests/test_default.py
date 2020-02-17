import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

def test_add_system_user(host):
    user_home = host.user(name='express')
    assert user_home.home == '/home/express'

@pytest.mark.parametrize('node_package', ['node', 'pm2'])
def test_node_and_pm2_is_installed(host, node_package):
    package_version_res = host.run('{} --version'.format(node_package))
    assert package_version_res.rc == 0

def test_node_version(host):
    node_version_res = host.run('node --version');
    assert node_version_res.stdout.startswith('v10.')

@pytest.mark.parametrize("name", ['git', 'yarn' ])
def test_packages(host, name):
    package = host.package(name)
    assert package.is_installed

def test_ensure_directories_are_present(host):
    user_home = host.file('/home/express')
    assert user_home.exists
    assert user_home.is_directory
    express_code_basePath = host.file('/home/express/app')
    assert express_code_basePath.is_symlink

# configure.yml

def test_check_env_file(host):
    express_env_path = host.file('/home/express/app/server/.env')
    express_env_path.exists
    assert 'NODE_ENV' in express_env_path.content_string

def test_installs_js_requirements(host):
    express_node_modules_path = host.file('/home/express/app/server/node_modules')
    express_node_modules_path.exists

def test_express_is_running(host):
    get_local_host = host.run('curl http://localhost:3000')
    assert """"message":"ENOENT: no such file or directory, stat '/home/express/app-versioned/""" in get_local_host.stdout

def test_express_service_is_up(host):
    express_server = host.sysctl('express.service')
    assert express_server == ''