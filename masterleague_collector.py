import requests
import json

# Note 60 requests per minute and up to 1'000 requests per 24 hours
# Keep routes fresh

# collecting the latest routes

data_folder = "data/"
root_req = requests.get("https://api.masterleague.net/?format=json")
api_route = root_req.json()


def write_file(filename, content):
    with open("{}".format(filename), "w") as fout:
        json.dump(content, fout)


def collect_heroes():
    # Had to handle this different than the other calls to get all
    # paginated results
    index = 1
    stop = False
    valid_links = []
    paginated_users = []
    while stop is False:
        req = requests.get("https://api.masterleague.net/heroes/?format=json&page={}".format(index))
        if req.status_code is 200:
            valid_links.append(req.url)
            index += 1
            res = req.json()
            for each_user in res['results']:
                paginated_users.append(each_user)
        else:
            stop = True
    master_record = {"count": len(paginated_users), "results": paginated_users}
    write_file(filename=data_folder + "heroes.json", content=master_record)





def collect_maps():
    req = requests.get(api_route['maps'])
    res = req.json()
    write_file(filename=data_folder + "maps.json", content=res)


def collect_regions():
    req = requests.get(api_route['regions'])
    res = req.json()
    write_file(filename=data_folder + "regions.json", content=res)


def collect_patches():
    req = requests.get(api_route['patches'])
    res = req.json()
    write_file(filename=data_folder + "patches.json", content=res)


def collect_teams():
    req = requests.get(api_route['teams'])
    res = req.json()
    write_file(filename=data_folder + "teams.json", content=res)


def collect_players():
    req = requests.get(api_route['players'])
    res = req.json()
    write_file(filename=data_folder + "players.json", content=res)


def collect_tournaments():
    req = requests.get(api_route['tournaments'])
    res = req.json()
    write_file(filename=data_folder + "tournaments.json", content=res)


def collect_matches():
    req = requests.get(api_route['matches'])
    res = req.json()
    write_file(filename=data_folder + "matches.json", content=res)


def collect_calender():
    req = requests.get(api_route['calendar'])
    res = req.json()
    write_file(filename=data_folder + "calendar.json", content=res)


def collect_all():
    collect_heroes()
    collect_maps()
    collect_players()
    collect_teams()
    collect_matches()
    collect_patches()
    collect_tournaments()
    collect_calender()


def main():
    collect_all()


if __name__ in '__main__':
    main()
