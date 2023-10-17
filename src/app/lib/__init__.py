def get_films(argument):
    # n = args.get('n')
    film_list = []
    for i in range(argument):
        film_list.append({'id': i, 'title': f'Awaking{i}', 'year': f'199{i}', 'description': f'About doctor number {i}', 'image': f'/images/film{i}.jpg', 'date': f'2019-03-0{i}'})

    return film_list
