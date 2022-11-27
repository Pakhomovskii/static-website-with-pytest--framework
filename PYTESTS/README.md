# Description
Simple tests framework based on pytest for the web-site https://pakhomovskii.github.io/static-website-with-pytest--framework/
with POM patterns

# Structure
```
dirs:
  data - config and locators location 
  page_objects - page patterns
  tests:
    - pytests
    results - html reports
```

# Requrements:
`sudo bash preinstall.sh`

# Test Execution
`pytest -v --html=results/report.html`