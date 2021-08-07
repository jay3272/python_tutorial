def ask_ok(prompt,retries=5,reminder='Please try again'):
    while True:
        ok=input(prompt)
        if ok in ('yes'):
            return True
        if ok in ('no'):
            retries=retries-1
            if retries<0:
                raise ValueError('invalid user response')
            print(reminder)


ask_ok('離開按yes或no:')
ask_ok('ok',2)
ask_ok('ok',2,'請再試一次')




















