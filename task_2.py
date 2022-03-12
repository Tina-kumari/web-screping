from task_1 import scrapped
import json
years=[]
def group_of_same_year(movie):
    # years=[]
    for i in movie:
        year=i["Year"]
        # print(i)
        if year not in years:
            years.append(year)
    # print(years)
    dict_movie={i:[]for i in years}
    # print(dict_fMovies)  
    for i in movie:
        year=i["Year"]
        for x in dict_movie:
            if (x)==(year):
                dict_movie[x].append(i)
    with open("grup of movie.json","w")as file:
        json.dump(dict_movie,file,indent=3)
    return(dict_movie)
group_of_same_year(scrapped)





