import json

def lambda_handler(event, context):
    golden_boot_winners = [
        {"season": "1992/93", "player": "Teddy Sheringham", "club": "NFO/TOT", "goals": 22},
        {"season": "1993/94", "player": "Andrew Cole", "club": "NEW", "goals": 34},
        {"season": "1994/95", "player": "Alan Shearer", "club": "BLB", "goals": 34},
        {"season": "1995/96", "player": "Alan Shearer", "club": "BLB", "goals": 31},
        {"season": "1996/97", "player": "Alan Shearer", "club": "NEW", "goals": 25},
        {"season": "1997/98", "player": "Dion Dublin", "club": "COV", "goals": 18},
        {"season": "1997/98", "player": "Michael Owen", "club": "LIV", "goals": 18},
        {"season": "1997/98", "player": "Chris Sutton", "club": "BLB", "goals": 18},
        {"season": "1998/99", "player": "Michael Owen", "club": "LIV", "goals": 18},
        {"season": "1998/99", "player": "Dwight Yorke", "club": "MUN", "goals": 18},
        {"season": "1999/00", "player": "Kevin Phillips", "club": "SUN", "goals": 30},
        {"season": "2000/01", "player": "Jimmy Floyd Hasselbaink", "club": "CHE", "goals": 23},
        {"season": "2001/02", "player": "Thierry Henry", "club": "ARS", "goals": 24},
        {"season": "2002/03", "player": "Ruud van Nistelrooy", "club": "MUN", "goals": 25},
        {"season": "2003/04", "player": "Thierry Henry", "club": "ARS", "goals": 30},
        {"season": "2004/05", "player": "Thierry Henry", "club": "ARS", "goals": 25},
        {"season": "2005/06", "player": "Thierry Henry", "club": "ARS", "goals": 27},
        {"season": "2006/07", "player": "Didier Drogba", "club": "CHE", "goals": 20},
        {"season": "2007/08", "player": "Cristiano Ronaldo", "club": "MUN", "goals": 31},
        {"season": "2008/09", "player": "Nicolas Anelka", "club": "CHE", "goals": 19},
        {"season": "2009/10", "player": "Didier Drogba", "club": "CHE", "goals": 29},
        {"season": "2010/11", "player": "Carlos Tevez", "club": "MCI", "goals": 20},
        {"season": "2010/11", "player": "Dimitar Berbatov", "club": "MUN", "goals": 20},
        {"season": "2011/12", "player": "Robin van Persie", "club": "ARS", "goals": 30},
        {"season": "2012/13", "player": "Robin van Persie", "club": "MUN", "goals": 26},
        {"season": "2013/14", "player": "Luis Suarez", "club": "LIV", "goals": 31},
        {"season": "2014/15", "player": "Sergio Aguero", "club": "MCI", "goals": 26},
        {"season": "2015/16", "player": "Harry Kane", "club": "TOT", "goals": 25},
        {"season": "2016/17", "player": "Harry Kane", "club": "TOT", "goals": 29},
        {"season": "2017/18", "player": "Mohamed Salah", "club": "LIV", "goals": 32},
        {"season": "2018/19", "player": "Pierre-Emerick Aubameyang", "club": "ARS", "goals": 22},
        {"season": "2018/19", "player": "Sadio Mane", "club": "LIV", "goals": 22},
        {"season": "2018/19", "player": "Mohamed Salah", "club": "LIV", "goals": 22},
        {"season": "2019/20", "player": "Jamie Vardy", "club": "LEI", "goals": 23},
        {"season": "2020/21", "player": "Harry Kane", "club": "TOT", "goals": 23},
        {"season": "2021/22", "player": "Mohamed Salah", "club": "LIV", "goals": 23},
        {"season": "2021/22", "player": "Son Heung-min", "club": "TOT", "goals": 23},
        {"season": "2022/23", "player": "Erling Haaland", "club": "MCI", "goals": 36},
        {"season": "2023/24", "player": "Erling Haaland", "club": "MCI", "goals": 27}
    ]
    
    return {
        'statusCode': 200,
        'body': json.dumps(golden_boot_winners)
    }
