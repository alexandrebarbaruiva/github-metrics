# Github-Metrics

[![Maintainability](https://api.codeclimate.com/v1/badges/700ee542b5ff919da2ff/maintainability)](https://codeclimate.com/github/alexandrebarbaruiva/github-metrics/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/700ee542b5ff919da2ff/test_coverage)](https://codeclimate.com/github/alexandrebarbaruiva/github-metrics/test_coverage)
![Build Status](https://travis-ci.org/alexandrebarbaruiva/github-metrics.svg?branch=master)

Repo for developing a tool to visualize Github metrics from developers

## Installing

### Creating access to your account

First create a token on [Github](https://github.com/settings/tokens),
you only have to tick read privileges, no need to write. After the token has been created,
download this repo, insert the value on `sample.ini` and rename file to `config.ini`.
Now, if you don't have, install
[Python 3.6.7 or higher](https://www.python.org/downloads/).

### Setting up your environment

After installing, all you have to do is create a virtual environment,
activate the env and install everything on `requirements.txt` using
`pip install requirements.txt` and run `inv run`. For more information, use `inv -l`.

## To Do

Things to do to improve tool:

#### Backend

[UNIX to utc timestamp](https://stackoverflow.com/questions/3682748/converting-unix-timestamp-string-to-readable-date)

- [ ] Choose organization to collect data
- [X] Collect info (mainly commits) from all users on said organization [get_stats_contributors]
  - [X] Added lines 
  - [X] Removed lines
  - [X] Commits
- [ ] Collect info from all users on organization with determined period (N weeks, N months, etc)

#### Frontend

[Chart.js](https://www.chartjs.org/)

[Lines chart](https://www.chartjs.org/samples/latest/charts/line/basic.html)

[Use Django with Chart.js](https://www.youtube.com/watch?v=B4Vmm3yZPgc)

- [ ] Show collected info from user on a simple web page (raw info)
  - [ ] Amount of commits
  - [ ] Amount of PRs
  - [ ] Amount of merged PRs 
  - [ ] Amount of created issues
  - [ ] Amount of closed issues
  - [ ] Amount of code reviews
- [ ] Show collected info from user on a graphic 
  - [ ] Commits x Date
- [ ] Show collected info from all users on a single graphic 
  - [ ] Commits x Date

### Interesting links

- https://stackoverflow.com/questions/9058305/getting-attributes-of-a-class
