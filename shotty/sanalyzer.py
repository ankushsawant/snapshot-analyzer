import boto3
import click

session = boto3.Session(profile_name='ec2user')
ec2 = session.resource('ec2')

def filter_instances(project):
    "Helper function to return EC2 instances, for a given project"

    instances = []
    if project:
        filters = [{'Name': 'tag:Project', 'Values': [project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    return instances

@click.group()
def instances():
    "Commands for EC2 instances"

    return

@instances.command('list')
@click.option('--project', default=None, help='Only instances for project (tag Project:<name>)')
def list_instances(project):
    "Lists EC2 instances"

    instances = filter_instances(project)

    for i in instances:
        tags = { t['Key']: t['Value'] for t in i.tags or []}
        print(', '.join((
            i.instance_id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            tags.get('Project', '<no project>')
            )))

    return

@instances.command('stop')
@click.option('--project', default=None, help='Only instances for project (tag Project:<name>)')
def stop_instances(project):
    "Stop EC2 instances"

    instances = filter_instances(project)

    for i in instances:
        print('Stopping instance: ' + str(i.instance_id))
        i.stop()

    return

@instances.command('start')
@click.option('--project', default=None, help='Only instances for project (tag Project:<name>)')
def start_instances(project):
    "Start EC2 instances"

    instances = filter_instances(project)

    for i in instances:
        print('Starting instance: ' + str(i.instance_id))
        i.start()

    return

@instances.command('terminate')
@click.option('--project', default=None, help='Only instances for project (tag Project:<name>)')
def terminate_instances(project):
    "Start EC2 instances"

    instances = filter_instances(project)

    for i in instances:
        print('Terminating instance: ' + str(i.instance_id))
        i.terminate()

    return


if __name__ == '__main__':
    instances()
