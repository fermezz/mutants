import random

from locust import HttpLocust, TaskSet, between, task


DNA_NUCLEOBASES = ["A", "C", "G", "T"]


class UserBehavior(TaskSet):

    @task
    def is_mutant(self):
        dna_matrix = generate_matrix(random.randint(4, 10))
        with self.client.post("/api/mutant/", json={"dna": dna_matrix}, catch_response=True) as response:
            if response.status_code == 403:
                response.success()


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1, 3)


def generate_matrix(size):
    return [
        [
            DNA_NUCLEOBASES[random.randint(0, 3)] for _j in range(size)
        ] for _i in range(size)
    ]
