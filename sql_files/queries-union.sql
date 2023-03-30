create table all_leagues as
select *
from aus_bundesliga
union all
select *
from bundesliga
union all
select *
from eredivisie
union all
select *
from jupiler
union all
select *
from la_liga
union all
select *
from liga_portugal
union all
select *
from ligue_1
union all
select *
from premier_league
union all
select *
from premier_liga
union all
select *
from serie_a
union all
select *
from super_lig;

alter table all_leagues
add primary key (club);

select * from all_leagues
