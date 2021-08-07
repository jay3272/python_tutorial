def ask_ok(prompt,retries=5,remider="Please try again"):
    while True:
        ok=input(prompt)
        if ok in ('yes'):
            return True
        if ok in ('no'):
            retries=retries-1
            if retries<0:
                raise ValueError('invalid User response')
            print(remider)

ask_ok('離開按Yes 或 no ：')
ask_ok('ok :',2)
ask_ok('ok :',2,'請再試一次')