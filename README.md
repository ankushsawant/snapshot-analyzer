# snapshot-analyzer
Python project to manage AWS EC2 snapshots

## About
Simple Python project, that uses boto3 and click modules to manage AWS EC2 instances

## Configuring
snapshot-analyzer uses AWS profile created by AWS CLI

e.g. `aws configure --profile ec2user`

## Running
`pipenv run "python shotty\sanalyzer.py <command> <--project=ProjectName>"`

*command* is list, start, stop or terminate
*project* is optional
