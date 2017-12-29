# Jobs - API
An application to serve as an API to manage business logic.

## Routes

| METHOD | URL | Description |
| --- | --- | --- |
| GET    | `/jobs/` | Gets a list of jobs |
| GET    | `/jobs/<id>` | Gets a certain job |
| POST   | `/jobs/` | Creates a job |
| PATCH  | `/jobs/<id>` | Updates a job |
| DELETE | `/jobs/<id>` | Deletes a job |

## Sample data

`GET /jobs/`

```
[
    {
        "id": 1,
        "title": "Full Stack Developer",
        "description": "I think my strongest asset maybe by far is my temperament. I have a placeholding temperament. Lorem Ipsum is unattractive, both inside and out. I fully understand why it’s former users left it for something else. They made a good decision. Does everybody know that pig named Lorem Ipsum? She's a disgusting pig, right?",
        "location": "Dubai",
        "company": "Airbnb",
        "email": "jobs@airbnb.com",
        "created_at": "2017-12-29T23:39:39.967356Z"
    },
    {
        "id": 2,
        "title": "UX Designer",
        "description": "I have a 10-year-old son. He has words. He is so good with these words it's unbelievable. Trump Ipsum is calling for a total and complete shutdown of Muslim text entering your website. Be careful, or I will spill the beans on your placeholder text.",
        "location": "San Francisco, USA",
        "company": "Facebook",
        "email": "jobs@facebook.com",
        "created_at": "2017-12-29T23:50:49.661760Z"
    },
    {
        "id": 3,
        "title": "Software Engineer",
        "description": "An ‘extremely credible source’ has called my office and told me that Barack Obama’s placeholder text is a fraud. Look at these words. Are they small words? And he referred to my words - if they're small, something else must be small. I guarantee you there's no problem, I guarantee.",
        "location": "New York, USA",
        "company": "SoundCloud",
        "email": "jobs@soundcloud.com",
        "created_at": "2017-12-28T23:50:49.661760Z"
    }
]
```