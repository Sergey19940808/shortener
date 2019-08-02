import celery


@celery.shared_task
def count_shortener(user_id, short_link):
    pass