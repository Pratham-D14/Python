setTiming: int = 10
users = ["u1", "u1", "u2", "u2", "u3", "u3", "u1"]
timers = [1, 2, 4, 18, 4, 6, 20]

store = {}
session = {}  # <- use if you want to track each user session
totalCount = 0


def countSession(timing: int, users, timers) -> None:
    global totalCount
    for i in range(len(users)):
        if users[i] not in store:
            store[users[i]] = timers[i]
            session[users[i]] = 1
            totalCount += 1
        else:
            if timers[i] - store[users[i]] > timing:
                store[users[i]] = timers[i]
                session[users[i]] += 1
                totalCount += 1


countSession(setTiming, users, timers)
print(totalCount)
