


# import boto3

# # Create an S3 client
# s3 = boto3.client('s3')

# # List all S3 buckets
# response = s3.list_buckets()

# print("S3 Buckets in your AWS account:")
# for bucket in response['Buckets']:
#     print(f"- {bucket['Name']}")


import boto3
from datetime import datetime, timedelta

def get_billed_regions(start_date, end_date):
    """
    Retrieves the list of AWS regions where charges occurred between start_date and end_date.
    
    :param start_date: Start date (YYYY-MM-DD) for the cost query.
    :param end_date: End date (YYYY-MM-DD) for the cost query.
    :return: Set of region names with billed resources.
    """
    # Create a Cost Explorer client
    ce = boto3.client('ce')

    try:
        response = ce.get_cost_and_usage(
            TimePeriod={
                'Start': start_date,
                'End': end_date
            },
            Granularity='MONTHLY',  # You can also use DAILY if needed
            Metrics=['UnblendedCost'],
            GroupBy=[
                {
                    'Type': 'DIMENSION',
                    'Key': 'REGION'
                },
            ]
        )
    except Exception as e:
        print(f"Error fetching cost data: {e}")
        return set()

    billed_regions = set()
    results_by_time = response.get('ResultsByTime', [])
    for result in results_by_time:
        groups = result.get('Groups', [])
        for group in groups:
            # Each group corresponds to a region
            keys = group.get('Keys', [])
            if not keys:
                continue
            region = keys[0]
            # Get the cost amount for the region
            cost_info = group.get('Metrics', {}).get('UnblendedCost', {})
            amount = float(cost_info.get('Amount', '0'))
            if amount > 0:
                billed_regions.add(region)
    return billed_regions

if __name__ == '__main__':
    # Define the time period for your cost query.
    # For example, we take the last 30 days.
    end_date_obj = datetime.today().date()
    start_date_obj = end_date_obj - timedelta(days=30)

    start_date_str = start_date_obj.strftime('%Y-%m-%d')
    end_date_str = end_date_obj.strftime('%Y-%m-%d')

    regions = get_billed_regions(start_date_str, end_date_str)
    if regions:
        print("Regions with billed resources in the last 30 days:")
        for region in regions:
            print(f"- {region}")
    else:
        print("No billed resources found in the specified time period.")
