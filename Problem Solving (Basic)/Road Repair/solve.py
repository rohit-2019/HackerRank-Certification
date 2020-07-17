def getMinCost(crew_id, job_id):
    crew_id = sorted(crew_id)
    job_id = sorted(job_id)
    sum = 0
    for i in range(len(crew_id)):
        add = job_id[i]-crew_id[i]
        sum += abs(add)
    return  sum