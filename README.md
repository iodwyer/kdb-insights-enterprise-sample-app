# kdb-insights-enterprise-sample-app

## Pre-requisites

* Install & configure the `kxi` CLI: https://code.kx.com/insights/1.6/platform/cli/index.html

## Deploy
```bash
kxi assembly deploy -f kdb-insights-enterprise-sample-app.yaml 
```

## Teardown
```bash
kxi assembly teardown --name kdb-sample-app
```