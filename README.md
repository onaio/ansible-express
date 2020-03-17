Role Name
=========

Installs and configures an express app built with typescript

This role installs and configures:

- node
- yarn
- pm2
- and other node packages that the app is dependent on

We intentionally consider the installation and configuration of web servers, and other things as out of scope for this role. Therefore, naturally this role is to be used in a playbook that installs and configures those other things, if you need them.

Role Variables
--------------

Some of the more important variables are briefly described below.  You can see all variables by looking at the `defaults/main.yml` file.

```yml
express_system_user: "express"  # name of the user that will own the django installation
express_node_version: 10.x  # the version of node to install

express_git_url: "https://github.com/onaio/kaznet-frontend.git"  # the git repo of your django app which we are installing
express_git_key:
```

### Custom environment variables

[Create express app](https://github.com/facebook/create-express-app) supports [custom environment variables](https://github.com/facebook/create-express-app/blob/master/packages/express-scripts/template/README.md#adding-custom-environment-variables) and this role does too!

You can set custom environment variables by using the `express_app_settings` variable, like so:

```yml
express_app_settings:
    SOME_VARIABLE: "you can put anything here"
```

Testing
------------

This project uses molecule for testing using a docker driver and testinfra as the verifier

Start by creating a virtual environment and install the pypi packages in `requirements.txt`

Then to run the full test sequence

```sh
molecule test
```

License
-------

APACHE-2

Author Information
------------------

[Ona Engineering](https://ona.io)
