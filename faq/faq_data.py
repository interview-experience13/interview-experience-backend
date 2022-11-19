from .models import FAQ

data = {
    "data": [
        {
            "id": 1,
            "attributes": {
                "question": "What is the testing library most often associated with React?",
                "answer": "Jest"
            }
        },
        {
            "id": 2,
            "attributes": {
                "question": "A representation of a user interface that is kept in memory and is synced with the 'real' DOM is called what?",
                "answer": "Virtual DOM"
            }
        }
    ],
}

def run():
    '''
        python manage.py shell
        from student_api.faker import run
        run()
        exit()
        # https://faker.readthedocs.io/en/master/
    '''

    fake = Faker()
    paths = (
        "FullStack",
        "DataScience",
        "AwsDevops",
        "CyberSec",
    )

    for path in paths:
        new_path = FAQ.objects.create(question = path)
        for _ in range(50):
            Student.objects.create(path = new_path, first_name = fake.first_name(), last_name = fake.last_name(), number = fake.pyint())
    
    print('OK')