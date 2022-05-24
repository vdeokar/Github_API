## README
## GITHUB_API Commit Info

This python scripts takes the following 5 input arguments and returns 5
 latest commits for the git repo/branch, with commit SHA, Commit Author and
 Commit message in a html table format.

##### Input arguments: 
```
  Github base url (e.g. https://github.com/ )
  Github owner
  git repo
  git branch
  output html report file path
```

#### How to run the script

##### 1. Install Requirements

```commandline
  Clone the repo
  cd Github_API/
  create a virtualenv
     1. python3 -m virtualenv venv
     2. source venv/bin/activate
  pip3 install -r requirements.txt (pip version atleast 22.0.4)
```
##### 2. Execute the script   
 
```commandline

  python3 github_fetch.py -a <Github_base_URL> -o <Github_owner> -r
 <Github_repo> -b <Github_branch> -p <Output_Path_html_report_file>

  Eg: python3 github_fetch.py -a "api.github.com" -o "kubernetes" -r
 "kubernetes" -b "master" -p "./html/"

```
      
##### HTML Report Sample

<details>
<summary>Code HTML</summary>

```html<!DOCTYPE html>
<html lang="en">
<style>table, th, td {
  border:1px solid black;
  text-align: center;
  vertical-align: middle;
}tbody td{
  padding: 10px;
}tbody tr:nth-child(odd){
  background-color: #76B900;
  color: #000000;
}</style>
<head>
    <title>My Github_API Python Project</title>
</head>
<body>
<h1>Github Commit Details</h1>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>No.</th>
      <th>CommitID</th>
      <th>Author</th>
      <th>Message</th>
    </tr>
  </thead>
<tbody>
      <tr>
         <td>0</td>
         <td>fdb2d544751adc9fd2f6fa5075e9a16df7d352df</td>
         <td>Kubernetes Prow Robot</td>
         <td>Merge pull request #108210 from jlsong01/update_kubectl_warning
             coordinate the kubectl warning style</td>
      </tr> 
      <tr>
         <td>1</td>
         <td>31a10245d67544b6718f569a1442b1de97a91e7d</td>
         <td>Kubernetes Prow Robot</td>
         <td>Merge pull request #110058 from glebiller/managed-fields-time
             Update managedFields time when field value is modified</td>
      </tr>
      <tr>
         <td>2</td>
         <td>aa49dffc7f24dc31dd333869be8e6e3cdfc00af9</td>
         <td>Kubernetes Prow Robot</td>
         <td>Merge pull request #110148 from wojtek-t/metrics_recorder_shutdown
             Clear shutdown of scheduler metrics recorder</td>
      </tr>
      <tr>
         <td>3</td>
         <td>1131fb95fc9e7f864dfa186000f815062061f1b9</td>
         <td>Kubernetes Prow Robot</td>
         <td>Merge pull request #110125 from wojtek-t/fix_resource_quota_shutdown
             Fix resource quota shutdown</td>
      </tr>
      <tr>
         <td>4</td>
         <td>cfd69463deeebfc5ae8a0813d7d2b125033c4aca</td>
         <td>Kubernetes Prow Robot</td>
         <td>Merge pull request #109975 from wojtek-t/cleanup_repair_controllers
             Cleanup portallocator/ipallocator interfaces</td>
      </tr>
</tbody>
</table>
</body>
</html>
```


</details>



#### Rendered HTML 
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
<h2>Github Commit Details</h2>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>No.</th>
      <th>CommitID</th>
      <th>Author</th>
      <th>Message</th>
    </tr>
  </thead>
<tbody> 
      <tr>
         <td>0</td>
         <td>fdb2d544751adc9fd2f6fa5075e9a16df7d352df</td>
         <td>Kubernetes Prow Robot</td>
         <td>Merge pull request #108210 from jlsong01/update_kubectl_warning
               coordinate the kubectl warning style</td>
      </tr>  
      <tr>
         <td>1</td>
         <td>31a10245d67544b6718f569a1442b1de97a91e7d</td>
         <td>Kubernetes Prow Robot</td>
         <td>Merge pull request #110058 from glebiller/managed-fields-time
            Update managedFields time when field value is modified</td>
      </tr>
      <tr>
         <td>2</td>
         <td>aa49dffc7f24dc31dd333869be8e6e3cdfc00af9</td>
         <td>Kubernetes Prow Robot</td>
         <td>Merge pull request #110148 from wojtek-t/metrics_recorder_shutdown
             Clear shutdown of scheduler metrics recorder</td>
      </tr>
      <tr>
         <td>3</td>
         <td>1131fb95fc9e7f864dfa186000f815062061f1b9</td>
         <td>Kubernetes Prow Robot</td>
         <td>Merge pull request #110125 from wojtek-t/fix_resource_quota_shutdown
             Fix resource quota shutdown</td>
      </tr>
      <tr>
         <td>4</td>
         <td>cfd69463deeebfc5ae8a0813d7d2b125033c4aca</td>
         <td>Kubernetes Prow Robot</td>
         <td>Merge pull request #109975 from wojtek-t/cleanup_repair_controllers
             Cleanup portallocator/ipallocator interfaces</td>
      </tr>
</tbody>
</table>
</body>
</html>

#### Next steps

      - Support Private repos
      - Input validation
      - Test Coverage ?

#### DEVELOPMENT

API
```commandline
curl -H "Accept: application/vnd.github.v3+json" \
"https://api.github.com/repos/kubernetes/kubernetes/commits?sha=master&per_page=5&page=1"

```

#### Run the tests


```commandline
python3 -m unittest test/mock.py
```


