import boto3

def get_kali_ami(region='ap-southeast-1'):
    ec2 = boto3.client('ec2', region_name=region)

    print(f"Searching for Kali Linux AMIs in {region}...")

    filters = [
        {'Name': 'name', 'Values': ['*kali*', '*Kali*']},
        {'Name': 'state', 'Values': ['available']},
        {'Name': 'architecture', 'Values': ['x86_64']},
    ]

    try:
        response = ec2.describe_images(
            Owners=['aws-marketplace'],
            Filters=filters
        )

        images = sorted(response['Images'],
                        key=lambda x: x['CreationDate'],
                        reverse=True)

        if not images:
            print("No Kali Linux AMIs found.")
            return

        print(f"Found {len(images)} image(s).\n")

        for i, ami in enumerate(images, 1):
            volume = ami['BlockDeviceMappings'][0]['Ebs'] if ami.get('BlockDeviceMappings') else {}
            print(f"[{i}] {ami['Name']}")
            print(f"    AMI ID        : {ami['ImageId']}")
            print(f"    Description   : {ami.get('Description', 'N/A')}")
            print(f"    Creation Date : {ami['CreationDate']}")
            print(f"    Deprecation   : {ami.get('DeprecationTime', 'N/A')}")
            print(f"    Architecture  : {ami['Architecture']}")
            print(f"    Virtualization: {ami['VirtualizationType']}")
            print(f"    Root Device   : {ami['RootDeviceName']} ({volume.get('VolumeType', 'N/A')}, {volume.get('VolumeSize', 'N/A')} GB)")
            print(f"    ENA Support   : {ami.get('EnaSupport', False)}")
            print(f"    Free Tier     : {ami.get('FreeTierEligible', False)}")
            print(f"    Public        : {ami.get('Public', False)}")
            print()

    except Exception as e:
        print(f"Error querying AWS: {e}")

if __name__ == "__main__":
    get_kali_ami('ap-southeast-1')
