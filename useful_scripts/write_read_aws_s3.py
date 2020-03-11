# Get the batch_plan key
from datetime import datetime

def get_s3_key(_zone_id, _batch_plan_at):

    BEGINNING_OF_TIME = datetime(1970, 1, 1)
    snapshot_at = datetime.strptime(_batch_plan_at[:19], "%Y-%m-%dT%H:%M:%S")
    epoch_timestamp = int((snapshot_at - BEGINNING_OF_TIME).total_seconds())
    s3_key = "no_shift_plan-zone_id=%s-timestamp=%s" % (_zone_id, epoch_timestamp)

    return s3_key
