import request.request as req

def add_critiques(data):
    """
    Crée une critique dans la base de données.
    :param data: dictionnaire contenant les informations de la critique.
    :return: l'id de la critique créée.
    """
    if (
        not "attraction_id" in data
        or not "nom" in data
        or not "prenom" in data
        or not "texte" in data
        or not "note" in data
    ):
        return False

    requete = """
        INSERT INTO critiques (attraction_id, nom, prenom, texte, note)
        VALUES (?, ?, ?, ?, ?);
    """

    id = req.insert_in_db(
        requete,
        (
            data["attraction_id"],
            data["nom"],
            data["prenom"],
            data["texte"],
            data["note"],
        ),
    )

    return id

def get_all_critiques():
    """
    Récupère toutes les critiques de la base de données.
    :return: une liste de critiques.
    """
    json = req.select_from_db("SELECT * FROM critiques")

    return json

def get_paginated_critiques(page_size=10, page_index=1):
    """
    Récupère les critiques paginées de la base de données.
    :param page_size: nombre de critiques par page.
    :param page_index: index de la page.
    :return: un dictionnaire contenant les critiques paginées et le nombre total de critiques.
    """
    # Calculate the offset based on page size and index
    offset = (page_index - 1) * page_size

    # Fetch paginated critiques with attraction names from the database
    requete = f"""
        SELECT c.*, a.nom as attraction_nom
        FROM critiques c
        JOIN attraction a ON c.attraction_id = a.attraction_id
        ORDER BY c.id DESC
        LIMIT {page_size} OFFSET {offset}
    """
    paginated_critiques = req.select_from_db(requete)

    # Get the total number of critiques (for pagination info)
    total_critiques = len(req.select_from_db("SELECT * FROM critiques"))

    return {
        'critiques': paginated_critiques,
        'totalCritiques': total_critiques,
    }

def get_critiques_for_attraction(page_size=10, page_index=1, attraction_id=1):
    """
    Récupère les critiques paginées pour une attraction spécifique de la base de données.
    :param page_size: nombre de critiques par page.
    :param page_index: index de la page.
    :param attraction_id: id de l'attraction.
    :return: un dictionnaire contenant les critiques paginées et le nombre total de critiques pour l'attraction spécifiée.
    """

    # Calculate the offset based on page size and index
    offset = (page_index - 1) * page_size

    # Fetch paginated critiques with attraction names from the database
    requete = f"""
        SELECT c.*, a.nom as attraction_nom
        FROM critiques c
        JOIN attraction a ON c.attraction_id = a.attraction_id
        WHERE c.attraction_id = ?  -- Filter critiques for the specified attraction_id
        ORDER BY c.id DESC  -- Order by id in descending order
        LIMIT {page_size} OFFSET {offset}
    """

    paginated_critiques = req.select_from_db(requete, (attraction_id,))
    # Get the total number of critiques for the specified attraction (for pagination info)
    total_critiques = len(req.select_from_db("SELECT * FROM critiques WHERE attraction_id = ?", (attraction_id,)))

    return {
        'critiques': paginated_critiques,
        'totalCritiques': total_critiques,
    }

def get_critiques(id):
    """
    Récupère une critique de la base de données.
    :param id: id de la critique.
    :return: une critique.
    """
    if not id:
        return False

    json = req.select_from_db(
        "SELECT * FROM critiques WHERE id = ?",
        (id,),
    )

    if len(json) > 0:
        return json[0]
    else:
        return []

def get_moyenne_note(attraction_id):
    """
    Récupère la moyenne des notes d'une attraction.
    :param attraction_id: id de l'attraction.
    :return: la moyenne des notes.
    """
    if not attraction_id:
        return False

    # Requête SQL pour obtenir la moyenne des notes
    sql = """
    SELECT AVG(note) AS moyenne
    FROM critiques
    WHERE attraction_id = ?
    """

    # Exécution de la requête
    json = req.select_from_db(sql, (attraction_id,))

    # Si l'attraction n'a pas de critique, on retourne None
    if len(json) == 0:
        return None

    # On extrait la moyenne du résultat
    moyenne = json[0]["moyenne"]

    return moyenne

def delete_critiques(id):
    """
    Supprime une critique de la base de données.
    :param id: id de la critique.
    :return: un booléen indiquant si la suppression a été effectuée.
    """
    if not id:
        return False

    req.delete_from_db("DELETE FROM critiques WHERE id = ?", (id,))

    return True

def update_critiques(data):
    """
    Met à jour une critique dans la base de données.
    :param data: dictionnaire contenant les informations de la critique.
    :return: un booléen indiquant si la mise à jour a été effectuée.
    """
    if (
        not "id" in data
        or not "attraction_id" in data
        or not "nom" in data
        or not "prenom" in data
        or not "texte" in data
        or not "note" in data
    ):
        return False

    requete = """
        UPDATE critiques
        SET attraction_id=?, nom=?, prenom=?, texte=?, note=?
        WHERE id = ?;
    """

    req.insert_in_db(
        requete,
        (
            data["attraction_id"],
            data["nom"],
            data["prenom"],
            data["texte"],
            data["note"],
            data["id"],
        ),
    )

    return True
