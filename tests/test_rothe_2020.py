import warnings
warnings.simplefilter('ignore', category=FutureWarning)
warnings.simplefilter('ignore', category=UserWarning)


import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


def test_pipeline():

    if torch.cuda.is_available():
        device_obj = torch.device('cuda:0')
    else:
        device_obj = torch.device('cpu')
    # end if

    tokenizer = AutoTokenizer.from_pretrained("google/roberta2roberta_L-24_bbc")
    model = AutoModelForSeq2SeqLM.from_pretrained("google/roberta2roberta_L-24_bbc")

    model = model.to(device_obj)

    article = """The problem is affecting people using the older
    versions of the PlayStation 3, called the "Fat"
    model.The problem isn't affecting the newer PS3
    Slim systems that have been on sale since
    September last year.Sony have also said they are
    aiming to have the problem fixed shortly but is
    advising some users to avoid using their console
    for the time being."We hope to resolve this
    problem within the next 24 hours," a statement
    reads. "In the meantime, if you have a model other
    than the new slim PS3, we advise that you do not
    use your PS3 system, as doing so may result in
    errors in some functionality, such as recording
    obtained trophies, and not being able to restore
    certain data."We believe we have identified that
    this problem is being caused by a bug in the clock
    functionality incorporated in the system."The
    PlayStation Network is used by millions of people
    around the world.It allows users to play their
    friends at games like Fifa over the internet and
    also do things like download software or visit
    online stores."""

    input_ids = tokenizer(article, return_tensors="pt").input_ids
    input_ids = input_ids.to(device_obj)

    output_ids = model.generate(input_ids)[0]
    print(tokenizer.decode(output_ids, skip_special_tokens=True))
    # should output
    # Some Sony PlayStation gamers are being advised to stay away from the network because of a problem with the PlayStation 3 network.



if __name__ == '__main__':
    test_pipeline()
