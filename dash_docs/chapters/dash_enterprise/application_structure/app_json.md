## app.json

`app.json` is an optional file that allow you to specify **predeploy** and **postdeploy** scripts to run 
in your Dash App's environment. It is used by {kubernetes} to configure app health checks similarly to 
how Dash Enterprise Single-Server uses `CHECKS` files — determining when an app is ready to 
receive web traffic. An `apps.json` file must be placed in your app's root directory.

Your `app.json` file may resemble:

**Dash Enterprise Single-Server**

```
{{
    "scripts": {{
        "dokku": {{
            "predeploy": "./predeploy.sh",
            "postdeploy" "./postdeploy.sh"
        }}
    }}
}}
```

See app.json section in {configure_system_dependencies} chapter for more details.

**Dash Enterprise Kubernetes**

```
{{
    "healthchecks": {{
        "web": {{
            "readiness": {{
                "httpGet": {{
                    "path": "/{{ $APP }}/_dash-layout",
                    "port": 5000
                }},
                "initialDelaySeconds": 10,
                "periodSeconds": 15,
                "timeoutSeconds": 15,
                "successThreshold": 1,
                "failureThreshold": 4
            }},
            "liveness": {{
                "httpGet": {{
                    "path": "/{{ $APP }}/_dash-layout",
                    "port": 5000
                }},
                "initialDelaySeconds": 77,
                "periodSeconds": 120,
                "timeoutSeconds": 15,
                "successThreshold": 1,
                "failureThreshold": 10
            }}
        }}
    }},
    "scripts": {{
        "dokku": {{
            "predeploy": "./predeploy.sh",
            "postdeploy" "./postdeploy.sh"
        }}
    }}
}}
    "scripts": {{
        "dokku": {{
            "predeploy": "./predeploy.sh",
            "postdeploy" "./postdeploy.sh"
        }}
    }}
}}

```

See Zero Downtime Deploys section in {kubernetes} chapter for more details.

{kubernetes_notes}
