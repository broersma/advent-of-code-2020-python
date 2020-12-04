def _get_input(day, year):

    if not (1 <= day <= 25):
        raise ValueError(f"day must be between 1 and 25 inclusive, is {day}")

    if not (2015 <= year <= 2999):
        raise ValueError(f"year must be between 2015 and 2999 inclusive, is {year}")

    import os

    cache_file_name = 'day{0}.txt'.format(day)

    if not os.path.isfile(cache_file_name):
        import urllib.request
        import shutil

        url = "https://adventofcode.com/{0}/day/{1}/input".format(year, day)
        req = urllib.request.Request(url)

        # cookie.txt should be in your .gitignore and contain 'session=<your advent of code session id>'
        with open('cookie.txt', 'r') as cookie:
            req.add_header('Cookie', cookie.read().strip())

        try:
            with urllib.request.urlopen(req) as input, open(cache_file_name, 'wb') as output:
                shutil.copyfileobj(input, output)
        except urllib.error.HTTPError:
            return

        # Open the most relevant files in Notepad++
        os.system(f'start notepad++ {cache_file_name}')
        os.system(f'start notepad++ {day}_1.py')

    with open(cache_file_name, 'rb') as input:
        return input.read().decode("utf-8").rstrip()


def _submit(answer, star, day, year, reopen=True):
    """
    Based on wimglenn's aocd.py
    """
    import requests
    import bs4
    import webbrowser

    if star not in {1, 2}:
        raise ValueError(f"star must be 1 or 2, is {star}")
    if not (1 <= day <= 25):
        raise ValueError(f"day must be between 1 and 25 inclusive, is {day}")
    if not (2015 <= year <= 2999):
        raise ValueError(f"year must be between 2015 and 2999 inclusive, is {year}")

    url = "https://adventofcode.com/{0}/day/{1}/answer".format(year, day)

    with open('cookie.txt', 'r') as cookie:
        session_string = cookie.read().strip()
        if session_string.startswith("session="):
            session = session_string[8:]
    response = requests.post(
        url,
        cookies={"session": session},
        headers={"User-Agent": "little_helper.py/v1"},
        data={"level": star, "answer": answer},
    )
    if not response.ok:
        raise RuntimeError("Non-200 response for POST: {}".format(response))
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    message = soup.article.text
    if _is_right_answer(message):
        if reopen:
            webbrowser.open(response.url)  # So you can read part B on the website...
    return message


def _is_right_answer(message):
    return "That's the right answer" in message


def _get_day(answer_file_name):
    return int(answer_file_name.split('_', 1)[0])


def _get_star(answer_file_name):
    if answer_file_name.endswith("_1.py"):
        return 1
    elif answer_file_name.endswith("_2.py"):
        return 2


def help(year, answer_file_name, answer_function):

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--submit', help='submit the current answer', action='store_true', default=False)
    args = parser.parse_args()

    day = _get_day(answer_file_name)
    star = _get_star(answer_file_name)

    input = _get_input(day, year)

    the_answer = answer_function(input)

    if not the_answer or not args.submit:
        print(f"\033[92mCurrent answer:\033[0m \033[1m{the_answer}\033[0m")
    else:
        print(f"\033[92mSubmitting '\033[0m\033[1m{the_answer}\033[0m\033[92m' for day {day} star {star}\033[0m")
        message = _submit(the_answer, star, day, year)
        print(message)
        if star == 1 and _is_right_answer(message):
            # Try to create a file for the second part
            import os
            new_file_name = answer_file_name.replace('_1.py', '_2.py')
            if not os.path.isfile(new_file_name):
                import shutil
                shutil.copy(answer_file_name, new_file_name)
                print(f"\033[92mCopied '{answer_file_name}' to '{new_file_name}'\033[0m")
            else:
                print(f"\033[93m'{new_file_name}' already exists, didn't copy '{answer_file_name}'\033[0m")

            # Open the new file in Notepad++
            os.system(f'start notepad++ {day}_2.py')
