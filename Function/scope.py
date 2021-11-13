MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    if age < MIN_DRIVING_AGE:
        print(name,'ещё рано садиться за руль')
    if age >= MIN_DRIVING_AGE:
        print(name,'может водить')

allowed_driving('tim', 16)
allowed_driving('tom', 18)
allowed_driving('tamara', 19)
allowed_driving('timoti', 32)