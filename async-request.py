import asyncio
import datetime
import requests
import httpx

url_list = [
    "https://badidesign.ir/wp-content/uploads/2021/11/logo-small-1.png",
    "https://badidesign.ir/wp-content/uploads/2021/11/logo-medium-1.png",
    "https://badidesign.ir/wp-content/uploads/2021/11/pr.png",
    "https://badidesign.ir/wp-content/uploads/2021/11/undraw_design_components_9vy6.png",
    "https://badidesign.ir/wp-content/uploads/2022/02/undraw_social_influencer_re_beim.png",
    "https://badidesign.ir/wp-content/uploads/2022/02/inst.png",
    "https://badidesign.ir/wp-content/uploads/2022/02/des2-8.png",
    "https://badidesign.ir/wp-content/uploads/2022/02/undraw_web_devices_re_m8sc.png",
    "https://badidesign.ir/wp-content/uploads/2022/02/pro-1.png",
    "https://badidesign.ir/wp-content/uploads/2022/03/logo-profile.jpg",
    "https://badidesign.ir/wp-content/uploads/elementor/thumbs/contact-pg0nurgs2eo6a8mvz6f82v70n6b1wms56nriqhnx4o.png",
    "https://badidesign.ir/wp-content/uploads/elementor/thumbs/design-pg0ntheorix4hchsg4ii6otfjam2fgpaobsq7xk7lk.png",
    "https://badidesign.ir/wp-content/uploads/elementor/thumbs/support-3-pg0npvoykdzjz5q7hkfzmljtk4dex8ec6hrpzqwjg8.png",
]


async def async_fetch_images():
    tasks = []
    async with httpx.AsyncClient() as client:
        for url in url_list:
            tasks.append(client.get(url))
        res = await asyncio.gather(*tasks)
    return res


def sync_fetch_images():
    for url in url_list:
        yield requests.get(url)


def main():
    print('# Running as Sync:')
    start_of_sync = datetime.datetime.now()
    sync_result = list(sync_fetch_images())
    end_of_sync = datetime.datetime.now()
    print('Sync  Results:', sync_result, '\n', 'Sync Time: ', end_of_sync - start_of_sync, )

    print('=*=' * 20)

    print('# Running as Async:')
    start_of_async = datetime.datetime.now()
    async_result = list(asyncio.run(async_fetch_images()))
    end_of_async = datetime.datetime.now()
    print('Async Results:', async_result, '\n', 'Async Time: ', end_of_async - start_of_async, )


if __name__ == '__main__':
    main()
