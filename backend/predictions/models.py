from django.db import models

class Predictions(models.Model):
    matchId = models.IntegerField()
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    gold =  models.IntegerField()
    cs = models.IntegerField()

    def getData(self):
        return {
            "kills" : self.kills,
            "deaths" : self.deaths,
            "assists" : self.assists,
            "gold" : self.gold,
            "cs" : self.cs
        }
    
    def __str__(self):
        return f"Predictions(match_id={self.match_id}, 
                            kills={self.kills}, 
                            deaths={self.deaths}, 
                            assists={self.assists}, 
                            gold={self.gold}, 
                            cs={self.cs})"