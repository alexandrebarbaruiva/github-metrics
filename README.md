# github-metrics

Repo for developing a tool to visualize Github metrics from developers

## Installing



## Setting up your environment for contributing



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
