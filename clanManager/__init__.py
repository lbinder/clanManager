from flask import Flask, render_template
try:
    from clanManager.database import database
except:
    from database import database
app = Flask(__name__)

@app.route("/")
def index():
    db = database.DataBase()
    members = db.get_members()
    data = sorted(collect_member_info(members, db), key = lambda i: (i['part_war'], i['star_avg'], i['dest_avg']), reverse=True)
    
    print(data)
    return render_template('index.html', data=data)

def collect_member_info(members, db):
    clan_info = []
    
    for member in members:
        tag = member[0]
        war_data = db.get_members_war_attacks(tag)
        war_stats = calculate_war_stats(war_data)
        clan_info.append({'name': member[1],
                          'joined': member[2],
                          'part_war': war_stats['participation'] * 100,
                          'star_avg': war_stats['average_stars'],
                          'dest_avg': war_stats['average_destruction']})
    
    return clan_info
        

def calculate_war_stats(war_stats):
    tot_attacks = 0
    used_attacks = 0
    tot_missed = 0
    tot_stars = 0.0
    tot_destruction = 0.0

    attack_one_used = 2
    attack_two_used = 5
    stars_attack_one = 3
    stars_attack_two = 6
    destruction_attack_one = 4
    destruction_attack_two = 7

    result = {'participation': 0,
              'average_stars': 0,
              'average_destruction': 0}

    for row in war_stats:
        tot_attacks += 2
        if row[attack_one_used] == 'T':
            used_attacks += 1
            tot_stars += float(row[stars_attack_one])
            tot_destruction += float(row[destruction_attack_one])
        if row[attack_two_used] == 'T':
            used_attacks += 1
            tot_stars += float(row[stars_attack_two])
            tot_destruction += float(row[destruction_attack_two])

    if (used_attacks != 0):
        result['participation'] = (used_attacks/tot_attacks)
        result['average_stars'] = (tot_stars/used_attacks)
        result['average_destruction'] = (tot_destruction/used_attacks)

    return result
    

if __name__ == "__main__":
    app.run()
