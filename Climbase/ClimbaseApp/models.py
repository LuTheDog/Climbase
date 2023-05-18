from django.db import models

class Admin(models.Model):
    userid = models.OneToOneField('User', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class Category(models.Model):
    categoryid = models.AutoField(db_column='CategoryId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    symbol = models.CharField(db_column='Symbol', max_length=20)  # Field name made lowercase.
    agemin = models.IntegerField(db_column='AgeMin', blank=True, null=True)  # Field name made lowercase.
    agemax = models.IntegerField(db_column='AgeMax', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'


class Club(models.Model):
    clubid = models.AutoField(db_column='ClubId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'club'


class Competed(models.Model):
    competitorid = models.OneToOneField('Competitor', models.DO_NOTHING, db_column='CompetitorId', primary_key=True)  # Field name made lowercase. The composite primary key (CompetitorId, CompetitionId) found, that is not supported. The first column is selected.
    competitionid = models.ForeignKey('Competition', models.DO_NOTHING, db_column='CompetitionId')  # Field name made lowercase.
    placement = models.IntegerField(db_column='Placement', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'competed'
        unique_together = (('competitorid', 'competitionid'),)


class Competition(models.Model):
    competitionid = models.AutoField(db_column='CompetitionId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('Organizer', models.DO_NOTHING, db_column='UserId', blank=True, null=True)  # Field name made lowercase.
    categoryid = models.ForeignKey(Category, models.DO_NOTHING, db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'competition'


class Competitor(models.Model):
    competitorid = models.AutoField(db_column='CompetitorId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=200)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1)  # Field name made lowercase.
    jmbg = models.CharField(db_column='JMBG', max_length=13)  # Field name made lowercase.
    dateofbirth = models.DateTimeField(db_column='DateOfBirth')  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId')  # Field name made lowercase.
    totalpoints = models.IntegerField(db_column='TotalPoints', blank=True, null=True)  # Field name made lowercase.
    clubid = models.IntegerField(db_column='ClubId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'competitor'


class Isincompetition(models.Model):
    routeid = models.OneToOneField('Route', models.DO_NOTHING, db_column='RouteId', primary_key=True)  # Field name made lowercase. The composite primary key (RouteId, CompetitionId) found, that is not supported. The first column isselected.
    competitionid = models.ForeignKey(Competition, models.DO_NOTHING, db_column='CompetitionId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'isincompetition'
        unique_together = (('routeid', 'competitionid'),)


class Judge(models.Model):
    userid = models.OneToOneField('User', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'judge'


class Judged(models.Model):
    competitionid = models.OneToOneField(Competition, models.DO_NOTHING, db_column='CompetitionId', primary_key=True)  # Field name made lowercase. The composite primary key (CompetitionId, UserId) found, that is not supported. Thefirst column is selected.
    userid = models.ForeignKey(Judge, models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'judged'
        unique_together = (('competitionid', 'userid'),)


class Organizer(models.Model):
    userid = models.OneToOneField('User', models.DO_NOTHING, db_column='UserId', primary_key=True)  # Field name made lowercase.
    clubid = models.ForeignKey(Club, models.DO_NOTHING, db_column='ClubId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'organizer'


class Points(models.Model):
    place = models.IntegerField(db_column='Place', blank=True, null=True)  # Field name made lowercase.
    amount = models.IntegerField(db_column='Amount', blank=True, null=True)  # Field name made lowercase.
    pointsid = models.AutoField(db_column='PointsID', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'points'


class Route(models.Model):
    routeid = models.AutoField(db_column='RouteId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, blank=True, null=True)  # Field name made lowercase.
    routesetter = models.CharField(db_column='Routesetter', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'route'


class Score(models.Model):
    competitorid = models.OneToOneField(Competitor, models.DO_NOTHING, db_column='CompetitorId', primary_key=True)  # Field name made lowercase. The composite primary key (CompetitorId, CompetitionId, RouteId) found, that is not supported. The first column is selected.
    competitionid = models.ForeignKey(Competed, models.DO_NOTHING, db_column='CompetitionId', to_field='CompetitionId')  # Field name made lowercase.
    routeid = models.ForeignKey(Isincompetition, models.DO_NOTHING, db_column='RouteId')  # Field name made lowercase.
    zone = models.IntegerField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.
    zoneattempts = models.IntegerField(db_column='ZoneAttempts', blank=True, null=True)  # Field name made lowercase.
    top = models.IntegerField(db_column='Top', blank=True, null=True)  # Field name made lowercase.
    topattempts = models.IntegerField(db_column='TopAttempts', blank=True, null=True)  # Field name made lowercase.
    judgeid = models.ForeignKey(Judged, models.DO_NOTHING, db_column='JudgeId', to_field='UserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'score'
        unique_together = (('competitorid', 'competitionid', 'routeid'),)


class User(models.Model):
    userid = models.AutoField(db_column='UserId', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=200)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=200)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'

