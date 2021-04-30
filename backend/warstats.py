from database.database import Database


def members_war_stats():
    db = Database()
    stats = []
    tags = member_tags(db.get_members_table())

    for i in range(0, len(tags)):
        member_war_attacks = db.get_members_war_attacks(tags[i])
        member_results = calc_avg(member_war_attacks, tags[i])
        if member_results != None:
            stats.append(member_results)

    db.close_connection()
    return stats


def member_tags(members):
    tags = []

    for i in range(0, len(members)):
        tags.append(members[i][0])

    return tags


def calc_avg(attacks, tag):
    total_stars = 0
    total_destruction = 0
    total_attacks = 0

    for attack in attacks:
        if attack[2] == "T":
            total_stars += attack[3]
            total_destruction += attack[4]
            total_attacks += 1
        if attack[5] == "T":
            total_stars += attack[6]
            total_destruction += attack[7]
            total_attacks += 1

    if len(attacks) > 0 and total_attacks == 0:
        return {"tag": tag, "stars": 0, "destruction": 0, "reliability": 0}

    if total_attacks == 0:
        return None

    return {
        "tag": tag,
        "stars": total_stars / total_attacks,
        "destruction": total_destruction / total_attacks,
        "reliability": total_attacks / (2 * len(attacks)),
    }


members_war_stats()
