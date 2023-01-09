test_cases = (
    ({ #1 case 
        "username": "testuser",
        "first_name": "test_fn",
        "last_name": "test_ln",
        "password": "secret",
    }, "user_registration"), # expected response
    ({ #2
        "email": "testemail@gmail.com",
        "username": "testuser",
    }, "newsletter"),
    ({ #3 
        "phone_number": "+7 999 999 99 99",
        "email": "testuser@example.com",
    }, "lead generation form"),
    ({ #4
        "title": "example",
        "body": "body test",
        "username": "testuser",
        "current_date": "07.01.2023",
    }, "article"),
    ({ #5
        "username": "testuser", 
        "my_name": "testmyname",
        "test_date": "2023-01-07",
        "test_email": "123!er@gmail.qwerty",
    },
    { 
        "username": "text", 
        "my_name": "text",
        "test_date": "date",
        "test_email": "text",
    }),
    ({ #6
        "phone_number": "79999999999",
        "email": "test@example.com",
    }, "newsletter"),
)