# Preface #

This document describes the functionality provided by the xlr-ansible-extended-plugin.

See the **[XL Release Reference Manual](https://docs.xebialabs.com/xl-release/)** for background information on XL Release and release concepts.

# Overview #

The xlr-ansible-extended-plugin is a XL Release plugin provides a task which run [Ansible](https://www.ansible.com/) Playbook with environment variables. This plugin provide facility to pass environment variable to Ansible runtime environment. This plugin is extended from the base Ansible plugin provided with XL Release.

## Types ##

You can pass multiple variables, it should be passed as below:
```
var1=value1 var2='some other value'
```
