from datasets import load_dataset

"""Downaloding the dataset from https://huggingface.co/datasets/shalinik/xsum"""


def test_call_xsum_dataset():

    dataset = load_dataset("shalinik/xsum")

    target_id = "34687720"

    found_records = dataset.filter(lambda example: example["id"] == target_id)

    if len(found_records) > 0:
        record = found_records['test'][0]
        print(f"Found record with id {target_id}:")
        print(record)
    else:
        print(f"No record found with id {target_id}.")

    # You can also check the type and content of found_records
    print(f"\nType of found_records: {type(found_records)}")
    print(f"Number of found records: {len(found_records)}")


if __name__ == '__main__':
    test_call_xsum_dataset()