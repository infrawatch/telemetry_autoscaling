---
config:
    plugin_type: test
subparsers:
    auto-scaling:
        description: Test Autoscaling for instances on openstack telemetry
        include_groups: ["Ansible options", "Inventory", "Common options", "Common variables", "Answers file"]
        groups:      
            - title: Verify
              options:
                  verify_autoscaling:
                      type: Bool
                      help: |
                          Verify overcloud deployment for autoscaling
                      default: false
                  ospversion:
                      type: Value
                      help: |
                          The product version
                          Numbers are for OSP releases
                          Names are for RDO releases
                          If not given, same version of the undercloud will be used
                      choices:
                        - "17.1"
                        - "18.0"

            - title: Configure
              options:
                  configure_heat:
                      type: Bool
                      help: |
                          Configure heat service for autoscaling
                      default: false

            - title: Create
              options:
                  create_stack:
                      type: Bool
                      help: |
                          Create the stack
                      default: false

            - title: Validate
              options:
                  test_autoscale_up:
                      type: Bool
                      help: |
                          Testing automatic scaling up of instances
                      default: false

                  test_autoscale_down:
                      type: Bool
                      help: |
                          Testing automatic scaling down of instances
                      default: false

