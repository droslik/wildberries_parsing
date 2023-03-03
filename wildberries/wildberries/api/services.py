import aiohttp
import asyncio


def get_url_data(article):
    """
    Function defines vol and part as elements of url address
    """
    if len(str(article)) > 5:
        vol = int(str(article)[0:-5])
        part = int(str(article)[0:-3])
    else:
        if len(str(article)) < 4:
            vol = 0
            part = 0
        else:
            vol = 0
            part = int(str(article)[0:-3])
    return vol, part


async def create_single_task(session, article):
    """
    Functions creates each particular task
    and returns result after its execution
    """
    for basket_number in range(1, 10):
        vol, part = get_url_data(article)
        async with session.get(
            f"https://basket-0{basket_number}.wb.ru/"
            f"vol{vol}/"
            f"part{part}/"
            f"{article}/info/ru/card.json"
        ) as resp:
            if resp.status != 200:
                continue
            if resp.status == 200:
                json_data = await resp.json()
                title = json_data.get("imt_name", json_data.get("subj_name"))
                article = json_data["nm_id"]
                brand = json_data.get("selling", None).get("brand_name", None)
                data = {"title": title, "brand": brand, "article": article}
                return data
            return None


async def gather_all_tasks(session, articles):
    """
    Function gathers all tasks on parsing and returns all results of the tasks
    """
    tasks = []
    for article in articles:
        task = asyncio.create_task(create_single_task(session, article))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results


async def parsing_main(articles):
    """
    Functions runs parsing process and returns gathered result of
    every parsed article
    """
    async with aiohttp.ClientSession(trust_env=True) as session:
        response = await gather_all_tasks(session, articles)
        items = [result for result in response if result is not None]
        if len(items) > 1:
            return items
        if len(items) != 0:
            return items[0]
        return None
